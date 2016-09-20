from django.conf.urls import url, include
from django.contrib import admin

# you will probably need to import DRF routers
from rest_framework import routers

from blog.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'entries', EntryViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # configure API URLs here
    url(r'^api/', include(router.urls))
]
