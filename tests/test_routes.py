"""Unit tests for counter routes"""
import unittest
from service.routes import app


class TestCounterRoutes(unittest.TestCase):
    """Test cases for Counter Routes"""

    def setUp(self):
        self.client = app.test_client()
        # Clear counters before each test
        from service import routes
        routes.counters = {}

    def test_index(self):
        """Test index route"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_create_counter(self):
        """Test creating a counter"""
        response = self.client.post("/counters/test")
        self.assertEqual(response.status_code, 201)

    def test_read_counter(self):
        """Test reading a counter"""
        self.client.post("/counters/test")
        response = self.client.get("/counters/test")
        self.assertEqual(response.status_code, 200)

    def test_update_counter(self):
        """Test updating a counter"""
        self.client.post("/counters/test")
        response = self.client.put("/counters/test")
        self.assertEqual(response.status_code, 200)

    def test_delete_counter(self):
        """Test deleting a counter"""
        self.client.post("/counters/test")
        response = self.client.delete("/counters/test")
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
