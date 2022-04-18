from urllib import response
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response
from django.http.response import HttpResponse, JsonResponse
from knox.auth import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from api.models import Project
from api.serializers import ProjectSerializer

from django.core.files.storage import default_storage

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


@csrf_exempt
def projectApi(request, id=0):
    if request.method== 'GET':
        projects= Project.objects.all()
        projects_serializer= ProjectSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe= False)

    elif request.method =='POST':
        project_data=JSONParser().parse(request)
        project_serializer = ProjectSerializer(data=project_data)
        if project_serializer.is_valid():
           project_serializer.save()
        #    return response(project_serializer.data)
           return JsonResponse("Project Uploaded succesfully", safe = False)
    
        return JsonResponse("Project failed to upload.", safe = False)

    elif request.method =='PUT':
        project_data = JSONParser().parse(request)
        project = Project.objects.get(id = '9')
        projects_serializer = ProjectSerializer(project, data = project_data)
        if projects_serializer.is_valid():
                projects_serializer.save()
                return JsonResponse("Updated succesfully", safe =False)
        return JsonResponse("Update Failed", safe= False)

    else:
        request.method =='Delete'
        project= Project.objects.get(id='2')
        project.delete()
        return JsonResponse("Deleted!", safe = False)

@csrf_exempt
def SaveFile(request):
    file =request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)