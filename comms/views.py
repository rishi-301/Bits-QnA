from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Question, Category, Comment, Rating
from .forms import QuestionForm, CommentcreateForm, RatingForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.db.models import Sum, Avg
from django.core.exceptions import PermissionDenied
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'comms/home.html')



    
class AddQuestionView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'comms/add_qn.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryDet(ListView):
    model = Category
    template_name = 'comms/category.html'

def CategoryView(request, cats):
    category_qns = Question.objects.filter(category = cats).order_by('-avg_rating')
    return render(request, 'comms/categories.html', {'cats':cats, 'category_qns':category_qns})

def CommentCreateView(request, **kwargs):
    current_qn = Question.objects.filter(id=kwargs['pk'])[0]
    qn_comments = Comment.objects.filter(question=current_qn).all()
    current_user=request.user
    qn_rating=Rating.objects.filter(question=current_qn).all()
    times_rated=qn_rating.count()
    if times_rated==0:
        avg_rating=0
    else:
        avg_rating=qn_rating.aggregate(Avg('rating'))['rating__avg']
    current_qn.avg_rating=avg_rating
    current_qn.times_rated=times_rated
    current_qn.save()


    if request.method == 'POST':
        cform = CommentcreateForm(request.POST)
        rform = RatingForm(request.POST)




        if rform.is_valid():
            rform.instance.rater=request.user
            rform.instance.question = current_qn
            rform.save()

        if cform.is_valid():
            cform.instance.author = request.user
            cform.instance.question = current_qn
            cform.save()
        return redirect('detail', current_qn.id)


    else:
        qn_ratings = Rating.objects.filter(question=current_qn).all()
        user_qn_rating = qn_ratings.filter(rater=current_user).all()
        if user_qn_rating.exists():
            rated = 1
        else:
            rated = 0
        cform = CommentcreateForm
        rform = RatingForm
        context = {
            'cform': cform,
            'rform': rform,
            'question': current_qn,
            'comments': qn_comments,
            'rated':rated,
        }
        return render(request, 'comms/detail.html', context)

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'comms/qn_delete.html'
    context_object_name = 'qn'
    success_url = '/report/list/'


def ReportsView(request):
    current_user=request.user
    if current_user.is_authenticated:
        reports = Question.objects.filter(report=True)
        if current_user.is_superuser:
            context={
                'question': reports
            }
            return render(request, 'comms/reported.html', context)
        else:
            raise PermissionDenied

    else:
        return redirect('login')

def reportconfirmview(request, **kwargs):
    current_qn = Question.objects.filter(id=kwargs['pk'])[0]
    if request.method=='POST':
        current_qn.report = True
        current_qn.save()
        messages.warning(request, f'Reported')
        return redirect('home')
    else:
        context={
            'question': current_qn
        }
        return render(request, 'comms/report_confirm.html', context)








    





