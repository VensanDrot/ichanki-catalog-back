from datetime import datetime

from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.shopping.filters import ApplicationFilter
from apps.shopping.models import Store, Application, ACCEPTED
from apps.shopping.serializer import GetStoreSerializer, PostStoreSerializer, GiveApplicationSerializer, \
    ApplicationListSerializer, StoreMultiLangListSerializer
from config.utils.pagination import APIPagination
from config.utils.permissions import LandingPage
from config.views import ModelViewSetPack


class StoreModelViewSet(ModelViewSetPack):
    queryset = Store.objects.all()
    serializer_class = GetStoreSerializer
    post_serializer_class = PostStoreSerializer
    permission_classes = (LandingPage,)
    http_method_names = ['patch', 'post', 'get', 'delete']

    @swagger_auto_schema(request_body=PostStoreSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostStoreSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class StoreMultiLangListAPIView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreMultiLangListSerializer


class StoreListAPIView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = GetStoreSerializer
    permission_classes = [AllowAny, ]


class GiveApplicationAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = GiveApplicationSerializer
    permission_classes = [AllowAny, ]


class ApplicationListAPIView(ListAPIView):
    queryset = Application.objects.all().order_by('-created_at')
    serializer_class = ApplicationListSerializer
    pagination_class = APIPagination
    filterset_class = ApplicationFilter

    @swagger_auto_schema(
        operation_description="Upload file",
        manual_parameters=[
            openapi.Parameter(
                'from', in_=openapi.IN_QUERY,
                type=openapi.FORMAT_DATE,
                format='date',
                required=False,
                description=_('Choose a start filter range')
            ),
            openapi.Parameter(
                'to', in_=openapi.IN_QUERY,
                type=openapi.FORMAT_DATE,
                format='date',
                required=False,
                description=_('Choose end of filter range')
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        from_date = self.request.query_params.get('from')
        to_date = self.request.query_params.get('to')

        if from_date:
            from_date = datetime.strptime(from_date, '%Y-%m-%d')
            from_date = timezone.make_aware(from_date, timezone.get_current_timezone())
            queryset = queryset.filter(created_at__gte=from_date)

        if to_date:
            to_date = datetime.strptime(to_date, '%Y-%m-%d')
            to_date = timezone.make_aware(to_date, timezone.get_current_timezone())
            queryset = queryset.filter(created_at__lte=to_date)

        return queryset


class AcceptApplicationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        application_id = kwargs['application_id']
        instance = get_object_or_404(Application, pk=application_id)
        instance.status = ACCEPTED
        instance.save()
        return Response({
            'detail': 'Application accepted',
            'id': application_id
        }, status=status.HTTP_200_OK)
