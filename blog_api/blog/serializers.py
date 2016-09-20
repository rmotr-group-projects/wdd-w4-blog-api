from rest_framework import serializers

from blog.models import Author, Entry, Blog


# implement all Serializers here
class EntrySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Entry
        fields = '__all__'


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Blog
        fields = '__all__'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'