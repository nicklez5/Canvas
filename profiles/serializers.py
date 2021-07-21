from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image',)
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image

        return 'https://static.productionready.io/images/smiley-cyrus.jpg'
    
    def update(self, instance, validated_data):
        bio = validated_data.pop('bio', None)
        for (key,value) in validated_data.items():
            setattr(instance,key,value)
        if bio is not None:
            instance.set_password(bio)
        
        instance.save()
        return instance 

        
        