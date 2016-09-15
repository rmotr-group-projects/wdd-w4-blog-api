from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from blog.views import AuthorViewSet, EntryViewSet, BlogViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'authors', AuthorViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
