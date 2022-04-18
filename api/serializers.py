from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Project

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class ProjectSerializer(serializers.ModelSerializer):
#   project_name=serializers.SlugRelatedField(many=True, slug_field='project_name', queryset=Project.objects.all())
  class Meta:
    model = Project
    fields = ('__all__'
            #     'id',
            #  'github_link',
            #  'project_name',
            #  'project_type',
            #  'project_landingpage',
            #  'project_description',
            #  'project_owner',
            #  'project_member1',
            #  'project_member2',
            #  'project_member3',
            #  'project_member4',
            #  'project_member5',
            #  'project_member6',
             )

# def create(self, validated_data):
#     project = Project.objects.create_project(**validated_data)
#     return project

# def update(self, instance, validated_data):
#     instance.project_name=validated_data.get('project_name', instance.project_name)
#     instance.project_type=validated_data.get('project_type', instance.project_type)
#     instance.project_description=validated_data.get('project_description', instance.project_description)
#     instance.project_owner=validated_data.get('project_owner', instance.project_owner)
#     instance.project_member1=validated_data.get('project_member1', instance.project_member1)
#     instance.project_member2=validated_data.get('project_member2', instance.project_member2)
#     instance.project_member3=validated_data.get('project_member3', instance.project_member3)
#     instance.project_member4=validated_data.get('project_member4', instance.project_member4)
#     instance.project_member5=validated_data.get('project_member5', instance.project_member5)
#     instance.project_member6=validated_data.get('project_member6', instance.project_member6)
#     instance.github_link=validated_data.get('github_link', instance.github_link)
#     instance.save()
#     return instance
