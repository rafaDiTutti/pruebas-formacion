from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_view(request):
    car_list= [
        {"title":"BMW"},
        {"title":"Mercedes"},
        {"title":"Audi"}
        ]
    context = {"car_list" : car_list} 
    return render(request, "my_first_app/car_list.html", context)

def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")


class CarLiisView(TemplateView):
    template_name = "my_first_app/car_list.html"


    def get_context_data():
        car_list= [
            {"title":"BMW"},
            {"title":"Mercedes"},
            {"title":"Audi"}
            ]
        return {"car_list" : car_list} 