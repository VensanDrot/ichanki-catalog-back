from django.urls import path

from apps.tools.views import ActionLogListAPIView, AdminSiteGlobalSearchAPIView, UserSiteGlobalSearchAPIView

app_name = 'tools'
urlpatterns = [
    path('activity-logs/', ActionLogListAPIView.as_view(), name='action_log_list'),
    path('admin-site/global-search/', AdminSiteGlobalSearchAPIView.as_view(), name='admin_site_global_search'),
    path('user-site/global-search/', UserSiteGlobalSearchAPIView.as_view(), name='global_search'),
]
