class TestHome:
    URL = "/"

    def test_get_page(self, home_test_client):
        resp = home_test_client.get(self.URL)
        assert resp.status_code == 200