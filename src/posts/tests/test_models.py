from django.contrib.auth.models import User

import pytest
from mixer.backend.django import mixer

from .base import PostsBaseTest

# Create your tests here.
# 테스트

pytestmark = pytest.mark.django_db

class PostsModelTest(PostsBaseTest):
    

    def test_create_user_mode(self):
        User.objects.create_user(
                    username='Hello_World'
                )
        
        assert User.objects.count() == 1, "Shoud be equal"

    def test_create_superuser_via_mixer(self):
        superuserobj = mixer.blend('auth.User',is_staff=True,is_superuser=True)
        assert User.objects.count() == 1, "Sould be equal"
        assert superuserobj.is_superuser == True, "Shoud be superuser"

    def  test_create_user_via_mixer(self):

        for cnt in range(50):
            obj = mixer.blend('auth.User')
        assert User.objects.count() == 50, "Should be equal"
