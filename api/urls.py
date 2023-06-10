from django.urls import path
from . import views
urlpatterns=[
path('restaurants/',views.Resturants.as_view()),
path('restaurants/<str:restaurant_id>/',views.ResturantDetail.as_view()),
path('restaurants/<str:restaurant_id>/recipes/',views.Recipes.as_view()),
path('restaurants/<str:restaurant_id>//recipes/<str:recipe_id>/',views.RecipeDetail.as_view()),
]
