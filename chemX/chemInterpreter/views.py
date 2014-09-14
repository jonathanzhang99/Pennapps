from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
# Create your views here.
def index(req):
	
	template = loader.get_template('chemInterpreter/index.html')
	return render(req, 'chemInterpreter/index.html')