from django.urls import path

from Python_Web_Basic_Exam_prep import common
from Python_Web_Basic_Exam_prep.common.views import home, create, edit, delete, details

urlpatterns = [
     path('', home, name='home'),
     path('create/', create, name='crete'),
     path('edit/<int:id>' , edit, name='edit'),
     path('delete/<int:id>', delete, name='delete'),
     path('details/<int:id>', details, name='details'),
]