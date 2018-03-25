# -*- coding=utf-8 -*-
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #如果是安全的方法（如GET），直接返回True
        if request.method in permissions.SAFE_METHODS:
            return True
        # 如果是不安全的方法（如DELETE,POST），只有发出请求的是拥有者才返回True
        return obj.owner == request.user