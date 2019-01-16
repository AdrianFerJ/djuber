from channels.generic.websocket import AsyncJsonWebsocketConsumer


class TaxiConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        user = self.scope['user']
        if user.is_anonymous:
            await self.close()
        else:
            await self.accept()
    
    async def receive_json(self, content, **kwargs):
        """Here comes business logic to process different message types"""
        message_type = content.get('type')
        if message_type == 'create.trip':
            await self.create_trip(content)

    async def create_trip(self, event):
        """
        creates a new trip (by calling _create_trip) and passes the details back to the client
        """
        trip = await self._create_trip(event.get('data'))
        trip_data = ReadOnlyTripSerializer(trip).data
        await self.send_json({
            'type': 'MESSAGE',
            'data': trip_data
        })

    @database_sync_to_async
    def _create_trip(self, content):
        """ Creates a new trip, does the actual database update """
        serializer = TripSerializer(data=content)
        serializer.is_valid(raise_exception=True)
        trip = serializer.create(serializer.validated_data)
        return trip