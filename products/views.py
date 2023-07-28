from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Manufact, Product
from .serializers import ManufactSerializer, ProductSerializer


class maunfact_list(APIView):
    """
    제조사 목록 조회 및 생성
    """

    def get(self, request):
        manufact = Manufact.objects.all()
        serializer = ManufactSerializer(manufact, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializers = ManufactSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class maunfact_detail(APIView):
    """
    제조사 조회, 존재하지않는 제조사 조회시 404
    """

    def get_object(self, id):
        try:
            return Manufact.objects.get(id=id)
        except Manufact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        manufact = self.get_object(id)
        serializer = ManufactSerializer(manufact)
        return Response(serializer.data)


class product_list(APIView):
    """
    제품 목록 조회 및 생성
    """

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class product_detail(APIView):
    """
    제품 조회, 존재하지않는 제품 조회시 404
    """

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
