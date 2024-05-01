from rest_framework import serializers

from api.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['author', 'body', 'created_on', 'post']
        read_only_fields = ['post']

        def create(self, validated_data):
            # Make the field not required for updates
            self.fields['post'].required = True
            return super(validated_data).create()

