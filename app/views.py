from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template import Template, Context, loader, RequestContext
from app.artists import ArtistParser
from app.artists import Compare

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        name1=request.GET.get('name1','rumcajsss')
        name2=request.GET.get('name2','msitake')
        template=Template("""
<html>
<head>
<link rel="stylesheet" href="stylesheet.css"/>
<title>Comparision of top artists of two given users.</title>
</head>
<body>
<form>{% csrf_token %}
User 1: <input type="text" name="name1"><br>
User 2: <input type="text" name="name2"><br>
<input type="submit" value="Submit">
</form>
{% for artist in artists2 %}
<h2>
    {{ artist }}

</h2>
{% endfor %}
</body>
</html>
""")
        artists_list_1 = ArtistParser.downloadArtists(name1)
        artists_list_2 = ArtistParser.downloadArtists(name2)
        #print (artists_list)
        common_artists =  Compare.checkCommon(artists_list_1, artists_list_2)
        # context1=Context(ArtistParser.downloadArtists(name1))
        context1=Context({"artists1": artists_list_1})
        context2=Context({"artists2": artists_list_2})
        #return HttpResponse(template.render(context2))
        return HttpResponse({"artists2" : common_artists})
        #return HttpResponse(name1)
        #print (ArtistParser.download('rumcajsss'))
        
        #context = Context(ArtistParser.download(name1))
        #return HttpResponse(template.render(context))
        
        #zmienna = Compare.checkCommon(ArtistParser.downloadArtists('rumcajsss'),
         #   ArtistParser.downloadArtists('msitake'))
        #return HttpResponse(ArtistParser.downloadArtists('rumcajsss'))
        #return HttpResponse(zmienna)