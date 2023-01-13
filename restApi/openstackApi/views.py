from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Openstack
from .serializers import OpenstackSerializer

###################################################
@api_view(["GET"])
def openstack_list_user(request):
    openstackList=Openstack.objects.all()
    openstackSerializer=OpenstackSerializer(openstackList,many=True)
    return Response(openstackSerializer.data)
###################################################
@api_view(["GET"])
def openstack_user_details(request,pk):
    openstackUser=Openstack.objects.get(id=pk)
    openstackUserSerializer=OpenstackSerializer(openstackUser,many=False)
    return Response(openstackUserSerializer.data)
###################################################
@api_view(["POST"])
def openstack_create_user(request):
    openstack_user=OpenstackSerializer(data=request.data)
    
    if openstack_user.is_valid():
        openstack_user.save()
    
    return Response(openstack_user.data)
###################################################
@api_view(["POST"])
def openstack_update_user(request,pk):
    instance=Openstack.objects.get(id=pk)
    openstack_user=OpenstackSerializer(instance=instance,data=request.data)
    
    if openstack_user.is_valid():
        openstack_user.save()
    
    return Response(openstack_user.data)
###################################################
@api_view(["DELETE"])
def openstack_delete_user(request,pk):
    instance=Openstack.objects.get(id=pk)
    instance.delete()
    
    return Response("user deleted!")