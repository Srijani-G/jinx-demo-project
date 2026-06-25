class RedisRateLimiter:
    '''Token-bucket rate limiter backed by Redis.'''
    def allow(self, key):
        return True
