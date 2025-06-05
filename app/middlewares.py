# middlewares.py

from aiogram.types import Message
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from app.roles  import get_user_roles

from aiogram.types import Message
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable


class RoleMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        roles = get_user_roles(user_id)
        data["roles"] = roles  # Endi handlerlarga ro‘yxat sifatida beriladi
        return await handler(event, data)













# ADMINS = set()
# KADR = {1061444753}
# OTZ = {1061444753, 306794063}

# def get_user_role(user_id: int) -> str:
#     """
#     Get the role of a user based on their user ID.
#     """
#     if user_id in ADMINS:
#         return 'admin'
#     if user_id in KADR:
#         return 'kadr'
#     if user_id in OTZ:
#         return 'otz'
#     return 'user'


# class RoleMiddleware(BaseMiddleware):
#     async def __call__(
#         self,
#         handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
#         event: Message,
#         data: Dict[str, Any]
#     ) -> Any:
#         user_id = event.from_user.id
#         role = get_user_roles(user_id)
#         data["role"] = role  # Har bir handlerga "role" kalit so'zi yuboriladi
#         return await handler(event, data)
