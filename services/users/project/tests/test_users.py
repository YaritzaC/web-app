# services/users/project/tests/test_users.py

import os
import unittest

import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Pruebas para el servicio de usuarios."""

    def test_users(self):
        """Asegúrese de que la ruta /ping se comporte correctamente."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data['status'])
        self.assertIn('pong!', data['message'])


if __name__ == '__main__':
    unittest.main()
