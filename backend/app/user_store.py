import json
from pathlib import Path
from uuid import UUID
from typing import List, Optional
from app.user import User

class UserStore:
    def __init__(self, path: str = "data/users.json"):
        self._path = Path(path)
        self._users = self._load_users()

    def _load_users(self) -> List[User]:
        with self._path.open() as f:
            raw_users = json.load(f)
            return [
                User(
                    id=UUID(u["id"]),
                    email=u["email"],
                    interests=u["interests"],
                    signup_date=u["signup_date"],
                    unsubscribed=u["unsubscribed"],
                    email_frequency=u["email_frequency"]
                )
                for u in raw_users
            ]

    def get_all_users(self) -> List[User]:
        return self._users

    def get_user_by_email(self, email: str) -> Optional[User]:
        return next((u for u in self._users if u.email == email), None)

    def get_user_by_id(self, user_id: UUID) -> Optional[User]:
            return next((u for u in self._users if u.id == user_id), None)

    def get_user_email(self, user_id: UUID) -> Optional[str]:
        user = self.get_user_by_id(user_id)
        return user.email if user else None

    def get_user_interests(self, user_id: UUID) -> Optional[List[str]]:
        user = self.get_user_by_id(user_id)
        return user.interests if user else None