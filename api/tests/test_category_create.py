import json

import pytest
from rest_framework.test import APITransactionTestCase

from api.models import Category
from authentication.helpers import generate_jwt_token
from authentication.models import User


class TestCategory(APITransactionTestCase):

    @classmethod
    @pytest.mark.django_db
    def setUp(cls):
        cls.user = User.objects.create_user(
            username='member',
            email='member@gmail.com',
            password='Mypassword',
        )

        cls.category1 = Category.objects.create(
            name='category1',
        )
        cls.category1.save()

    def test_create(self):
        self.jwt_token = generate_jwt_token(self.user.id)
        self.client.force_authenticate(user=self.user, token=self.jwt_token)

        data = json.dumps({"name": "category 1"})

        response = self.client.post(
            path='/api/categories/',
            data=data,
            content_type='application/json'
        )
        assert response.status_code == 201
        assert response.data['id'] is not None
        assert response.data['name'] == 'category 1'

        response = self.client.get(
            path='/api/categories/',
        )
        assert response.status_code == 200
        assert len(response.json()) == 2

