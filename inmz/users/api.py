from ninja import Router, Schema
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

router = Router()
User = get_user_model()

class RegisterSchema(Schema):
    username: str
    password: str
    email: str

@router.post("/register")
def register(request, payload: RegisterSchema):
    if User.objects.filter(username=payload.username).exists():
        return {"error": "this username is already taken"}
    user = User.objects.create_user(
        username=payload.username,
        email=payload.email,
        password=payload.password
    )
    return {"id": user.id, "username": user.username}
