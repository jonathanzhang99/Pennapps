from django.shortcuts import render
from django.http import HttpResponse, JsonResponse	
from django.template import loader, RequestContext
from chemspipy import ChemSpider
import re
import json

# Create your views here.
security_token = "132fb6c6-5179-4ce4-9b4f-2e9ee518d143"

def textToLatex(name, neutrons=None, charge=None, atomicMass=None, number=None):
	
	latexstr = '\ce{%s}'
	latexname = name
	if number != '' and number > 1:
		latexname += str(number)

	try:
		if charge != '' and int(charge) != 0:
			sign = ''
			latexname += "^"
			if int(charge) > 0:
				sign = '+'
			else:
				sign = '-'
			if abs(int(charge)) != 1:
				sign = str(abs(int(charge)))+sign
			latexname += sign
	except ValueError:
		if charge == '-':
			latexname += '-' 

	if atomicMass != '':
		latexname = "_{" + str(atomicMass) + "}" + latexname

	if neutrons != '':
		latexname = "^{" + str(neutrons) + "}" + latexname



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
		# response["Access-Control-Allow-Origin"] = "*"
		print "POST METHOD"
		body = json.loads(req.body);
		print body
		print body['chemType']
		chemType = body['chemType']
		values = body['value']
		print chemType == 'compound'
		if chemType == 'compound':
			print "in this function"
			CS = ChemSpider(security_token)
			current_chem_symbol = CS.search(body)
			print current_chem_symbol
			print current_chem_symbol[0].common_name
			returned_responses = [formulaToLatex(c.molecularFormula) for c in current_chem_symbol]
			if len(returned_responses) > 4:
				returned_responses = returned_responses[:4]
			return JSONResponse({"latex": str(returned_resposnes)})

		elif chemType == 'element':
			name = body['name']
			print "arrived at function"
			for i in range(4):
				print values[i]
			print name
			print textToLatex(name, values[0], values[1], values[2], values[3])

			# return JSONResponse({"latex": textToLatex(name, values[0], values[1], values[2], values[3])})
			return HttpResponse(textToLatex(name, values[0], values[1], values[2], values[3]), content_type="text/plain")

		else:
			return

	else:
		template = loader.get_template('chemInterpreter/index.html')
		return render(req, 'chemInterpreter/index.html')


# def SMILEtoLATEX(molecularFormula){
# 	break
	
# }


	
