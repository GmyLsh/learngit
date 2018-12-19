from django.urls import path
from .views import *
urlpatterns = [
    path('list/',SubjectlistView.as_view(),name='subject_list'),
    path('add/',SubjectAddView.as_view(),name='subject_add'),
    path('detail/',SubjectDetailView.as_view(),name='subject_detail'),
    path('update/',SubjectEditView.as_view(),name='subject_edit'),
    path('delete',SubjectDeleteView.as_view(),name='subject_delete'),
]
