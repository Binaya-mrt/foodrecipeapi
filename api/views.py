from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Resturant,Recipe,Ingredient
from django.http import Http404
from rest_framework import status




class Resturants(APIView):
    def get(self,request):
        restaurants=Resturant.objects.all()
        serializer=serializers.ResturantSerializer(restaurants,many=True)
        return Response(serializer.data)
    
    def post(self,request):
       
        serializer=serializers.ResturantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ResturantDetail(APIView):
    def get(self,request,restaurant_id):
       
        try:
            restaurant=Resturant.objects.get(pk=restaurant_id)
        except Resturant.DoesNotExist:
            raise Http404
        
        serializer=serializers.ResturantSerializer(restaurant)
        return Response(serializer.data)
    def delete(self,request,restaurant_id):
        try:
            restaurant=Resturant.objects.get(pk=restaurant_id)
        except Resturant.DoesNotExist:
            raise Http404
        
        restaurant.delete()
        return Response( status=status.HTTP_204_NO_CONTENT)
    
class Recipes(APIView):
    def get(self,request,restaurant_id):
       recipes=Recipe.objects.filter(restaurant_id=restaurant_id)
       serializer=serializers.RecipeSerializer(recipes,many=True)
       return Response(serializer.data)
    
    def post(self,request,restaurant_id):
        try:
            Resturant.objects.get(pk=restaurant_id)
        except Resturant.DoesNotExist:
            raise Http404
        
        serializer=serializers.RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant__id=restaurant_id,ingredients=request.data.get('ingredients'))
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RecipeDetail(APIView):
    def get(self,request,restaurant_id,recipe_id):
        try:
            recipe = Recipe.objects.get(restaurant__id=restaurant_id, pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        serializer = serializers.RecipeSerializer(recipe)
        return Response(serializer.data)
    
    def delete(self, request, restaurant_id, recipe_id):
        try:
            recipe = Recipe.objects.get(restaurant__id=restaurant_id, pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        