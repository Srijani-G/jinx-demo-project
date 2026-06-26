"""Distributed tracing with OpenTelemetry: spans across our microservices.

Instruments inbound/outbound calls so a single request can be followed end-to-end
across services in the trace backend (Jaeger/Tempo). Reused by every service.
"""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter


def init_tracing(service_name: str, otlp_endpoint: str) -> trace.Tracer:
    provider = TracerProvider()
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=otlp_endpoint)))
    trace.set_tracer_provider(provider)
    return trace.get_tracer(service_name)