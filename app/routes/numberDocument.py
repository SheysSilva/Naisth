from flask import render_template, redirect, url_for
from app.routes.util import *
from app.routes.company import *
from app.response import *

def addNumberDocument(number, id_company):
	numberDoc = postNumberDocument(number, id_company)
	if not numberDoc or numberDoc.ok:
		return render_template('numberDoc/register.html', menus=menu, title="Numero de Documento", id_company=str(id_company))
	return err(numberDoc.status_code)