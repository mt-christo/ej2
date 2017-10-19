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
    x = pd.read_csv('story/static/' + product.tspath)


    x = pd.read_csv('/var/www/django/antontest/story/static/gspc.csv')
    x.Date = pd.to_datetime(x.Date)
    x.Close = x.Close/x.Close[0]
    
    dates = ['2007-08-09', '2009-07-01', '2012-01-01', '2016-10-01']
    labels = ["Pre-Crisis", "2008-2009 Crisis", "QE era", "Obama 2", "Trump era"]
    intdates = pd.to_datetime(np.array(dates)).astype(np.int64)
    bins = pd.DataFrame({'bin': range(len(dates)+1), 'label': labels})

    x['bin'] = np.digitize(x.Date.astype(np.int64), intdates)
    x = pd.merge(x, bins, 'inner', 'bin')

    x_months = x.set_index(pd.DatetimeIndex(x.Date))
    x_months = x_months.groupby([pd.TimeGrouper('M')])
    x = pd.merge(x, x_months.agg({'Date': 'max'}), 'inner', ['Date'])
    
    b = x.rename(columns={'label': 'note'}).groupby(['bin', 'note'])
    b = b.agg({'Date': 'min', 'Close': ['max', 'min']}).reset_index()
    b.columns = b.columns.get_level_values(0)
    b.columns = ['bin', 'note', 'closemax', 'closemin', 'Date']
    b['r'] = np.array(b.closemax.astype(float))/np.array(b.closemin.astype(float)) - 1.0
    b['ann'] = '39;' + b.r.apply(lambda x: str(round(100*x,1))) + '%39;'
    b.note = '39;' + b.note + '%39;'
    x = pd.merge(x, b, 'left', 'Date')
    x.loc[x.ann != x.ann, 'ann'] = 'null'

    data = np.array(x.apply(lambda row: str(['new Date('+str(row.Date.date()).replace('-',',')+')', row.Close, row.Close*0.9, row.ann]), axis=1))
    ticks = np.array(b.apply(lambda row: '{v: new Date('+str(row.Date.date()).replace('-',',')+'), f: ' + row.note + '}', axis=1))
    return render_to_response("story/" + product.templatepath, {'product': product, 'data': data, 'ticks' : ticks})
