from math import ceil

from rest_framework import pagination
from rest_framework.response import Response


class APIPagination(pagination.PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100

    # def paginate_queryset(self, queryset, request, view=None):
    #     # total_pages = len(queryset) // self.get_page_size(request) + 1
    #     # req_page = request.query_params.get('page')
    #     # if req_page:
    #     #     if int(req_page) >= total_pages:
    #     #         return []
    #     #     else:
    #     return super().paginate_queryset(queryset, request, view)
    #
    # def get_paginated_response(self, data):
    #     if data:
    #         return Response({
    #             'links': {
    #                 'next': self.get_next_link(),
    #                 'previous': self.get_previous_link()
    #             },
    #             'count': self.page.paginator.count,
    #             'total_pages': self.page.paginator.num_pages,
    #             'results': data
    #         })
    #     else:
    #         return Response({
    #             'links': {
    #                 'next': None,
    #                 'previous': None
    #             },
    #             'count': 0,
    #             'total_pages': 0,
    #             'results': None
    #         })
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': ceil(self.page.paginator.count / self.get_page_size(self.request)),
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
