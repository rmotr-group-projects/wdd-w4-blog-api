from rest_framework import serializers

from blog.models import Author, Entry, Blog


# implement all Serializers here
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'url',
            'name',
            'tagline'
        )


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = (
            'url',
            'name',
            'email',
            'nationality'
        )


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = (
            'url',
            'headline',
            'body_text',
            'pub_date',
            'mod_date',
            'number_comments',
            'scoring',
            'blog',
            'authors'
        )
