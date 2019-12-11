from flask import render_template, redirect, url_for
from  jsonmerge import merge
from app.routes.util import *
from app.response import *

def companies():
	companies = getCompanies()
	if companies.ok:
		return render_template('company/companies.html', menus=menu, title="Empresas", table=legend_company, elements=companies.json())
	return err(companies.status_code)

def createCompany(cnpj, name, rand):
	company = postCompany(cnpj, name, rand)
	if not company or company.ok:
		return render_template('company/register.html', menus=menu, title="Cadastrar", random=random)
	return err(company.status_code)

def companyID(id):
	company = getCompanyId(id)
	numbers = getNumberDocumentsCompanyId(id)
	keys = getKeys(id)
	print(keys)

	if company.ok:
		return render_template('company/company.html', menus=menu, id=str(id), company=company.json(), table=legend, numbers=numbers.json(), keys=keys)
	return err(company.status_code)

