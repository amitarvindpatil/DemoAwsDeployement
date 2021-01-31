from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import StudentModel
from .serializers import StudentModelSerializers

class get_post_product(ListCreateAPIView):
    serializer_class = StudentModelSerializers

    def get_queryset(self):
        queryset = StudentModel.objects.all()
        return queryset

    # Get method of Product

    def get(self, request):
        get_data = self.get_queryset()
        serializer = StudentModelSerializers(get_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)