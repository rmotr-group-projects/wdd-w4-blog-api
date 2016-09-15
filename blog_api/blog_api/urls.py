from django.conf.urls import url, include
from django.contrib import admin

# you will probably need to import DRF routers

from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # configure API URLs here
]
