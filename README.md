# Load Testing Demo with Locust, Prometheus & Grafana

This project demonstrates how to set up a **load testing and monitoring stack** using:

- **FastAPI** → sample web app (our test subject)
- **Locust** → simulate user traffic
- **Locust Exporter** → expose metrics in Prometheus format
- **Prometheus** → collect & store metrics
- **Grafana** → visualize performance trends

---

## 📂 Project Structure

```
server/
├── app.py              # FastAPI sample app
├── locustfile.py       # Locust test definition (user behavior)
├── prometheus.yml      # Prometheus scrape config
├── docker-compose.yml  # Combined setup (exporter, Prometheus, Grafana)
├── poetry.lock         # Dependency lock file (Poetry)
├── pyproject.toml      # Python project dependencies
```

---

## 🛠 Prerequisites

- [Docker](https://docs.docker.com/get-docker/) + Docker Compose
- [Python 3.9+](https://www.python.org/downloads/) (if running app/Locust locally)
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

---

## ▶Getting Started

### 1. Move into the project folder

```bash
cd server
```

---

### 2. Run the FastAPI app

```bash
poetry install
poetry run uvicorn app:app --host 0.0.0.0 --port 8000
```

App available at → http://localhost:8000

---

### 3. Run Locust (load testing)

```bash
poetry run locust -f locustfile.py --host=http://localhost:8000
```

Locust UI → http://localhost:8089

---

### 4. Start Monitoring Stack (Exporter, Prometheus, Grafana)

```bash
docker compose up
```

Services available at:
- **Locust Exporter** → http://localhost:9646/metrics
- **Prometheus** → http://localhost:9090
- **Grafana** → http://localhost:3000

Default Grafana login:
```
username: admin
password: admin
```

---

## 📊 Visualizing Performance

In Grafana:
1. Add Prometheus datasource → `http://prometheus:9090`
2. Import or create dashboards with queries like:

- Requests per second:
  ```promql
  rate(locust_requests_total[1m])
  ```
- Avg response time:
  ```promql
  locust_response_time_seconds_avg
  ```
- 95th percentile latency:
  ```promql
  locust_response_time_seconds_percentile_95
  ```
- Failure rate:
  ```promql
  rate(locust_failures_total[5m])
  ```

---

##  What You’ll Learn

- How to simulate user traffic against a Python web app
- How to expose Locust metrics in Prometheus format
- How to scrape and visualize load test data over time
- How to spot performance bottlenecks before production

---

## 📜 License

MIT — feel free to fork and adapt.
