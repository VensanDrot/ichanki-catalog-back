from os import remove as delete_file

from django.core.files.images import get_image_dimensions
from django.utils.translation import gettext_lazy as _
from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.files.models import File
from apps.files.utils import upload_file
from config.utils.api_exceptions import APIValidation


class FileCreateAPIView(APIView):
    parser_classes = [MultiPartParser, ]

    @swagger_auto_schema(
        operation_description="Upload file",
        manual_parameters=[
            openapi.Parameter(
                'file', in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=True,
                description=_('The file to upload (max size 50 MB)')
            ),
            openapi.Parameter(
                'miniature', in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                enum=[0, 1],
                required=False,
                description=_('Flag to indicate if the file is a miniature')
            ),
        ]
    )
    def post(self, request):
        file = request.data.get('file')
        if not file:
            raise APIValidation(detail=_('File was not sent'), code=status.HTTP_400_BAD_REQUEST)

        is_miniature = int(request.query_params.get('miniature', 0))

        if 'image' in file.content_type:
            dimensions = get_image_dimensions(file)  # (width, height)
            if dimensions != (100, 100) and is_miniature:
                raise APIValidation(detail=_('Image dimensions should be 100x100'), code=status.HTTP_400_BAD_REQUEST)

        if file.size > 52_428_800:
            raise APIValidation(detail=_('The file size has exceeded 50 mb!'), code=status.HTTP_400_BAD_REQUEST)

        e_file = upload_file(file=file)
        return Response({
            "message": "File successfully uploaded",
            "file": e_file.id,
            "status": status.HTTP_201_CREATED
        }, status=status.HTTP_201_CREATED)


class FileDeleteAPIView(APIView):

    @staticmethod
    def get_object(pk):
        try:
            return File.objects.get(pk=pk)
        except File.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        file = self.get_object(pk)
        delete_file(file.path)
        file.delete()
        return Response({
            "message": "File successfully deleted",
            "status": status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class UploadFilesAPIView(APIView):
    parser_classes = [MultiPartParser, ]

    @staticmethod
    @swagger_auto_schema(
        operation_description="Upload files",
        manual_parameters=[
            openapi.Parameter(
                'files', in_=openapi.IN_FORM,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_FILE),
                required=True,
                description=_('The file to upload (max size 50 MB)')
            )
        ]
    )
    def post(request, *args, **kwargs):
        files = request.FILES.getlist('files')
        if not files:
            raise APIValidation(detail=_('File was not sent'), code=status.HTTP_400_BAD_REQUEST)

        response = []
        for file in files:
            if file.size > 52_428_800:
                raise APIValidation(detail=_('The file size has exceeded 50 mb!'), code=status.HTTP_400_BAD_REQUEST)
            e_file = upload_file(file=file)
            response.append(e_file.id)
        return Response({
            "files": response,
            "status": status.HTTP_201_CREATED
        })
