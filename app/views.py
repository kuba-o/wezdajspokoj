from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template import Template, Context, loader, RequestContext
from app.artists import ArtistParser

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        name1=request.GET.get('name1','rumcajsss')
        #name2=request.GET.get('name2','rumcajsss')
        template=Template("""
<html>
<head>
<title>Comparision of top artists of two given users.</title>
</head>
<body>
<form>{% csrf_token %}
User 1: <input type="text" name="name1"><br>
<input type="submit" value="Submit">
</form>

wtf
</body>
</html>
""")

        #user1=ArtistParser.download('rumcajsss')
        #user2=ArtistParser()
        #ArtistParser.download()
        #context1=Context(ArtistParser.download('rumcajsss'))
        #print (ArtistParser.download())
        #print (context1)
        #return HttpResponse(template.render(context1))
        #return HttpResponse(name1)
        #print (ArtistParser.download('rumcajsss'))
        zmienna = ArtistParser.download('rumcajsss')
        zmienna2 = ArtistParser.download('msitake')
        #context = Context(ArtistParser.download(name1))
        #return HttpResponse(template.render(context))
        
        return HttpResponse(zmienna2)