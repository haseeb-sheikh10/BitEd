from django.urls import path
from questions.views import QuestionCreate
from questions.views import MyQuestionsUpdate
from questions.views import SelectTiles

urlpatterns = [
    path('',
          QuestionCreate.as_view(),
          name="createQuestion"),
    path('question_update/<int:pk>', 
         MyQuestionsUpdate.as_view(), 
         name='question_update'),
    path('select_tiles/<int:pk>',
         SelectTiles.as_view(),
         name='select_tiles')
]

