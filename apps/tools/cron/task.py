import logging
from os import remove
from os.path import join as join_path

from django.conf import settings

from apps.files.models import File

logger = logging.getLogger()


def unused_files():
    upload_path = settings.FILE_UPLOAD_DIR
    all_files = File.objects.filter(catalog_id__isnull=True,
                                    specification_id__isnull=True,
                                    news__isnull=True,
                                    article__isnull=True,
                                    store__isnull=True).values_list('id', flat=True)
    unused_files_list = set(all_files)
    for file in unused_files_list:
        file_name = File.objects.get(id=file).gen_name
        file_obj = File.objects.get(id=file)
        file_path = join_path(upload_path, file_name)
        try:
            remove(file_path)
            file_obj.delete()
        except Exception as e:
            logger.debug(f"Error unused_files_cron: {e.args}")
