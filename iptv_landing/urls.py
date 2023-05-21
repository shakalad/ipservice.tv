from django.urls import path
from .views import index, success_page, index_kz, success_page_kz


urlpatterns = [
    path('', index),
    path('kz', index_kz),
    path('success', success_page),
    path('success_kz', success_page_kz),
]
