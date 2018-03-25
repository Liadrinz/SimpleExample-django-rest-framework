from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
import views

router=DefaultRouter()
router.register('articles',views.ArticleViewSet)
router.register('users',views.UserViewSet)

# Create a router and register our viewsets with it.

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^articles/user/(?P<username>.+)/$',views.SpecifiedUserFilteredArticles.as_view()),
    url(r'^',include(router.urls))
]

