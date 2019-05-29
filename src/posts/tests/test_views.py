from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
# 테스트
class PostsBaseTest(TestCase):

    def test_create_user_mode(self):
        User.objects.create_user(
                    username='Hello_World'
                )

        assert User.objects.count() == 1, "Shoud be equal"
