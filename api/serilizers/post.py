from rest_framework import serializers

from api.models import Post, Category
from api.serilizers.category import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    category_pk = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='name',
        write_only=True,
    )
    print(category_pk)

    class Meta:
        model = Post
        fields = ['title', 'body', 'category_pk']
        depth = 10
        extra_kwargs = dict(
            category_pk=dict(required=True),
            title=dict(required=True),
            body=dict(required=True),
        )

