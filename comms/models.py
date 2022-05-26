from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

rating = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
# cat = (
#     ('Academics', 'Academics'),
#     ('Sports', 'Sports'),
#     ('Financial', 'Financial'),
#     ('Food and Accomodation', 'Food and Accomodation'),
#     ('Others', 'Others'))

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Question(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=255, default='Others')
    year = models.CharField(max_length = 10, default='1st Year')
    report = models.BooleanField(default=False)
    avg_rating = models.DecimalField(default=0.00, decimal_places=2, max_digits=4)
    times_rated = models.IntegerField(default=0)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        print('Now')
        return reverse('detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    date_posted=models.DateTimeField(default=timezone.now)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    body=RichTextField()


    def __str__(self):
        return self.body

class Rating(models.Model):

    rater=models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(choices=rating)



    



