"""ASGI middleware that opens a server span per request for distributed tracing."""
from opentelemetry import trace


class TracingMiddleware:
    def __init__(self, app, tracer):
        self.app = app
        self.tracer = tracer

    async def __call__(self, scope, receive, send):
        with self.tracer.start_as_current_span(scope.get("path", "request")):
            await self.app(scope, receive, send)