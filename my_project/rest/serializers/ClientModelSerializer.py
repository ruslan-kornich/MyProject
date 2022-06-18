from my_project.product.models import Client
from rest_framework import serializers





class ClientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'