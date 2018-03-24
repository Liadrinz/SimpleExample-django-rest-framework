 #database
from models import Article
from django.contrib.auth.models import User

#serializers
from serializers import ArticleSerializer,UserSerializer

#views
from rest_framework import viewsets

#permissions
from rest_framework import permissions
from permissions import IsOwnerOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

