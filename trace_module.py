from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.trace import Status, StatusCode

class SimpleTracer:
    def __init__(self, service_name):
        resource = Resource(attributes={
            SERVICE_NAME: service_name
        })
        provider = TracerProvider(resource=resource)
        trace.set_tracer_provider(provider)
        span_processor = BatchSpanProcessor(ConsoleSpanExporter())
        trace.get_tracer_provider().add_span_processor(span_processor)
        self.tracer = trace.get_tracer(service_name)

    def log(self, span_name, func, *args, **kwargs):
        with self.tracer.start_as_current_span(span_name) as span:
            try:
                result = func(*args, **kwargs)
                span.set_status(Status(StatusCode.OK))
                return result
            except Exception as e:
                span.set_status(Status(StatusCode.ERROR, str(e)))
                raise e

# Usage example:
# tracer = SimpleTracer("example-service")
# tracer.log("span-name", some_function, arg1, arg2, kwarg1=value1)
