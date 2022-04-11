from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OfferSerializer, CategorySerializer

from .models import Category, Offer

@api_view(['GET'])
def apiOverwiew(request):
    api_urls = {
        'View all offers':'/offers',
        'View all categories':'/category',
        'View offer detail':'offers/{id}/',
        'Create offer':'offers_create',
        'Update offer':'offers_update/{id}/',
        'Delete offer':'offers_delete/{id}',
        'Create category':'category_create/',
        'Update category':'category_update/{id}/',
        'Delete category':'category_delete/{id}/',
    }
    return Response(api_urls)

@api_view(['GET'])
def offer_list(request):
    if request.method == 'GET':
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

@api_view(['GET'])
def offer_detail(request, pk):
    if request.method == 'GET':
        offers = Offer.objects.get(id=pk)
        serializer = OfferSerializer(offers, many=False)
        return Response(serializer.data)
    
@api_view(['POST'])
def offer_create(request):
    if request.method == 'POST':
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Not all data have been passed")

@api_view(['PUT'])
def offer_update(request, pk):
    if request.method == 'PUT':
        offer = Offer.objects.get(id=pk)
        serializer = OfferSerializer(instance=offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Not all data have been passed")

@api_view(['DELETE'])
def offer_delete(request, pk):
    if request.method == 'DELETE':
        offers = Offer.objects.get(id=pk)
        offers.delete()
        return Response('Offer deleted')


@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def category_create(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Not all data have been passed")

@api_view(['PUT'])
def category_update(request, pk):
    if request.method == 'PUT':
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Not all data have been passed")

@api_view(['DELETE'])
def category_delete(request, pk):
    if request.method == 'DELETE':
        categorys = Category.objects.get(id=pk)
        categorys.delete()
        return Response('Category deleted')
