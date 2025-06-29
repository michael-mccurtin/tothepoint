from dataclasses import dataclass
from typing import List
from uuid import UUID

@dataclass
class User:
    id: UUID
    email: str
    interests: List[str]
    signup_date: str
    unsubscribed: bool
    email_frequency: str
