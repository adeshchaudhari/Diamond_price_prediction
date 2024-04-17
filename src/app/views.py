from django.shortcuts import render,redirect
import pandas as pd
import numpy as np
import pickle

def getPredictions(carat,cut,color,clarity,depth,table,x,y,z):
    model = pickle.load(open("diamond_price.pkl", "rb"))
    prediction = model.predict([[carat,cut,color,clarity,depth,table,x,y,z]])
    
    return prediction

def index(request):
    return render(request,'index.html')

def form(request):
    return render(request,'form.html')

def calc_price(request):

    if request.method=='POST':
        carat = eval(request.POST.get('carat'))
        cut = eval(request.POST.get('cut'))
        color = eval(request.POST.get('color'))
        clarity = eval(request.POST.get('clarity'))
        depth = eval(request.POST.get('depth'))
        table = eval(request.POST.get('table'))
        x = eval(request.POST.get('x'))
        y = eval(request.POST.get('y'))
        z = eval(request.POST.get('z'))

        result = getPredictions(carat,cut,color,clarity,depth,table,x,y,z)
        diamond_prices = np.around(result[0],2)

        context = {
            'result':diamond_prices,
        }
        return render(request,'price.html',context)