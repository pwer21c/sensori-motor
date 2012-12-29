# Create your views here.
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import Http404
from result.models import Action, Result, Mode
from django.http import HttpResponse

def index(request):
    latest_verbe_list=Action.objects.all()
    t=loader.get_template('result/index.html')
    c=Context(
              {'latest_verbe_list':latest_verbe_list,}
              )
    return HttpResponse(t.render(c))

def detail(request, action_id):
    
    try:
        p=Action.objects.get(pk=action_id)
    except Action.DoesNotExist:
        raise Http404
    return render_to_response('result/detail.html',{'action':p})

def results(request, action_id):
    return HttpResponse("You're looking at the results of poll %s." % action_id)
