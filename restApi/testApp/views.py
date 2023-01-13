from django.shortcuts import render,redirect
import requests
import json
# Create your views here.


# api receive openstack
def show_user_list(request):
    response=requests.get('http://127.0.0.1:8000/openstackApi/openstack_list_user').json()
    context={
        'list_user':response
    }
    return render(request,'index.html',context)

# api send openstack
def create_user(request):
    # receive data forntend
    instance={'name':'user4','password':123456,'nameProject':'website4'}
    jsonUser=json.dumps(instance)
    headers={'content-type':'application/json'}   
    requests.post('http://127.0.0.1:8000/openstackApi/openstack_create_user/',data=jsonUser,headers=headers)
    
    return redirect(show_user_list)
    