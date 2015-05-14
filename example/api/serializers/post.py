from rest_framework_3 import serializers


class PostSerializer(serializers.Serializer):
    """
    Blog post serializer
    """
    title = serializers.CharField(max_length=50)

