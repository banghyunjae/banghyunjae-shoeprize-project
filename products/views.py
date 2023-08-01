# from rest_framework import status
# from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Manufact, Currency, Product
from .serializers import ManufactSerializer, ProductSerializer, CurrencySerializer

"""
GenericView는 두가지 방법으로 사용할 수 있음

단일 APIView를 사용할 경우
ex) list, create, retrieve, update, destroy
믹스 APIView를 사용할 경우
ex) ListCreateAPIView, RetrieveUpdateDestroyAPIView

# APIView는 get, post, put, delete 등의 HTTP 메소드를 직접 사용할 수있고, 유연성이 좋지만 코드가 길어지고, 가독성이 좋지 않음.
# GenericView는 HTTP 메소드들을 미리 구현한 형태로 제공하고, 코드가 간결하고 가독성이 좋고, APIView에 비해 유연성이 떨어짐.
# ViewSet은 GenericView와 유사하지만, url을 직접 지정하지 않고, router를 사용하여 url을 자동으로 생성해주는 장점이 있음.

"""


class maunfact_list(generics.ListCreateAPIView):
    """
    제조사 목록 조회 및 생성
    """

    queryset = Manufact.objects.all()  # generic view는 queryset과 serializer_class를 필수로 가져야함
    serializer_class = ManufactSerializer


class maunfact_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    제조사 조회 및 존재하지 않는 제조사 조회시 자동으로 404를 띄움
    """

    queryset = Manufact.objects.all()
    serializer_class = ManufactSerializer
    lookup_field = (
        "id"  # 포스트맨을 활용하여 개별적인 id를 찾으려했지만 기본적으로 pk를 찾으려고함. 그래서 lookup_field를 설정해주어서 id를 받아옴
    )


class currency_list(generics.ListCreateAPIView):
    """
    가격 정보 목록 조회 및 생성
    """

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class currency_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    가격 정보 조회, 존재하지않는 가격 정보 조회시 자동으로 404를 띄움
    """

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    lookup_field = "id"


class product_list(generics.ListCreateAPIView):
    """
    제품 목록 조회 및 생성
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class product_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    제품 조회, 존재하지않는 제품 조회시 자동으로 404를 띄움
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = (
        "id"  # 포스트맨을 활용하여 개별적인 id를 찾으려했지만 기본적으로 pk를 찾으려고함. 그래서 lookup_field를 설정해주어서 id를 받아옴
    )


# -----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
APIView를 사용
"""
# class maunfact_list(APIView):
#     """
#     제조사 목록 조회 및 생성
#     """

#     def get(self, request):
#         manufact = Manufact.objects.all()
#         serializer = ManufactSerializer(manufact, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializers = ManufactSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# class maunfact_detail(APIView):
#     """
#     제조사 조회, 존재하지않는 제조사 조회시 404
#     """

#     def get_object(self, id):
#         try:
#             return Manufact.objects.get(id=id)
#         except Manufact.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         manufact = self.get_object(id)
#         serializer = ManufactSerializer(manufact)
#         return Response(serializer.data)


# class currency_list(APIView):
#     """
#     가격 정보 목록 조회 및 생성
#     """

#     def get(self, request):
#         currency = Currency.objects.all()
#         serializer = CurrencySerializer(currency, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializers = CurrencySerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# class product_list(APIView):
#     """
#     제품 목록 조회 및 생성
#     """

#     def get(self, request):
#         product = Product.objects.all()
#         serializer = ProductSerializer(product, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializers = ProductSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# class product_detail(APIView):
#     """
#     제품 조회, 존재하지않는 제품 조회시 404
#     """

#     def get_object(self, id):
#         try:
#             return Product.objects.get(id=id)
#         except Product.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         product = self.get_object(id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
