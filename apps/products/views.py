"""Views"""
from django.shortcuts import get_object_or_404
from django.db.models.query_utils import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import *
from .models import *
from .pagination import MediumSetPagination


# Category
class CategoryListView(APIView):

    def get(self, request, format=None):
        if Category.objects.all().exists():
            categories = Category.objects.all()

            paginator = MediumSetPagination()
            results = paginator.paginate_queryset(categories, request)

            serializer = CategorySerializer(results, many=True)

            return paginator.get_paginated_response({'categories': serializer.data})

        return Response({'message': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):

    def get(self, request, category_id, format=None):
        category = get_object_or_404(Category, id=category_id)
        serializer = CategorySerializer(category)

        return Response({'category': serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, category_id, format=None):
        category = get_object_or_404(Category, id=category_id)
        serializer = CategorySerializer(
            category, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'category updated': serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Product
class CategoryProductListView(APIView):

    def get(self, request, category_id, format=None):
        if Product.objects.all().exists():
            category = Category.objects.get(id=category_id)
            products = Product.objects.order_by(
                'name').filter(category=category)

            paginator = MediumSetPagination()
            results = paginator.paginate_queryset(products, request)

            serializer = ProductSerializer(results, many=True)

            return paginator.get_paginated_response({'products': serializer.data})

        return Response({'message': 'No products found for this category'}, status=status.HTTP_404_NOT_FOUND)


class ProductListView(APIView):

    def get(self, request, format=None):
        if Product.objects.all().exists():
            products = Product.objects.order_by('name')

            paginator = MediumSetPagination()
            results = paginator.paginate_queryset(products, request)

            serializer = ProductSerializer(results, many=True)

            return paginator.get_paginated_response({'products': serializer.data})

        return Response({'message': 'No products registered yet'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):

    def get(self, request, product_slug, format=None):
        product = get_object_or_404(Product, slug=product_slug)
        serializer = ProductSerializer(product)

        return Response({'product': serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, product_slug, format=None):
        product = get_object_or_404(Product, slug=product_slug)
        serializer = ProductSerializer(
            product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'product updated': serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchProductView(APIView):
    def get(self, request, search_term):
        matches = Product.objects.filter(
            Q(name__icontains=search_term) |
            Q(category__name__icontains=search_term)
        )

        paginator = MediumSetPagination()
        results = paginator.paginate_queryset(matches, request)

        serializer = ProductSerializer(results, many=True)

        return Response({'filtered products': serializer.data}, status=status.HTTP_200_OK)
