import re
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from .models import ZombieSurvivalSocialNetwork
from .serializers import ZssnSerializer
from rest_framework.decorators import api_view
from django.db.models import Count,Q

# Create your views here.

class ZombieSurvivalSocialNetworkAPI(APIView):
    def get(self,request,id=None):
        """
        get:
        Return all the survivors in Zssn.
        """
        if id is not None:
            zssn_obj = ZombieSurvivalSocialNetwork.objects.get(id=id)
            serializer = ZssnSerializer(zssn_obj)
        else:
            zssn_obj = ZombieSurvivalSocialNetwork.objects.all()
            serializer = ZssnSerializer(zssn_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        """
        post:
        Create the new survivors in Zssn.
        """

        serializer = ZssnSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)

    def put(self,request,id=None):
        zssn_obj = ZombieSurvivalSocialNetwork.objects.get(id=id)
        serializer = ZssnSerializer(zssn_obj,data = {'location':request.data.get('location')},partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Location Has Been Updated'})

@api_view(['GET'])
def show_percentage_reports(request):
    """
    get:
    Return the percentage of infected and non-infected usersin Zssn.
    """
    if request.method == 'GET':
        survival_data = ZombieSurvivalSocialNetwork.objects.aggregate(total_count=Count('pk'),infected_count=Count('infected',filter=Q(infected=True)), non_infected_count=Count('infected',filter=Q(infected=False)) )
        infected_count = survival_data.get('infected_count')
        non_infected_count = survival_data.get('non_infected_count')
        total_count = survival_data.get('total_count')
        infected_percentage = (infected_count/total_count) * 100
        non_infected_percentage = (non_infected_count/total_count) * 100
        return Response({'survival_data':{'infected_percentage':infected_percentage,'non_infected_percentage':non_infected_percentage}})

 

