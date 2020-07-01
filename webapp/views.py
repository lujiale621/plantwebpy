from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import json
import RPi.GPIO as GPIO
import webapp.src.dht11test.dht11start as dht
import webapp.src.gy30.light as igt
import requests

header = {

            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",

            }
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
    GPIO.setup(25,GPIO.OUT)
    GPIO.setup(12,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
class LightGet(View):
    def get(self,request):
        light=igt.getlight()
        data={'data':light,'name':'putlight'}
        url="http://192.168.1.109:8080/penzai/insert"
        requests.post(url,data,headers=header)
        return HttpResponse(dealer().dealres(1,light,"coisture get data"))
class DeepGet(View):
    def get(self,request):
        msg=request.GET.get('msg')
        url="http://192.168.1.109:8080/penzai/insert"
        data={'data':msg,'name':'putdeepget'}
        requests.post(url,data,headers=header)
        return HttpResponse(dealer().dealres(1,msg,"coisture get data"))
class SoilGet(View):
    def get(self,request):
        msg=request.GET.get('msg')
        data={'data':msg,'name':'putsoilget'}
        #url="http://192.168.1.109:8080/penzai/insert?"+"name=putsoilget&"+"data="+str(msg)
        url="http://192.168.1.109:8080/penzai/insert"
        requests.post(url,data,headers=header)
        return HttpResponse(dealer().dealres(1,msg,"coisture get data"))
class Dht11Get(View):
    def get(self,request):
         dht11 = dht.DHT11(23)
         ret,temp,humi = dht11.GetTemp()
         st="temp:"+str(temp)+"hum:"+str(humi)
         data={'data':st,'name':'putdht11'}
         url="http://192.168.1.109:8080/penzai/insert"
         requests.post(url,data,headers=header)
         return HttpResponse(dealer().dealres(1,st,"dht11 get data"))
class Pumb(View):
    def get(self,request):
        initgpio()
        msg=request.GET.get('msg')
        if msg=="open":
           GPIO.output(24,GPIO.HIGH) 
           return HttpResponse(dealer().dealres(1,msg,"pumb open"))
        elif msg=="close":
           GPIO.output(24,GPIO.LOW)
           return HttpResponse(dealer().dealres(1,msg,"pumb close"))
class Pumb2(View):
        def get(self,request):
            initgpio()
            msg=request.GET.get('msg')
            if msg=="open":
               GPIO.output(25,GPIO.HIGH)
               return HttpResponse(dealer().dealres(1,msg,"pumb2 open"))
            elif msg=="close":
               GPIO.output(25,GPIO.LOW)
               return HttpResponse(dealer().dealres(1,msg,"pumb2 close"))
class Spray(View):
        def get(self,request):
            initgpio()
            msg=request.GET.get('msg')
            if msg=="open":
               GPIO.output(12,GPIO.HIGH)
               return HttpResponse(dealer().dealres(1,msg,"spray open"))
            elif msg=="close":
               GPIO.output(12,GPIO.LOW)
               return HttpResponse(dealer().dealres(1,msg,"spray close"))
class Moudlebat(View):
        def get(self,request):
            initgpio()
            msg=request.GET.get('msg')
            if msg=="open":
               GPIO.output(16,GPIO.HIGH)
               return HttpResponse(dealer().dealres(1,msg,"it has open"))
            elif msg=="close":
               GPIO.output(16,GPIO.LOW)
               return HttpResponse(dealer().dealres(1,msg,"it has close"))


# Create your views here.

