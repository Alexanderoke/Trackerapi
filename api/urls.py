# from django.conf.urls import url
from api import views
# from .views import projectApi
from .views import RegisterAPI, LoginAPI, projectApi, SaveFile
from knox import views as knox_views
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^project/$',views.projectApi),
    re_path(r'^project/([0-9]+)$', views.projectApi),
    re_path('api/register/', RegisterAPI.as_view(), name='register'),
    re_path('api/login/', LoginAPI.as_view(), name='login'),
    re_path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    re_path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    re_path('SaveFile/', views.SaveFile)
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)