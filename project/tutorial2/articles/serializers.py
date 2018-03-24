# -*- coding=utf-8 -*-
from rest_framework import serializers
from models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    #owner设为ReadOnlyField
    owner=serializers.ReadOnlyField(source='owner.username')

    #以Article为模板，并规定有哪些字段
    class Meta:
        model=Article
        fields=('url','id','title','content','owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    #此处aritcle设为超链接字段
    articles=serializers.HyperlinkedIdentityField(many=True,view_name='article-detail',read_only=True)
    
    #以User为模板，并规定有哪些字段
    class Meta:
        model=User
        fields=('url','id','username','articles')