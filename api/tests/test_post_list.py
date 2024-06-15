import json

import pytest
from rest_framework.test import APITransactionTestCase

from api.models import Category, Post
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

        cls.post1 = Post.objects.create(
            title='post',
            body='hey you',
            category_id=cls.category1.id
        )
        cls.post1.save()

        cls.post2 = Post.objects.create(
            title='post2',
            body='hey you2',
            category_id=cls.category1.id
        )
        cls.post2.save()

    def test_list(self):
        self.jwt_token = generate_jwt_token(self.user.id)
        self.client.force_authenticate(user=self.user, token=self.jwt_token)

        response = self.client.get(
            path=f'/api/categories/{self.category1.id}/posts/',
        )
        assert response.status_code == 200
        assert len(response.json()) == 2

