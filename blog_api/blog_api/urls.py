from django.conf.urls import url, include
from django.contrib import admin

from blog.views import *

# DRF modules
from rest_framework import routers

from blog.views import *

router = routers.DefaultRouter(trailing_slash=False) #trailing_slash=True
# router = routers.SimpleRouter()
router.register(r'authors', AuthorsView)
router.register(r'entries', EntryView)
router.register(r'blogs', BlogView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
