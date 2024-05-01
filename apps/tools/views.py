from django.db.models import Q
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.catalog.models import Size, Color, Category, Catalog
from apps.catalog.serializer import GetCategorySerializer, GetColorSerializer, GetSizeSerializer, GetCatalogSerializer
from apps.content.models import News, Article
from apps.content.serializer import GetNewsSerializer
from apps.shopping.models import Application, Store
from apps.shopping.serializer import SearchStoreSerializer, ApplicationListSerializer
from apps.tools.models import ActionLog
from apps.tools.serializer import ActionLogListSerializer
from config.utils.pagination import APIPagination


class ActionLogListAPIView(ListAPIView):
    queryset = ActionLog.objects.order_by('-id').exclude(action__isnull=True)
    serializer_class = ActionLogListSerializer
    pagination_class = APIPagination


class GlobalSearchAPIView(APIView):
    @swagger_auto_schema(manual_parameters=[
        Parameter('search', IN_QUERY, description="Search", type=TYPE_STRING),
    ])
    def get(self, request, *args, **kwargs):
        search = request.query_params.get('search')
        if not search:
            return Response({
                'category': [],
                'color': [],
                'size': [],
            })
        category_results = Category.objects.filter(
            Q(name_uz__icontains=search) | Q(name_ru__icontains=search) | Q(name_en__icontains=search)
        )
        category_serializer = GetCategorySerializer(category_results, many=True)
        color_results = Color.objects.filter(
            Q(name_uz__icontains=search) | Q(name_ru__icontains=search) | Q(name_en__icontains=search)
        )
        color_serializer = GetColorSerializer(color_results, many=True)
        size_results = Size.objects.filter(
            Q(list_uz__icontains=search) | Q(list_ru__icontains=search) | Q(list_en__icontains=search) |
            Q(roll_uz__icontains=search) | Q(roll_ru__icontains=search) | Q(roll_en__icontains=search)
        )
        size_serializer = GetSizeSerializer(size_results, many=True)
        catalog_results = Catalog.objects.filter(
            Q(name_uz__icontains=search) | Q(description_uz__icontains=search) |
            Q(material_uz__icontains=search) | Q(shape_uz__icontains=search) |

            Q(name_ru__icontains=search) | Q(description_ru__icontains=search) |
            Q(material_ru__icontains=search) | Q(shape_ru__icontains=search) |

            Q(name_en__icontains=search) | Q(description_en__icontains=search) |
            Q(material_en__icontains=search) | Q(shape_en__icontains=search)
        )
        catalog_serializer = GetCatalogSerializer(catalog_results, many=True)

        news_results = News.objects.filter(
            Q(title_uz__icontains=search) | Q(title_ru__icontains=search) | Q(title_en__icontains=search) |
            Q(description_uz__icontains=search) | Q(description_ru__icontains=search) |
            Q(description_en__icontains=search)
        )
        news_serializer = GetNewsSerializer(news_results, many=True)
        article_results = Article.objects.filter(
            Q(name_uz__icontains=search) | Q(name_ru__icontains=search) | Q(name_en__icontains=search)
        )
        article_serializer = GetColorSerializer(article_results, many=True)

        store_results = Store.objects.filter(
            Q(title_uz__icontains=search) | Q(title_ru__icontains=search) | Q(title_en__icontains=search) |
            Q(address_uz__icontains=search) | Q(address_ru__icontains=search) | Q(address_en__icontains=search)
        )
        store_serializer = SearchStoreSerializer(store_results, many=True)
        application_results = Application.objects.filter(
            Q(fullname__icontains=search) | Q(phone_number__icontains=search) | Q(address__icontains=search)
        )
        application_serializer = ApplicationListSerializer(application_results, many=True)

        return Response({
            'category': category_serializer.data or [],
            'color': color_serializer.data or [],
            'size': size_serializer.data or [],
            'product': catalog_serializer.data or [],
            'news': news_serializer.data or [],
            'article': article_serializer.data or [],
            'store': store_serializer.data or [],
            'application': application_serializer.data or [],
        })
