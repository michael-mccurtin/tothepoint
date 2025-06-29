from uuid import UUID
from app.user_store import UserStore

def test_user_lookup_by_id():
    store = UserStore("data/users.json")
    uid = UUID("d77e3d4e-1d2f-4b5f-84b9-927ea89cf96b")
    user = store.get_user_by_id(uid)
    assert user is not None
    assert user.email == "grace@turing.io"

def test_user_email_and_interests():
    store = UserStore("data/users.json")
    uid = UUID("d77e3d4e-1d2f-4b5f-84b9-927ea89cf96b")
    assert store.get_user_email(uid) == "grace@turing.io"
    assert "ai" in store.get_user_interests(uid)
