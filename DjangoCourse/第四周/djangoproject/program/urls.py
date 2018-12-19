from django.urls import path
from program import views
urlpatterns = [
    path('add/',views.program_add),
    path('detail/',views.program_detail),
    path('edit/',views.program_edit),
    path('list/',views.program_list),
]