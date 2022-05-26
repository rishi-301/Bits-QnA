from django.urls import path, include
#from . import views
from .views import home, CommentCreateView, AddQuestionView, CategoryDet, CategoryView, ReportsView, QuestionDeleteView, reportconfirmview
urlpatterns = [
    #path('', views.home, name='home')
    path('', home, name='home'),
    path('question/<int:pk>', CommentCreateView, name='detail'),
    path('add_qn/', AddQuestionView.as_view(), name='add_qn' ),
    path('category/', CategoryDet.as_view(), name='category-det'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('report/list/',ReportsView,name='reports'),
    path('question/<int:pk>/report', reportconfirmview, name='report_confirm'),
    path('question/<int:pk>/delete', QuestionDeleteView.as_view(), name='qn_delete'),
]
