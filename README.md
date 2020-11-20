A demo project showing how to use Prometheus to monitor a machine learning system.

## Result

You should be able to view the `dev` and `prod` distributions on Grafana in real time.

<p align="center">
  <img src="https://i.imgur.com/g7lDepn.png">
</p>

## Setup

### Demo
Run `python train.py` and `python deploy.py` in seperate terminals and leave them running.

### Prometheus

Follow the [Starting Prometheus ](https://prometheus.io/docs/prometheus/latest/getting_started/#starting-prometheus) guide, using the `prometheus.yml` in this repository as the config file when starting Prometheus locally.

### Grafana

Follow the [Install Grafana](https://grafana.com/docs/grafana/latest/installation/) guide to both install and start Grafana locally.

You can then add a Prometheus data source and create a panel. Create two panels with the following queries:

PromQL query for `dev` distribution
```
model_feature_bucket{env="dev"}
```

PromQL query for `prod` distribution
```
model_feature_bucket{env="prod"}
```

Select `Heatmap` for both `Visualization` and `Format`, `legend` to `{{le}}` and `Data Format` to `Time series buckets`, like so:

<p align="center">
  <img src="https://media.giphy.com/media/aEtDSmnOoFNmXS1woy/giphy.gif">
</p>

## Alerts for data drift

Grafana doesn't allow for alerts to be set on heatmaps.

One option for detecting data drift is to write an exporter, which takes the exported metrics (on ports `8000` and `8001` in the demo), augmenting them (with e.g. distance between `dev` and `prod` using the [KS test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)) and exposing them on another endpoint.

For more information on exporters, see [Prometheus - Writing Exporters](https://prometheus.io/docs/instrumenting/writing_exporters/).
