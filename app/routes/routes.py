from app import app
from flask import render_template, redirect, url_for
from pygments import highlight, lexers, formatters
import json
from app.response import *
from app.routes import company
from app.routes import numberDocument
from app.routes import key
from app.routes.util import *

@app.route("/", methods=['GET'])
def index():
	return render_template('home.html', menus=menu, title="Home")

@app.route("/company", methods=['GET'])
def companies():
	return company.companies()

@app.route("/company/register", methods=['GET', 'POST'])
def addCompany():
	cnpj = request.form.get('cnpj-company')
	name = request.form.get('name-company')
	print(cnpj)
	print(name)
	return company.addCompany(cnpj, name)

@app.route("/company/<string:id>", methods=['GET', 'POST'])
def numberDocuments(id):
	return numberDocument.numberDocuments(id)

@app.route("/numberDocument/<string:id>", methods=['GET'])
def numberDocumentsId(id):
	return numberDocument.numberDocumentsId(id)

@app.route("/company/<string:id>/numberDocument/register", methods=['GET', 'POST'])
def addNumberDocument(id):
	number = request.form.get('number-document')
	return numberDocument.addNumberDocument(number, id)

@app.route("/company/<string:id>/key/register", methods=['GET', 'POST'])
def addKey(id):
	return key.addKeys(id)

@app.route("/list", methods=['GET', 'POST'])
def list():
	select = request.args.get('select')
	if select=='Chaves Livres':
		return company.free()
	if select=='Chaves em Uso':
		return company.using()
	if select=='Chaves Utilizadas':
		return company.ok()
	if select=='Empresas':
		return company.companies()
	return company.companies()
