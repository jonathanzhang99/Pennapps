from django.shortcuts import render
from django.http import HttpResponse, JsonResponse	
from django.template import loader, RequestContext
from chemspipy import ChemSpider
import re
import json

# Create your views here.
security_token = "132fb6c6-5179-4ce4-9b4f-2e9ee518d143"

def textToLatex(name, charge=None, number=None, neutrons=None, atomicMass=None):
	latexstr = '/ce{%s}'
	latexname = name

	if number != None and number > 1:

		latexname += str(number)
	if charge != None and charge != 0:
		latexname + "^"
		sign = ''
		if charge > 0:
			sign = '+'
		else:
			sign = '-'

		if abs(charge) != 1:
			sign + str(abs(charge))
		latexname = latexname + "%s" % sign
	if neutrons != None:
		latexname = "_{" + str(neutrons) + "}" + latexname
	if atomicMass != None:
		latexname = "^{" + str(atomicMass) + "}" + latexname

	return latexstr % latexname

def formulaToLatex(name):
	latexstr = '/ce{%s}'
	elements = name.replace("_", "")
	elements = elements.replace("{", "")
	elements = elements.replace("}", "")
	return latexstr % elements

def index(req):

	if req.method == "POST":
		response = HttpResponse
		response["Access-Control-Allow-Origin"] = "*"
		body = json.loads(req.body);
		chemType = req.chemType
		if body.chemType == 'compound':
			CS = ChemSpider(security_token)
			current_chem_symbol = CS.search(body)
			return JSONResponse({"latex": str(formulaToLatex(CS[0].molecularFormula))})

		elif body.chemType == 'element':
			return JSONResponse({"latex": str(textToLatex(body.name, body.charge, body.number, body.neutrons, body.atomicMass))})

		else
			return
	
	else:
		template = loader.get_template('chemInterpreter/index.html')
		return render(req, 'chemInterpreter/index.html')


# def SMILEtoLATEX(molecularFormula){
# 	break
	
# }


	
