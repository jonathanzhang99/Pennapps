from django.shortcuts import render
from django.http import HttpResponse, JsonResponse	
from django.template import loader, RequestContext
from chemspipy import ChemSpider

# Create your views here.
security_token = "132fb6c6-5179-4ce4-9b4f-2e9ee518d143"

def index(req):

	if req.method == "POST":
		response = HttpResponse
		body = req.body
		chemType = req.chemType
		if chemType == 'element':
			CS = ChemSpider(security_token)
			current_chem_symbol = CS.search(req.)


	
	template = loader.get_template('chemInterpreter/index.html')
	return render(req, 'chemInterpreter/index.html')

def SMILEtoLATEX(molecularFormula){

	
}


	