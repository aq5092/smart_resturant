# middlewares.py

from aiogram.types import Message
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from app.roles  import get_user_role

class RoleMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        role = get_user_role(user_id)
        data["role"] = role  # Har bir handlerga "role" kalit so'zi yuboriladi
        return await handler(event, data)
