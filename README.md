# Installation
1. Download Damn Vulnerable Web Application Docker container from Docker 
Hub: https://hub.docker.com/r/vulnerables/web-dvwa/

2. Run it:
<code>
$ docker run --rm -it -p 11985:80 vulnerables/web-dvwa
</code>

3. Download and run Redis Docker Container:
<pre>
$ docker run --name some-redis -p 6380:6379 -d redis redis-server --appendonly yes
</pre>

3. Clone the crawler from https://github.com/calinrada/appcheck: 
<pre>
$ git clone https://github.com/calinrada/appcheck.git
</pre>