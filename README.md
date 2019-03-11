# Requirements
This software is build and optimized to run having the following requirements / dependency:

* Ubuntu (Ubuntu Server) >= 16.04 / Debian >= 7
* Python >= 3.6.4
* pip >= 19.0.3

# Installation

## Application
<pre>
$ git clone https://github.com/calinrada/appcheck.git
$ cd appcheck
$ pip install virtualenv
$ mkvirtualenv -p /usr/bin/python3.6 appcheck
$ workon appcheck
# cp .env.dist .env
</pre>

## Storage configuration
A storage (database) can be configured. By default only Redis storage is implemented (see storage/RedisStorage.py).
Update your local .env file before running the application. 

## Docker containers
If you don't want to / can't use docker, you can install Redis and DVWA application locally 

* Run DVWA Docker container:
<pre>
$ docker run --rm -it -p 11985:80 vulnerables/web-dvwa
</pre>

* Run Redis Docker Container:
<pre>
$ docker run --name some-redis -p 6380:6379 -d redis redis-server --appendonly yes
</pre>

# Run the application

<code>
$ python run.py
</code>

or in background

<code>
$ nohup python run.py >> debug.log &
</code>

# Todo
* Catch socket and storage connection errors
* Build a docker image containing this app
