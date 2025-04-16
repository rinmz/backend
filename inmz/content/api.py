from ninja import Router, Schema
from .models import Content
from django.contrib.auth import get_user_model

router = Router()
User = get_user_model()

class ContentSchema(Schema):
    user_id: int
    content: str
    content_type: str

@router.post("/create")
def create_content(request, payload: ContentSchema):
    try:
        user = User.objects.get(id=payload.user_id)
    except User.DoesNotExist:
        return {"error": "user not found"}
    
    new_content = Content.objects.create(
        user=user,
        content=payload.content,
        content_type=payload.content_type
    )
    
    return {"id": new_content.id,
            "user": new_content.user.username,
            "content": new_content.content,
            "content_type": new_content.content_type,
            "created_at": new_content.created_at}


@router.get("{content_id}")
def get_content(request, content_id: int):
    try:
        content = Content.objects.get(id=content_id)
    except Content.DoesNotExist:
        return {"error": "content not found"}

    return {
         "id": content.id,
         "user": content.user.username,
         "content": content.content,
         "content_type": content.content_type,
         "created_at": content.created_at.isoformat() # isoformat() changes the datetime object to a string
    }