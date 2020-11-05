import time
import random
import prometheus_client


# Start server to expose metrics (for Prometheus to scrape)
prometheus_client.start_http_server(8001)

# Metrics
feature = prometheus_client.Histogram(
    "model_feature", "Toy feature to track using Prometheus", ("env",)
).labels(env="prod")

# Deploy
while True:
    value = random.normalvariate(1, 1)
    feature.observe(value)  # observe feature
    print(f"Observed {value}")
    time.sleep(1)
