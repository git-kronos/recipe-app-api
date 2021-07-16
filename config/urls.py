from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('apps.user.urls'), name='user'),
    path('api/recipe/', include('apps.recipe.urls'), name='recipe'),
] + static(settings.MEDIA_URL, doucument_root=settings.MEDIA_ROOT)
