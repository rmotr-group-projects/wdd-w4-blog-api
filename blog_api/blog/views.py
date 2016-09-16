from rest_framework import viewsets, mixins, filters

from blog.models import Author, Entry, Blog
from blog.serializers import *


# implement Views here
class EntryViewSet(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    '''
    A viewset that provides ___ actions for the Entry model
    '''
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class BlogViewSet(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    '''
    A viewset that provides ___ actions for the Blog model
    '''
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class AuthorViewSet(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    '''
    A viewset that provides ___ actions for the Author model
    '''
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id',)