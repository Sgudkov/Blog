from django.urls import path
from .views import HomePageView, DetailArticle, SearchResultsView

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('articles/<int:pk>/',DetailArticle.as_view(), name='articles'),
path('search/', SearchResultsView.as_view(), name='search')
]