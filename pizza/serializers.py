from rest_framework import serializers
from .models import Pizza,Pizza_size,Pizza_topping

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Pizza
        fields = ['id','pizza_type','pizza_size','pizza_toppings']
        depth = 1

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza_topping
        fields = ['topping']

class PizzaSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza_size
        fields = ['pizza_size']