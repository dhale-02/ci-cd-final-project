"""Unit tests for Account Service"""
import json
import unittest
from service import app


class TestAccountRoutes(unittest.TestCase):
    """Test cases for Account Service Routes"""

    def setUp(self):
        self.client = app.test_client()
        from service import routes
        routes.accounts = {}
        routes.next_id[0] = 1

    def test_index(self):
        """It should return the service name and version"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["name"], "Account REST API Service")
        self.assertEqual(data["version"], "1.0")

    def test_create_account(self):
        """It should create a new Account"""
        payload = {"name": "John Doe", "email": "john@example.com"}
        response = self.client.post(
            "/accounts",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["name"], "John Doe")

    def test_list_accounts(self):
        """It should list all Accounts"""
        payload = {"name": "Jane Doe", "email": "jane@example.com"}
        self.client.post(
            "/accounts",
            data=json.dumps(payload),
            content_type="application/json"
        )
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_read_account(self):
        """It should read an Account"""
        payload = {"name": "Alice", "email": "alice@example.com"}
        create_resp = self.client.post(
            "/accounts",
            data=json.dumps(payload),
            content_type="application/json"
        )
        account_id = json.loads(create_resp.data)["id"]
        response = self.client.get(f"/accounts/{account_id}")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["name"], "Alice")

    def test_update_account(self):
        """It should update an Account"""
        payload = {"name": "Bob", "email": "bob@example.com"}
        create_resp = self.client.post(
            "/accounts",
            data=json.dumps(payload),
            content_type="application/json"
        )
        account_id = json.loads(create_resp.data)["id"]
        update_payload = {"name": "Bob Updated", "email": "bob@example.com"}
        response = self.client.put(
            f"/accounts/{account_id}",
            data=json.dumps(update_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["name"], "Bob Updated")

    def test_delete_account(self):
        """It should delete an Account"""
        payload = {"name": "Charlie", "email": "charlie@example.com"}
        create_resp = self.client.post(
            "/accounts",
            data=json.dumps(payload),
            content_type="application/json"
        )
        account_id = json.loads(create_resp.data)["id"]
        response = self.client.delete(f"/accounts/{account_id}")
        self.assertEqual(response.status_code, 204)

    def test_security_headers(self):
        """It should return security headers"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("X-Content-Type-Options", response.headers)

    def test_cors_headers(self):
        """It should return a CORS header"""
        response = self.client.get(
            "/",
            headers={"Origin": "http://localhost:3000"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Access-Control-Allow-Origin", response.headers)


if __name__ == "__main__":
    unittest.main()
