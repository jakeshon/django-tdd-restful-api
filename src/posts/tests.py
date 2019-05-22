from django.test import TestCase

# Create your tests here.
# 테스트
class TestPosts(TestCase):

    def test_smoke_test(self):
        assert 1 is not 1, "당연히 같아야 해요."
