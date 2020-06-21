from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import json
import RPi.GPIO as GPIO
def index(request):
    print("index html")
    return HttpResponse("hello you are at the index page")
class dealer():
        def dealres(self,flag,msg,event):
            ms = {}
            filt=flag
            print("dealer function ")
            if filt ==0:
              ms['code'] = 0
              ms['message'] = '失败'
            else:
              ms['code'] = 1
              ms['message'] = '成功'
            ms['data']=msg 
            ms['event']=event
            presendmsg = json.dumps(ms, ensure_ascii=False)
            print(presendmsg)
            send=presendmsg.encode('utf-8')
            return send
def initgpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24,GPIO.OUT)
class Dht11Get(View):
    def get(self,request):
         return HttpResponse(dealer().dealres(1,23,"dht11 get data"))
class Pumb(View):
    def get(self,request):
        print("pumb")
        initgpio()
        msg=request.GET.get('msg')
        if msg=="open":
           GPIO.output(24,GPIO.HIGH) 
           return HttpResponse(dealer().dealres(1,msg,"pumb open"))
        elif msg=="close":
           GPIO.output(24,GPIO.LOW)
           return HttpResponse(dealer().dealres(1,msg,"pumb close"))

# Create your views here.

