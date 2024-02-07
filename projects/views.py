from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ProfileSerializer, ProjectSerializer
from django.shortcuts import render
from .models import Profile, Project


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == 'GET':
            profile_id = kwargs.get('pk')
            profile = Profile.objects.get(pk=profile_id)

            return render(
                    request,
                    'profile_detail.html',
                    {
                        'profile': profile,
                    }
            )

        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
