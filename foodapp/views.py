from django import forms
from django.forms import fields
from django.shortcuts import redirect, render

from foodapp.models import Food
from .forms import FoodForm
from django.http.response import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib import messages

# Create your views here.
# belows functonalites are using FBV
'''
def index(req):
    return render(req,'foodapp/index.html')

def addfood(req):
    if req.method=='POST':
        foodform = FoodForm(req.POST)
        if foodform.is_valid():
            foodform.save()
            return HttpResponse('<h1> Food is Added...</h1>')
    else:
        foodform = FoodForm()
    data = {'foodform':foodform}
    return render(req,'foodapp/foodform.html',data)
    '''

# add food with image using FBV
def AddFood(req):
    if req.method=='POST':
        form = FoodForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req,'Food is Added')
            return redirect('FoodMenu')
        else:
            messages.error(req,'Food is Not Added')
            return render(req,'foodapp/foodmenu.html',{'action':'add','form':form})
    elif req.method=='GET':
        form = FoodForm()
        return render(req,'foodapp/foodmenu.html',{'action':'add','form':form})


# Now we convert the FBV functionlaties in CBV

class FoodCreateView(CreateView):
    model = Food
    # fields = ('food_Name',)
    # fields = '__all__'
    form_class = FoodForm
    template_name  = "foodapp/foodmenu.html"
    success_url = reverse_lazy('FoodMenu')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['flist'] = Food.objects.all()
        data.setdefault('action','add')
        return data


class FoodListView(ListView):
    model = Food
    template_name = 'foodapp/foodmenu.html'
    context_object_name = 'flist'

'''
    default values as follow
        template_name = 'appname/modelname_list.html'
        context_object_name = object_list
'''

class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'foodapp/foodmenu.html'
    form_class = FoodForm
    success_url = reverse_lazy('FoodMenu')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['flist'] = Food.objects.all()
        data.setdefault('action','update')
        return data


class FoodDeleteView(DeleteView):
    model = Food
    success_url = reverse_lazy('FoodMenu')
# above view will form object


class FoodDetailView(DetailView):
    model = Food
    template_name = 'foodapp/foodmenu.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['flist'] = Food.objects.all()
        data.setdefault('action','detail')
        return data
