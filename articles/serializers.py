from rest_framework import serializers

from .models import Article, Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'article',
            'photo',
            'restaurant_name',
            'content',
            'restaurant_url',
        )
        model = Entry


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name)

    entry_set = EntrySerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'user',
            'photo',
            'title',
            'description',
            'entry_set',
        )
        model = Article
