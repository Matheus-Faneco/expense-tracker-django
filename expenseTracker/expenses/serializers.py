from rest_framework import serializers
from .models import Expense

#Serializando campos de despesa
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'