from locust import HttpUser, task, between


class DemoUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def load_api(self):
        self.client.get("/api/data")
