from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from story.models import Product, Provider
import numpy as np
import pandas as pd
import random

# Create your views here.


def allproducts(request):
    #return render_to_response("story/allproducts.html", {'products' : Product.objects.all()})
    return render_to_response("story/tmp.html", {'products' : Product.objects.all()})

def product(request,id):
    product = Product.objects.get(pk=id)
    #x.apply(lambda row: "[new Date('" + str(row.Date) + "'), " + str(row.Close),axis=1) + "]"
    #product = Product.objects.all()[0]
    x = pd.read_csv('story/static/' + product.tspath)
    x.Date = pd.to_datetime(x.Date)
    x = pd.merge(x,x.set_index(pd.DatetimeIndex(x.Date)).groupby([pd.TimeGrouper('M')]).agg({'Date':'max'}),'inner',['Date'])
    data = np.array(x.apply(lambda row: str(['new Date('+str(row.Date.date()).replace('-',',')+')', row.Close]),axis=1))
#    data = np.array(x.apply(lambda row: [int(x) for x in str(row.Date).split('-')] + [row.Close],axis=1))[1]
    return render_to_response("story/" + product.templatepath, {'product': product, 'data': data})
