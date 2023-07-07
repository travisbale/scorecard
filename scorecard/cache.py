"""Caching implementation."""

import os
import redis


class Cache:
    client = None

    def __init__(self):
        if Cache.client != None:
            return Cache.client
        try:
            client = redis.Redis(host=os.getenv("REDIS_HOST", ""), port=os.getenv("REDIS_PORT", ""), db=0)

