from flask import render_template, redirect, url_for
from app.routes.util import *
from app.routes.company import *
from app.response import *

def numberDocuments(id):
	legend = {'title_1': 'Numero do Documento', 'title_2':'Status'}
	numbers = []
	numbers = getNumberDocumentsCompanyId(str(id))
	if numbers.ok:
		return render_template('numberDoc/numberdocuments.html', menus=menu, title="Numero de Documento", table=legend, elements=numbers.json(), id_company=str(id))
	return err(numbers.status_code)

def numberDocumentsId(id):
	legend = {'title_1': 'Numero do Documento', 'title_2':'CNPJ'}
	numbers = getNumberDocuments(str(id))
	if numbers.ok:
		return render_template('numberDoc/numberdocuments.html', menus=menu, title="Numero de Documento", table=legend, elements=numbers.json())
	return err(numbers.status_code)

def addNumberDocument(number, id_company):
	numberDoc = postNumberDocument(number, id_company)
	if not numberDoc or numberDoc.ok:
		return render_template('numberDoc/register.html', menus=menu, title="Numero de Documento", id_company=str(id_company))
	return err(numberDoc.status_code)