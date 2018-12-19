from django.urls import path

urlpatterns = [
    path('',GoodsListView.as_view()),
]