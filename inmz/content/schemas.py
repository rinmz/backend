from ninja import Schema

class ContentOut(Schema):
    id: int
    user: str
    content: str
    content_type: str
    created_at: str
