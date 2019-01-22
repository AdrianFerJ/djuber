# Taxi App
Based on Michael Herman's tutorial, at [testdriven.io](https://testdriven.io/courses/real-time-app-with-django-channels-and-angular/part-one-getting-started/)

## SETUP

### 1. Set Up Python (venv) and Django 
```bash
# install pipenv
$ pipenv --python 3.7  # or path/to/python ... like the python used in django-docker pipenv

# Make sure pip is not v18.1, while venv is active.(Known issue with v18.1, fix src: https://github.com/pypa/pipenv/issues/2924)
$ pip --version

# IF pip==18.1, THEN downgrade to 18.0 (from within venv)
$ pip install pipenv
$ pipenv run pip install pip==18.0
$ pipenv install

# Install packages
$ pip install \
       channels==2.1.2 \
       channels-redis==2.3.0 \
       Django==2.1.5 \
       djangorestframework==3.8.2 \
       nose==1.3.7 \
       Pillow==5.2.0 \
       pytest-asyncio==0.9.0 \
       pytest-django==3.4.2
```

#### 2. Set Up Redis
For more info about Redis setup, check the [docs](https://redis.io/topics/quickstart)

**IF not installed:**
```bash
# install Redis
$ wget http://download.redis.io/redis-stable.tar.gz
$ tar xvzf redis-stable.tar.gz
$ cd redis-stable
$ make

# move src and bin to proper places
$ sudo cp src/redis-server /usr/local/bin/
$ sudo cp src/redis-cli /usr/local/bin/
```
Test server
```bash
# run server, on new terminal
$ redis-server

# ping server, back on previous terminal
$ redis-cli ping
Pong
```

### 3. Set Angular
Requirements npm and node
```bash
#If npm and node.js aren't installed, do that first:
$ sudo snap install node --channel=10/stable --classic
```

Install Angular CLI
```bash
# install
$ npm install -g @angular/cli@6.1.4

# check version
$ ng v
```

Initialize Angular project (from ../taxi-app~)
```bash
$ ng new taxi-ui
$ cd taxi-ui
$ ng serve
# this should take you to Angular's default welcome page
```

If you were taken to the welcome page (http://localhost:4200), Kill server and install packages
```bash
# *NOTE: Could remove package versions to have the latest
$ npm install \
  bootstrap@4.1.3 \
  jquery@3.3.1 \
  popper.js@1.14.4 \
  bootswatch@4.1.3 --save
```
Finally, add css and scripts to angular.json 

### Use tags for versioning
```bash
# example: 
$ git tag -a v1.5 -m "Part 1 chapter 5"
```

