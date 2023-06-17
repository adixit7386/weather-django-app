from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e8558e63f3770ba446c7a1912f259388').read()
        json_data = json.loads(res)
        data={
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'K',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
        }
        return render(request,'index.html',{'data':data,'city':city})
    else:
        data={}
        city=""
        return render(request,'index.html',{'data':data,'city':city})