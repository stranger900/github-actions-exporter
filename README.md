# github-actions-exporter
github-actions-exporter

#### Steps to Build and Run
1. Build and Run the Docker Containers:

```
docker-compose up --build
```

2. Access Grafana:
Open your web browser and go to `http://localhost:3000`. Log in with the default credentials (`admin / admin`).

3. Add Prometheus Data Source in Grafana:

- Go to Grafana's settings.
- Add a new data source.
- Select Prometheus.
- Set the URL to http://prometheus:9090.
- Save and test the data source.

4. Create a Dashboard:

Create a new dashboard in Grafana.
Add panels to visualize the metrics from the GitHub Actions exporter.
