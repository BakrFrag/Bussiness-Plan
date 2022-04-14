
from django.urls import path;
from rest_framework.routers import DefaultRouter
from .views import *

router= DefaultRouter();
router.register("question",viewset=QuestionViewSet,basename="questions")
router.register("plan",viewset=BussinessPlanViewSet,basename="plan")
router.register("user",viewset=UserRegisterViewset,basename="user")
urlpatterns = [

]
urlpatterns += router.urls 
   
   
