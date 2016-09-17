from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from blog.views import BlogViewSet, AuthorViewSet, EntryViewSet

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # configure API URLs here
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
