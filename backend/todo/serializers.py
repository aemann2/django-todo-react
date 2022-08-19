from pyexpat import model
from rest_framework import serializers
from .models import Todo

# serializer will convert our model instance to JSON so that the frontend can work with the received data
class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')