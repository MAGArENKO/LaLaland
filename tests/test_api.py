from fastapi.testclient import TestClient

from api.main import app


class TestHealthEndpoint:
    def test_health_check(self):
        with TestClient(app) as client:
            response = client.get("/health")
            assert response.status_code == 200
            data = response.json()
            assert data["status"] == "healthy"


class TestSearchEndpoint:
    def test_search_empty(self):
        with TestClient(app) as client:
            response = client.post("/search", json={"query": "test", "limit": 5})
            assert response.status_code == 200
            assert isinstance(response.json(), list)


class TestSourcesEndpoint:
    def test_get_sources(self):
        with TestClient(app) as client:
            response = client.get("/sources")
            assert response.status_code == 200
            data = response.json()
            assert "sources" in data


class TestRunsEndpoint:
    def test_get_runs(self):
        with TestClient(app) as client:
            response = client.get("/runs")
            assert response.status_code == 200
            assert isinstance(response.json(), list)


class TestStatsEndpoint:
    def test_get_stats(self):
        with TestClient(app) as client:
            response = client.get("/stats")
            assert response.status_code == 200
            data = response.json()
            assert "status" in data
            assert "vector_store" in data
