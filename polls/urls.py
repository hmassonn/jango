from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='base'),
    # ex: /polls/5/
    path('<int:product_id>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:product_id>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:product_id>/vote/', views.vote, name='vote'),
]