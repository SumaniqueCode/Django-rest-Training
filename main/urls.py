"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from users.router import router as user_router
from django.conf import settings
from django.conf.urls.static import static
from projects.router import router as project_router
from tasks.router import router as task_router

auth_api_urls=[]

if settings.DEBUG:
    auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))

api_urlpatterns = [
    path("users/", include(user_router.urls)),
    path("projects/", include(project_router.urls)),
    path("tasks/", include(task_router.urls)),
]
urlpatterns = [
    path("api/", include(api_urlpatterns)),
    path("admin/", admin.site.urls),
]+auth_api_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
