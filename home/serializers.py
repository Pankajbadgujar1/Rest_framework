from rest_framework import serializers

from .models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields = ['name', 'age']

        #exclude = [' id',]
        # use any one of this above
          
        fields = '__all__'
        