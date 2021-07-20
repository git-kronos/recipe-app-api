from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('apps.user.urls'), name='user'),
    path('api/recipe/', include('apps.recipe.urls'), name='recipe'),
    path('docs/', include_docs_urls(title='Recipe App API')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
