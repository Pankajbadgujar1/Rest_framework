from rest_framework import serializers

from .models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields = ['name', 'age']

        #exclude = [' id',]
        # use any one of this above
          
        fields = '__all__'
        
    def validate(self, data):
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error', 'name cannot be numeric'})
                

        if data['age'] < 18:
            raise serializers.ValidationError({'error': 'age cannot be less than  18'})
        

        return data
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'