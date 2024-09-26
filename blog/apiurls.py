# apiurls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apiviews import PostViewSet, CategoryViewSet, TagViewSet, ProfileViewSet, CommentViewSet, SignUpView, SignInView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('api-auth/', include('rest_framework.urls')),
]
