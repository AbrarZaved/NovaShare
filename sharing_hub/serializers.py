from rest_framework import serializers
from sharing_hub.models import Upload


class UploadSerializer(serializers.ModelSerializer):
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)

    class Meta:
        model = Upload
        fields = ["file", "slug", "created_at", "updated_at", "user_first_name"]
