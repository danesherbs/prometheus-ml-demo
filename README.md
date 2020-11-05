A demo project showing how to use Prometheus to monitor a machine learning system

### Grafana

PromQL query for `dev` distribution
```
model_feature_bucket{env="dev"}
```

PromQL query for `prod` distribution
```
model_feature_bucket{env="dev"}
```

Select `Heatmap` for both `Visualization` and `Format` to plot the distribution over time.
