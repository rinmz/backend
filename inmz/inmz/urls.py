from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from users.api import router as users_router
from content.api import router as content_router

api = NinjaAPI()
api.add_router("/users/", users_router)
api.add_router("/content/", content_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]