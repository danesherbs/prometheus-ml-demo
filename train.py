import time
import random
import prometheus_client


# Start server to expose metrics (for Prometheus to scrape)
prometheus_client.start_http_server(8000)

# Metrics
feature = prometheus_client.Histogram(
    "model_feature", "Toy feature to track using Prometheus", ("env",)
).labels(env="dev")

# Train
while True:
    value = random.normalvariate(5, 2)
    feature.observe(value)  # observe feature
    print(f"Observed {value}")
    time.sleep(1)
