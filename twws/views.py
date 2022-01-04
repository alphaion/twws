from django.shortcuts import render
from book.models import BookModel,BookOfMonth
from django.views.generic import TemplateView
import datetime
class Home(TemplateView):
    template_name="home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        context["BookOfMonth"] = BookOfMonth.objects.get(month=str(today.month)) 
        context["CurrentlyReading"] = BookModel.objects.filter(currently_reading=True).last()
        return context
    