from django.urls import path,include
from .views import MobileInfoApiView, MobileInfoDetailView, MobileInfoSerializer, MobileInfoNewView, Mobileinfo, \
    Mobileinfosingle
from rest_framework.routers import DefaultRouter
from .views import DataViewSet
router = DefaultRouter()
router.register('', DataViewSet)

urlpatterns = [
    path('', MobileInfoApiView.as_view()),
    #path('<int:pk>/', MobileInfoDetailView.as_view()),
    path('new/', MobileInfoNewView.as_view()),
    #path('/', Mobileinfo.as_view()),
    # path('', Mobileinfo.as_view()),
    path('<int:pid>/', Mobileinfosingle.as_view()),
    # path('other', include(router.urls)),

]