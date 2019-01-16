import asyncio

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from example.models import Trip
from example.serializers import ReadOnlyTripSerializer, TripSerializer


class TaxiConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        user = self.scope['user']
        if user.is_anonymous:
            await self.close()
        else:
            # Get trips and add rider to each one's group.
            channel_groups = []
            self.trips = set(await self._get_trips(self.scope['user']))
            for trip in self.trips:
                channel_groups.append(self.channel_layer.group_add(trip, self.channel_name))
            asyncio.gather(*channel_groups)
            await self.accept()
    
    async def receive_json(self, content, **kwargs):
        """Here comes business logic to process different message types"""
        message_type = content.get('type')
        if message_type == 'create.trip':
            await self.create_trip(content)
    
    async def echo_message(self, event):
        await self.send_json(event)

    async def create_trip(self, event):
        trip = await self._create_trip(event.get('data'))
        trip_data = ReadOnlyTripSerializer(trip).data   
    
        # Handle add only if trip is not being tracked.
        if trip.nk not in self.trips:
            # Add trip to set.
            self.trips.add(trip.nk)
            # Add this channel to the new trip's group.
            await self.channel_layer.group_add(
                group=trip.nk,
                channel=self.channel_name
            )

        await self.send_json({
            'type': 'MESSAGE',
            'data': trip_data
        })

    async def disconnect(self, code):
        # Remove this channel from every trip's group.
        channel_groups = [
            self.channel_layer.group_discard(
                group=trip,
                channel=self.channel_name
            )
            for trip in self.trips
        ]
        asyncio.gather(*channel_groups)

        # Remove all references to trips.
        self.trips.clear()

        await super().disconnect(code)


    @database_sync_to_async
    def _create_trip(self, content):
        """ Creates a new trip, does the actual database update """
        serializer = TripSerializer(data=content)
        serializer.is_valid(raise_exception=True)
        trip = serializer.create(serializer.validated_data)
        return trip