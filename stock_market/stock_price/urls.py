from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='stockhome'),  #The url setup. When there's  127.0.0.1/ then it'll display whatever is at views.home. Go to views.home
    path('about',views.about,name='stock-about'), #When the user goes to 127.0.0.1/about it'll display views.about. Go to views .about
    path('graph',views.graph,name='stock-graph'),
    path('buy',views.buy,name='stock-buy'),
    path('sell',views.sell,name='stock-sell'),
]
