from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from blog.views import AuthorViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
