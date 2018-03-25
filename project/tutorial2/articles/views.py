 #database
from models import Article
from django.contrib.auth.models import User

#serializers
from serializers import ArticleSerializer,UserSerializer

#views
from rest_framework import viewsets
from rest_framework import generics

#permissions
from rest_framework import permissions
from permissions import IsOwnerOrReadOnly

#decorators
from rest_framework.decorators import list_route


class ArticleViewSet(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset=Article.objects.all()
        query_params=self.request.query_params
        if query_params.has_key('username'):
            user=User.objects.get(username=query_params['username'])
            queryset=queryset.filter(owner=user)
        return queryset


class SpecifiedUserFilteredArticles(generics.ListCreateAPIView):
    serializer_class=ArticleSerializer
    permissions_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    def get_queryset(self):
        username=User.objects.get(username=self.kwargs['username'])
        return Article.objects.filter(owner=username)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

