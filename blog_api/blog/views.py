from rest_framework import viewsets, mixins, filters

from blog.models import Author
from blog.serializers import AuthorSerializer


class AuthorViewSet(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id',)
