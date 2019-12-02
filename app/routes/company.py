from flask import render_template, redirect, url_for
from app.routes.util import *
from app.response import *

def companies():
	companies = getCompanies()
	if companies.ok:
		return render_template('company/companies.html', menus=menu, title="Empresas", table=legend_company, elements=companies.json())
	return err(companies.status_code)

def addCompany(cnpj, name):
	company = postCompany(cnpj, name)
	if not company or company.ok:
		return render_template('company/register.html', menus=menu, title="Cadastrar")
	return err(company.status_code)

def free():
	_keys = getFree()
	if _keys.ok:
		return render_template('list.html', menus=menu, title="Chaves Livres", options=options, table=legend, elements=_keys.json())
	return err(_keys.status_code)

def using():
	_keys = getUsing()
	if _keys.ok:
		return render_template('list.html', menus=menu, title="Chaves em Uso", options=options, table=legend, elements=_keys.json())
	return err(_keys.status_code)

def ok():
	_keys = getOk()
	if _keys.ok:
		return render_template('list.html', menus=menu, title="Chaves Utilizadas", options=options, table=legend, elements=_keys.json())
	return err(_keys.status_code)

