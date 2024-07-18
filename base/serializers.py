from rest_framework.serializers import ModelSerializer
from base.models import Notes, Profile
from django.contrib.auth.models import User

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data.pop('is_superuser', None)
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance