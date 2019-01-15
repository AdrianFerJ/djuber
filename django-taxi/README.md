# Taxi App
https://testdriven.io/courses/real-time-app-with-django-channels-and-angular/part-one-getting-started/

## SETUP

### 1. Set Up env
```
# install pipenv
$ pipenv --python 3.7  # or path/to/python ... like the python used in django-docker pipenv

# Make sure pip is not v18.1 (src: https://github.com/pypa/pipenv/issues/2924)
$ pip install pipenv
$ pipenv run pip install pip==18.0
$ pipenv install

# Install packages
$ pip install \
       channels==2.1.2 \
       channels-redis==2.3.0 \
       Django==2.1 \
       djangorestframework==3.8.2 \
       nose==1.3.7 \
       Pillow==5.2.0 \
       pytest-asyncio==0.9.0 \
       pytest-django==3.4.2
```

#### 2. Set Up Redis
(src: https://redis.io/topics/quickstart
)
**IF not installed:**
```
# install Redis
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make

# move src and bin to proper places
sudo cp src/redis-server /usr/local/bin/
sudo cp src/redis-cli /usr/local/bin/
```
Test server
```
# run server, on new terminal
redis-server

# ping server, back on previous terminal
redis-cli ping
```