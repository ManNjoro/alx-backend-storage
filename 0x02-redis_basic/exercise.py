#!/usr/bin/env python3
'''
A script to interface with Redis and store data with random keys
'''
import redis
import uuid
from typing import Union


class Cache:
    """
    A Cache class to interface with Redis and store data with random keys.
    """

    def __init__(self):
        """
        Initialize the Cache instance.
        Connects to the Redis server and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key.
        """
        # Generate a random key using uuid
        key = str(uuid.uuid4())

        # Store the data in Redis with the generated key
        if isinstance(data, str):
            self._redis.set(key, data)
        elif isinstance(data, bytes):
            self._redis.set(key, data)
        elif isinstance(data, int) or isinstance(data, float):
            self._redis.set(key, str(data))

        # Return the generated key
        return key