# Redis basics
Redis is a special kind of database that stores information in a way that's super fast to access

## Install Redis on Ubuntu 18.04
```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
## Use Redis in a container
```
sudo service redis-server start
```