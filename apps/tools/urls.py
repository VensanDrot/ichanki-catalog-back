from django.urls import path

from apps.tools.views import ActionLogListAPIView, GlobalSearchAPIView

app_name = 'tools'
urlpatterns = [
    path('activity-logs/', ActionLogListAPIView.as_view(), name='action_log_list'),
    path('global-search/', GlobalSearchAPIView.as_view(), name='global_search'),
]
