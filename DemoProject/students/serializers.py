from rest_framework import serializers
from .models import StudentModel


class StudentModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ('id', 'Name', 'age')