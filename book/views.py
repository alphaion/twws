from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import BookModel,BookOfMonth,Review
import datetime
# Create your views here.

class BookOfMonthView(TemplateView):
    template_name = "book/botm.html"
                                    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        context["BookOfMonth"] = BookOfMonth.objects.get(month=str(today.month)) 
        context["CurrentlyReading"] = BookModel.objects.filter(currently_reading=True).last()
        return context          


class BookReviewListView(ListView):
    template_name="book/review.html"
    model=Review
    context_object_name="reviews"


class BookReviewDetailView(DetailView):
    model=Review
    context_object_name="review"
     

class AboutView(TemplateView):
    template_name="book/about.html"
    