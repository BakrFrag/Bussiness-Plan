from logging import raiseExceptions
from rest_framework.exceptions import ValidationError
from rest_framework import mixins;
from rest_framework.response import Response
from .serializers import *
from .models import Answer, Question
from rest_framework.response import Response
from rest_framework import viewsets;
from rest_framework import permissions
class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class=QuestionSerializer
    def get_queryset(self):
        name=self.request.query_params.get("name")
        print("name:",name)
        if name==None:
            return Question.objects.all().order_by("-id")
        try:
            section = Section.objects.get(name=name);
            return Question.objects.filter(section=section).order_by("-id")
        except Exception as E:
            raise ValidationError("no section associate with this name")
    
class BussinessPlanViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
       serializer_class = BussinessPlanSerializer
       def create(self,request):
           serializer=self.get_serializer(data=request.data);
           serializer.is_valid(raise_exception=True)
           question_id=serializer.validated_data.get("question_id")
           answer=serializer.validated_data.get("answer")
           try:
               question=Question.objects.get(id=question_id)
           except  Exception as E:
                raise ValidationError({"detail":"no question associate with this id"})
           questions_map_answers={
               "Is your business model B2C or B2B or both?":["B2B","B2C","both"],
               "Do you target all age brackets?":["Yes","No"],
               "Do you target all industries?":["Yes","No"],
               "Did you have an investment?":["Yes","No"],
           }
           if question.question == "how much was the investment?" and int(answer) < 0:
               raise ValidationError({"detial":"invetment amount must be >= 0"})
            
           elif answer not in questions_map_answers[question.question]:
               raise ValidationError({"detail":"answer not suitable for question"})
           else:
               user=request.user
               try:
                    answer=Answer.objects.get_or_create(answer=answer)
               
                    bussiness_plan=BussinessPlan.objects.create(user=user,answer=answer,question=question)
               except Exception as E:
                      bussiness_plan=BussinessPlan.objects.create(user=user,answer=answer[0],question=question)
               output={
                   "question":bussiness_plan.question.question,
                   "answer":bussiness_plan.answer.answer
               }
               return Response(output,status=201)
       def get_queryset(self):
           user=self.request.user;
           queryset=BussinessPlan.objects.filter(user=user)
           return queryset

class UserRegisterViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
           serializer_class = UserRegisterSerializer
           model=User
           permission_classes = [permissions.AllowAny,]
           def create(self,request):
               serializer= self.get_serializer(data=request.data)
               serializer.is_valid(raise_exception=True)
               username=serializer.validated_data.get("username")
               password=serializer.validated_data.get("password")
               user=User.objects.create_user(username=username,password=password)
               return Response({"username":username},status=201)

            

