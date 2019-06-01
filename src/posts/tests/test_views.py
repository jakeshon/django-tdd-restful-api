from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from mixer.backend.django import mixer

from rest_framework import status
from .base import PostsBaseTest

# Create your tests here.
# 테스트

class PostsViewTest(PostsBaseTest):

    def test_send_get_request_via_user_viewset(self):

        # list  GET : POST
        # retrive / patch / destroy     GET : PUT : DELETE
        url = reverse('user-list')
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK

    def test_create_fake_data_tehn_send_get_request_via_user_viewset(self):

        #create 50 set

        for cnt in range(50):
            mixer.blend('auth.User', is_active=True)

        url = reverse('user-list')
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK

    def test_send_post_request_via_user_viewset(self):

        # list  GET : POST
        # retrive / patch / destroy     GET : PUT : DELETE
        url = reverse('user-list')
        data = {
                'username': 'HelloWorld',
                'password': 'test',
                'email': 'jakeshon@naver.com',
                'is_active': True,
        }
        response = self.client.post(url, data=data, format='json')

        assert response.status_code == status.HTTP_201_CREATED

    def test_send_retrive_update_destroy_request_via_user_viewset(self):
    
        # POST 를 이용해서 유저생성
        # list  GET : POST
        # retrive / patch / destroy     GET : PUT : DELETE
        url = reverse('user-list')
        data = {
                'username': 'HelloWorld',
                'password': 'test',
                'email': 'jakeshon@naver.com',
                'is_active': True,
        }
        response = self.client.post(url, data=data, format='json')

        assert response.status_code == status.HTTP_201_CREATED

        url = reverse('user-detail', args=[1])
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK

        url = reverse('user-detail', args=[1])
        data = {
                'is_active': False
        }
        response = self.client.patch(url, data=data, content_type='application/json')
        assert response.status_code == status.HTTP_200_OK

