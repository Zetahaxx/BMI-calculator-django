#from django.http import HttpResponse
from django.shortcuts import render

def calc(request):
    return render(request,"index.html")
    
def process(request):
    wt=float(request.GET["weight"])
    ht=float(request.GET["height"])
    bmi=(wt*100*100)/(ht*ht)
    category=["underweight","normal","overweight","obesity"]
    if bmi<18.5:
        result=category[0]
    elif bmi>=18.5 and bmi<=24.9:
        result=category[1]
    elif bmi>=25.0 and bmi<=29.9:
        result=category[2]
    else:
         result=category[3]
    params={"value":bmi,"what":result}
    return render(request,'process.html',params)
