import pytest
from unittest.mock import MagicMock
from EDITTHIS.src.services.user_service import UserService
from EDITTHIS.src.database.models import User

@pytest.fixture
def user_service():
    return UserService()

@pytest.fixture
def mock_user():
    user = MagicMock(User)
    user.tg_id = 12345
    user.all.return_value = [user]
    return user

def test_add_user(user_service, mock_user):
    user_service.add_user(mock_user)
    assert len(user_service._users_list) == 1

@pytest.mark.asyncio
async def test_get_user(user_service, mock_user):
    user_service.add_user(mock_user)
    user = await user_service.get_user(12345)
    assert user.tg_id == 12345

@pytest.mark.asyncio
async def test_remove_user(user_service, mock_user):
    start_len = len(user_service._users_list)
    user_service.add_user(mock_user)
    await user_service.remove_user(mock_user)
    assert len(user_service._users_list) - start_len == 0
