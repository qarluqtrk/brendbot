from loader import db


def is_authenticated(tg_id) -> bool:
    user = db.get_user(tgid=tg_id)
    if user:
        return True
    else:
        return False
