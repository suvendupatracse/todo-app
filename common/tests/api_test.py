import pytest

from common.models import User
from common.factories import UserFactory


@pytest.mark.django_db
class TestUsers:
    def test_my_user(self):
        UserFactory(email="s@test.com", is_admin=True)
        me = User.objects.get(email="s@test.com")
        assert me.is_admin
