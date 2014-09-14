from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from chemspipy import ChemSpider

# Create your views here.
security_token = "132fb6c6-5179-4ce4-9b4f-2e9ee518d143"
CS = ChemSpider()
def index(req):
	
	template = loader.get_template('chemInterpreter/index.html')
	return render(req, 'chemInterpreter/index.html')

	if (req.method == "POST"){

	}