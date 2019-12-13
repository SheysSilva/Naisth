import json
from app import app
from flask import render_template, redirect, url_for
from pygments import highlight, lexers, formatters
from app.response import *
from app.routes import company,  key
from app.routes.util import *

@app.route("/", methods=['GET'])
def index():
	return render_template('home.html', menus=menu, title="Home")

@app.route("/company/", methods=['GET'])
def companies():
	return company.companies()

@app.route("/company/register/", methods=['GET', 'POST'])
def postCompany():
	cnpj = request.form.get('cnpj-company')
	name = request.form.get('name-company')
	random = request.form.get('type-random-company')
	return company.createCompany(cnpj, name, random)

@app.route("/company/<string:id_company>/", methods=['GET', 'POST'])
def companyID(id_company):
	return company.companyID(id_company)

@app.route("/company/<string:id_company>/numberDocument/<string:id_number>/", methods=['GET'])
def numberDocumentsId(id_company, id_number):
	return numberDocument.numberDocumentsId(id)

@app.route("/company/<string:id_company>/numberDocument/register/", methods=['GET', 'POST'])
def addNumberDocument(id_company):
	number = request.form.get('number-document')
	return numberDocument.addNumberDocument(number, id_company)

@app.route("/company/<string:id>/key/register/", methods=['GET', 'POST'])
def addKey(id):
	month_min = None
	month_max = None
	year_min = None
	year_max = None
	model = None
	issue = None
	serie_min = None
	serie_max = None
	state = None
	number_inicial = None

	month_min = request.form.get('select-month-min')
	month_max = request.form.get('select-month-max')
	year_min = request.form.get('select-year-min')
	year_max = request.form.get('select-year-max')
	model = request.form.get('select-model')
	issue = request.form.get('select-issue')
	serie_min = request.form.get('select-serie-min')
	serie_max = request.form.get('select-serie-max')
	state = request.form.get('select-uf')
	number_inicial = request.form.get('number-inicial')
	
	return key.addKeys(id, month_min, month_max, year_min, year_max, model, issue, serie_min, serie_max, state, number_inicial)