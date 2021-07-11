from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('apps.user.urls'), name='user'),
    path('api/recipe/', include('apps.recipe.urls'), name='recipe'),
]
