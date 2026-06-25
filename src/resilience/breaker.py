"""Circuit breaker + retry policy for flaky downstream payment provider calls."""
import time


class CircuitBreaker:
    def __init__(self, fail_max=5, reset_timeout=30):
        self.fail_max = fail_max
        self.reset_timeout = reset_timeout
        self._failures = 0
        self._opened_at = None

    def allow(self):
        if self._opened_at and time.time() - self._opened_at < self.reset_timeout:
            return False
        return True

    def record(self, ok):
        if ok:
            self._failures = 0
            self._opened_at = None
        else:
            self._failures += 1
            if self._failures >= self.fail_max:
                self._opened_at = time.time()