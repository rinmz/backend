from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from users.api import router as users_router
from content.api import router as content_router
from django.conf import settings
from django.conf.urls.static import static

api = NinjaAPI()
api.add_router("/users/", users_router)
api.add_router("/content/", content_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]

# Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)