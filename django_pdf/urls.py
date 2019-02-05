from django.contrib import admin
from django.urls import path

from pdf.views import index, pdf, pdf2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('pdf/', pdf),
    path('pdf2/', pdf2),
]
