from rest_framework import serializers

from api.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['category']
        depth = 2

        def create(self, validated_data):
            # Make the field not required for updates
            self.fields['category'].required = True
            return super(validated_data).create()

