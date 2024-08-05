from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.trace import Status, StatusCode
<<<<<<< HEAD
from opentelemetry.exporter.jaeger.thrift import JaegerExporter


class SimpleTracer:
    def __init__(self, service_name, jaeger_host='localhost', jaeger_port=6831):
=======

class SimpleTracer:
    def __init__(self, service_name):
>>>>>>> b393116dab536a45c257b83acfd4bc8e139064b9
        resource = Resource(attributes={
            SERVICE_NAME: service_name
        })
        provider = TracerProvider(resource=resource)
<<<<<<< HEAD

        # Set the tracer provider
        trace.set_tracer_provider(provider)

        # Set up the Jaeger exporter
        jaeger_exporter = JaegerExporter(
            agent_host_name=jaeger_host,
            agent_port=jaeger_port,
        )
        span_processor = BatchSpanProcessor(jaeger_exporter)
        provider.add_span_processor(span_processor)

        # Also log to console
        console_exporter = ConsoleSpanExporter()
        console_span_processor = BatchSpanProcessor(console_exporter)
        provider.add_span_processor(console_span_processor)

=======
        trace.set_tracer_provider(provider)
        span_processor = BatchSpanProcessor(ConsoleSpanExporter())
        trace.get_tracer_provider().add_span_processor(span_processor)
>>>>>>> b393116dab536a45c257b83acfd4bc8e139064b9
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
<<<<<<< HEAD
# tracer = SimpleTracer("example-service", jaeger_host="localhost", jaeger_port=6831)
=======
# tracer = SimpleTracer("example-service")
>>>>>>> b393116dab536a45c257b83acfd4bc8e139064b9
# tracer.log("span-name", some_function, arg1, arg2, kwarg1=value1)
