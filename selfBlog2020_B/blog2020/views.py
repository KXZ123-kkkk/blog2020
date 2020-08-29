from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework import pagination
from . import serializers, models


class BlogView(ListAPIView, RetrieveAPIView, ModelViewSet):
    serializer_class = serializers.BlogModelSerializer
    queryset = models.Blog.objects.filter(is_delete=False).all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 0, 'message': 'ok', 'results': serializer.data})

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.blogReadPerson = 1 + instance.blogReadPerson
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class MyPageNumberPagination1(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'pageSize'
    max_page_size = 15

    page_query_param = 'page'


class LeaveMessagesView(ListAPIView, CreateAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['owner']
    serializer_class = serializers.LeaveMessageModelSerializer
    queryset = models.LeaveMessage.objects.filter(is_delete=False).all()

    pagination_class = MyPageNumberPagination1

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 0, 'message': 'ok', 'results': serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 0, 'message': 'ok'})


class ReplyMessagesView(ListAPIView, CreateAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['owner']
    serializer_class = serializers.ReplyMessageModelSerializer
    queryset = models.ReplyMessage.objects.filter(is_delete=False).all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 0, 'message': 'ok', 'results': serializer.data})

    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 0, 'message': 'ok'})


class MyPageNumberPagination2(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'pageSize'
    max_page_size = 15

    page_query_param = 'page'


class MusicView(ListAPIView, CreateAPIView):
    serializer_class = serializers.MusicModelSerializer
    queryset = models.Music.objects.filter(is_delete=False).all()

    pagination_class = MyPageNumberPagination2

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 0, 'message': 'ok', 'results': serializer.data})


class MyPageNumberPagination3(pagination.PageNumberPagination):
    page_size = 8
    page_size_query_param = 'pageSize'
    max_page_size = 8

    page_query_param = 'page'


class CartoonView(ModelViewSet, ListAPIView, RetrieveAPIView):
    serializer_class = serializers.CartoonModelSerializer
    queryset = models.Cartoon.objects.filter(is_delete=False).all()

    filter_backends = [SearchFilter]
    search_fields = ['kind']

    pagination_class = MyPageNumberPagination3

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 0, 'message': 'ok', 'results': serializer.data})


class WebReadPersonView(RetrieveAPIView):
    serializer_class = serializers.WebReadPersonModelSerializer
    queryset = models.Recording.objects.filter(is_delete=False).all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.websiteReadPerson = 1 + instance.websiteReadPerson
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
