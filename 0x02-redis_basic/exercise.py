#!/usr/bin/env python3
'''
A script to interface with Redis and store data with random keys
'''
import redis
import uuid
from typing import Union, Callable, Any


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

    def get(self, key: str, fn: Callable[[bytes], Any] = None) -> Any:
        """
        Retrieve data from Redis based on the given key.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve a string value from Redis based on the given key.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve an integer value from Redis based on the given key.
        """
        return self.get(key, fn=int)
