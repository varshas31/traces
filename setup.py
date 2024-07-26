from setuptools import setup, find_packages

setup(
    name='my_tracer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'opentelemetry-api',
        'opentelemetry-sdk',
        'opentelemetry-exporter-otlp',
    ],
    description='A simple OpenTelemetry tracing package',
)
