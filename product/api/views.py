# api/views.py
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from ..models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(status=True)  # Only show active products
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        # Soft delete: set status to False instead of deleting
        instance.status = False
        instance.save()

@api_view(['GET', 'POST'])
def product_list_create(request):
    if request.method == 'GET':
        products = Product.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class ProductUpdateView(APIView):
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.status = False
        product.save()
        return Response({'message': 'Product marked as deleted.'}, status=204)