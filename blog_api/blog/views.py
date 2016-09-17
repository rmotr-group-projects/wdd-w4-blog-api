from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAdminUser

from blog.models import Author, Entry, Blog
from blog.serializers import *


class AuthorsView(mixins.CreateModelMixin, 
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Author.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    serializer_class = AuthorSerializer
    search_fields = ('name', 'email', 'nationality')
    ordering_fields = ('name', 'email', 'nationality', 'id')
    
class EntryView(mixins.CreateModelMixin, 
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class BlogView(mixins.CreateModelMixin, 
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
