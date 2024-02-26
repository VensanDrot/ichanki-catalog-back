from django.db import models

from config.models import BaseModel


class Category(BaseModel):

    class Meta:
        db_table = 'Category'
