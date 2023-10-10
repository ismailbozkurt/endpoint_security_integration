from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.integration import IntegrationService
from core.base_product import BaseProduct
from utils.products import get_products
from .serializers import ProductSerializer
from utils.services import (
    validate_fields,
    set_keys,
    remove_keys
)


class ProductAPIView(APIView):
    serializer_class = ProductSerializer

    def get(self, request):
        data = get_products()
        return Response(data, status=status.HTTP_200_OK)


class IntegrationAPIView(APIView):
    serializer_class = ProductSerializer

    def post(self, request, product):
        data = request.data
        if validate_fields(product, data):
            product: BaseProduct = IntegrationService.get_service(product)
            if product.integrate(keys=data):
                product_obj = set_keys(product, data)
                serializer = ProductSerializer(product_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"error": "invalid schema"}, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, product):
    #     data = request.data
    #     return Response()

    # def put(self, request, product):
    #     return Response()

    def delete(self, request, product):
        if remove_keys(product):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
