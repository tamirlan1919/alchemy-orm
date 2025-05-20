from models import Address, User, Profile
from database import session

def create_user(name: str, email: str):
    new_user = User(name=name, email=email)
    session.add(new_user)
    session.commit()
    session.close()
    print(f"User {name} created with email {email} ✅")
    return new_user

