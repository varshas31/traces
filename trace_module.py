from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.trace import Status, StatusCode
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
import threading

class SimpleTracer:
    _provider_initialized = False
    _provider_lock = threading.Lock()

    def __init__(self, service_name, jaeger_host='localhost', jaeger_port=6831):
        self.service_name = service_name
        self.jaeger_host = jaeger_host
        self.jaeger_port = jaeger_port
        self._initialize_tracer_provider()

        self.tracer = trace.get_tracer(service_name)

    def _initialize_tracer_provider(self):
        with self._provider_lock:
            if not self._provider_initialized:
                resource = Resource(attributes={
                    SERVICE_NAME: self.service_name
                })
                provider = TracerProvider(resource=resource)

                # Set the tracer provider
                trace.set_tracer_provider(provider)

                # Set up the Jaeger exporter
                jaeger_exporter = JaegerExporter(
                    agent_host_name=self.jaeger_host,
                    agent_port=self.jaeger_port,
                )
                span_processor = BatchSpanProcessor(jaeger_exporter)
                provider.add_span_processor(span_processor)

                # Also log to console
                console_exporter = ConsoleSpanExporter()
                console_span_processor = BatchSpanProcessor(console_exporter)
                provider.add_span_processor(console_span_processor)

                self._provider_initialized = True

    def log(self, span_name, func, *args, **kwargs):
        with self.tracer.start_as_current_span(span_name) as span:
            try:
                result = func(*args, **kwargs)
                span.set_status(Status(StatusCode.OK))
                return result
            except Exception as e:
                span.set_status(Status(StatusCode.ERROR, str(e)))
                raise e
