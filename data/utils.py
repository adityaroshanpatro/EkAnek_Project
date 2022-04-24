import csv
import datetime
import logging
from wsgiref.util import FileWrapper

from django.http import HttpResponse
from import_export.admin import ImportExportMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from simple_history.admin import SimpleHistoryAdmin







class SaveModel(ImportExportMixin, SimpleHistoryAdmin):
    def save_model(self, request, obj, *args, **kwargs):
        if not obj.created_by:
            obj.created_by = request.user.username
        obj.last_updated_by = request.user.username
        return obj
