from django.db.models import Q
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.catalog.models import Size, Color, Category, Catalog
from apps.catalog.serializer import GetCategorySerializer, GetColorSerializer, GetSizeSerializer, GetCatalogSerializer
from apps.content.models import News, Article
from apps.content.serializer import GetNewsSerializer, GetArticleSerializer
from apps.shopping.models import Application, Store
from apps.shopping.serializer import SearchStoreSerializer, ApplicationListSerializer
from apps.tools.models import ActionLog
from apps.tools.serializer import ActionLogListSerializer, AdminSiteGlobalSearchResponseSerializer
from config.utils.pagination import APIPagination


class ActionLogListAPIView(ListAPIView):
    queryset = ActionLog.objects.order_by('-id').exclude(action__isnull=True)
    serializer_class = ActionLogListSerializer
    pagination_class = APIPagination


class AdminSiteGlobalSearchAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            Parameter('search', IN_QUERY, description="Search", type=TYPE_STRING),
        ],
        responses={status.HTTP_200_OK: AdminSiteGlobalSearchResponseSerializer}
    )
    def get(self, request, *args, **kwargs):
        search = request.query_params.get('search')
        if not search:
            return Response({
                'categories': [],
                'colors': [],
                'sizes': [],
                'products': [],
                'news': [],
                'articles': [],
                'stores': [],
                'applications': []
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
            Q(name__icontains=search)
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
        article_serializer = GetArticleSerializer(article_results, many=True)

        store_results = Store.objects.filter(
            Q(name_uz__icontains=search) | Q(name_ru__icontains=search) | Q(name_en__icontains=search) |
            Q(address_uz__icontains=search) | Q(address_ru__icontains=search) | Q(address_en__icontains=search)
        )
        store_serializer = SearchStoreSerializer(store_results, many=True)
        application_results = Application.objects.filter(
            Q(fullname__icontains=search) | Q(phone_number__icontains=search) | Q(address__icontains=search)
        )
        application_serializer = ApplicationListSerializer(application_results, many=True)

        return Response({
            'categories': category_serializer.data or [],
            'colors': color_serializer.data or [],
            'sizes': size_serializer.data or [],
            'products': catalog_serializer.data or [],
            'news': news_serializer.data or [],
            'articles': article_serializer.data or [],
            'stores': store_serializer.data or [],
            'applications': application_serializer.data or [],
        })


class UserSiteGlobalSearchAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            Parameter('search', IN_QUERY, description="Search", type=TYPE_STRING),
        ],
        responses={status.HTTP_200_OK: AdminSiteGlobalSearchResponseSerializer}
    )
    def get(self, request, *args, **kwargs):
        search = request.query_params.get('search')
        if not search:
            return Response({
                'catalogs': [],
                'news': [],
                'articles': [],
                'stores': []
            })
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
            Q(name_uz__icontains=search) | Q(name_ru__icontains=search) | Q(name_en__icontains=search) |
            Q(address_uz__icontains=search) | Q(address_ru__icontains=search) | Q(address_en__icontains=search)
        )
        store_serializer = SearchStoreSerializer(store_results, many=True)

        return Response({
            'catalogs': catalog_serializer.data or [],
            'news': news_serializer.data or [],
            'articles': article_serializer.data or [],
            'stores': store_serializer.data or []
        })
