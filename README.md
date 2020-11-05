A demo project showing how to use Prometheus to monitor a machine learning system.

### Result

You should be able to view the `dev` and `prod` distributions on Grafana in real time.

<p align="center">
  <img src="https://media.giphy.com/media/P1ERIRmHUCySKJmLC1/giphy.gif">
</p>

### Configuring Grafana

PromQL query for `dev` distribution
```
model_feature_bucket{env="dev"}
```

PromQL query for `prod` distribution
```
model_feature_bucket{env="dev"}
```

Select `Heatmap` for both `Visualization` and `Format`, `legend` to `{{le}}` and `Data Format` to `Time series buckets`, like so:

<p align="center">
  <img src="https://media.giphy.com/media/aEtDSmnOoFNmXS1woy/giphy.gif">
</p>
