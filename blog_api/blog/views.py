from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAdminUser

from blog.models import Author, Entry, Blog
from blog.serializers import *


class AuthorsView(mixins.CreateModelMixin, 
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = (IsAdminUser,)
    
class EntryView(mixins.CreateModelMixin, 
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class BlogView(mixins.CreateModelMixin, 
                  mixins.ListModelMixin,
                #   mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
