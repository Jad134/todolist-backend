from rest_framework import serializers
from .models import  TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'



class TodoItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['title', 'checked']  # Nur die Felder, die der Benutzer ausfüllen soll