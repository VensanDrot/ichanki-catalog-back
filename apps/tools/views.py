import locale
from collections import defaultdict
from datetime import datetime, timedelta

from django.conf import settings
from django.db.models import Q
from django.utils.timezone import localdate
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.catalog.models import Size, Color, Category, Catalog
from apps.catalog.serializer import GetCategorySerializer, GetColorSerializer, GetSizeSerializer, GetCatalogSerializer
from apps.content.models import News, Article
from apps.content.serializer import GetNewsSerializer, GetArticleSerializer
from apps.shopping.models import Application, Store
from apps.shopping.serializer import SearchStoreSerializer, ApplicationListSerializer
from apps.tools.models import ActionLog, Region
from apps.tools.serializer import ActionLogListSerializer, AdminSiteGlobalSearchResponseSerializer, \
    UserSiteGlobalSearchResponseSerializer, UserSiteGlobalSearchCountResponseSerializer, RegionListSerializer
from config.utils.api_exceptions import APIValidation
from config.utils.pagination import APIPagination


class ActionLogListAPIView(ListAPIView):
    queryset = ActionLog.objects.order_by('-id').exclude(action__isnull=True)
    serializer_class = ActionLogListSerializer
    pagination_class = APIPagination


class AdminSiteGlobalSearchAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            Parameter('search', IN_QUERY, description="Search", type=TYPE_STRING),
            Parameter('page', IN_QUERY, description="Search", type=TYPE_STRING),
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


class UserSiteGlobalSearchAPIView(APIView, APIPagination):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(
        manual_parameters=[
            Parameter('search', IN_QUERY, description="Search", type=TYPE_STRING),
        ],
        responses={status.HTTP_200_OK: UserSiteGlobalSearchResponseSerializer}
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
        catalog_page = self.paginate_queryset(catalog_results, request)
        if catalog_page is not None:
            catalog_serializer = GetCatalogSerializer(catalog_page, many=True)
        else:
            catalog_serializer = GetCatalogSerializer(catalog_results, many=True)
        catalog_data = self.get_paginated_response(catalog_serializer.data)

        news_results = News.objects.filter(
            Q(title_uz__icontains=search) | Q(title_ru__icontains=search) | Q(title_en__icontains=search) |
            Q(description_uz__icontains=search) | Q(description_ru__icontains=search) |
            Q(description_en__icontains=search)
        )
        news_page = self.paginate_queryset(news_results, request)
        if news_page is not None:
            news_serializer = GetNewsSerializer(news_page, many=True)
        else:
            news_serializer = GetNewsSerializer(news_results, many=True)
        news_data = self.get_paginated_response(news_serializer.data)

        article_results = Article.objects.filter(
            Q(name_uz__icontains=search) | Q(name_ru__icontains=search) | Q(name_en__icontains=search)
        )
        article_page = self.paginate_queryset(article_results, request)
        if article_page is not None:
            article_serializer = GetColorSerializer(article_page, many=True)
        else:
            article_serializer = GetColorSerializer(article_results, many=True)
        article_data = self.get_paginated_response(article_serializer.data)

        store_results = Store.objects.filter(
            Q(name_uz__icontains=search) | Q(name_ru__icontains=search) | Q(name_en__icontains=search) |
            Q(address_uz__icontains=search) | Q(address_ru__icontains=search) | Q(address_en__icontains=search)
        )
        store_page = self.paginate_queryset(store_results, request)
        if store_page is not None:
            store_serializer = SearchStoreSerializer(store_page, many=True)
        else:
            store_serializer = SearchStoreSerializer(store_results, many=True)
        store_data = self.get_paginated_response(store_serializer.data)

        return Response({
            'catalogs': catalog_data.data,
            'news': news_data.data,
            'articles': article_data.data,
            'stores': store_data.data
            # 'catalogs': catalog_serializer.data or [],
            # 'news': news_serializer.data or [],
            # 'articles': article_serializer.data or [],
            # 'stores': store_serializer.data or []
        })


class UserSiteGlobalSearchCountsAPIView(APIView, APIPagination):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(
        manual_parameters=[
            Parameter('search', IN_QUERY, description="Search", type=TYPE_STRING),
        ],
        responses={status.HTTP_200_OK: UserSiteGlobalSearchCountResponseSerializer}
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
        news_results = News.objects.filter(
            Q(title_uz__icontains=search) | Q(title_ru__icontains=search) | Q(title_en__icontains=search) |
            Q(description_uz__icontains=search) | Q(description_ru__icontains=search) |
            Q(description_en__icontains=search)
        )
        article_results = Article.objects.filter(
            Q(name_uz__icontains=search) | Q(name_ru__icontains=search) | Q(name_en__icontains=search)
        )

        return Response({
            'catalogs': catalog_results.count(),
            'news': news_results.count(),
            'articles': article_results.count(),
            # 'catalogs': catalog_serializer.data or [],
            # 'news': news_serializer.data or [],
            # 'articles': article_serializer.data or [],
            # 'stores': store_serializer.data or []
        })


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer
    permission_classes = [AllowAny, ]


class DashboardAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            Parameter('from', IN_QUERY, description="FROM date filter", type=TYPE_STRING),
            Parameter('to', IN_QUERY, description="TO date filter", type=TYPE_STRING),
        ]
    )
    def get(self, request):
        from_date = request.query_params.get('from')
        to_date = request.query_params.get('to')
        if not (from_date and to_date):
            raise APIValidation('from and to params required!', status_code=status.HTTP_400_BAD_REQUEST)
        start_date = datetime.strptime(from_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(to_date, '%Y-%m-%d').date()

        applications = (Application.objects
                        .select_related('author', 'store', 'region', )
                        .prefetch_related('ordered_product')
                        .filter(created_at__date__gte=from_date, created_at__date__lte=to_date))

        date_applications = defaultdict(int)
        for app in applications:
            local_date = localdate(app.created_at)
            date_applications[local_date] += 1
        all_dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
        for date in all_dates:
            if date not in date_applications:
                date_applications[date] = 0
        sorted_dates = sorted(date_applications.keys())
        locale.setlocale(locale.LC_TIME, settings.SET_LOCAL_LANGUAGE)
        labels = [date.strftime('%b-%d').capitalize() for date in sorted_dates]
        line1 = [date_applications[date] for date in sorted_dates]
        chart = {
            'line1': line1,
            'labels': labels
        }
        return Response(chart)
