# Requirements
* Python >= 3.6
* Virtualenv

# Installation
## Application
<pre>
$ git clone https://github.com/calinrada/appcheck.git
$ cd appcheck
$ mkvirtualenv -p /usr/bin/python3.6 appcheck
$ workon appcheck
</pre>

## Docker containers
* Run DVWA Docker container:
<pre>
$ docker run --rm -it -p 11985:80 vulnerables/web-dvwa
</pre>

* Run Redis Docker Container:
<pre>
$ docker run --name some-redis -p 6380:6379 -d redis redis-server --appendonly yes
</pre>

# Run it

<code>
$ python run.py
</code>

or in background

<code>
$ nohup python run.py >> debug.log &
</code>

# Todo
* Build a docker image containing this app
