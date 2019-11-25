from app import app
from flask import render_template
from pygments import highlight, lexers, formatters
import json
from app.response import *
from app.forms import Form

menu = [
	{'name': 'Home', 'route': 'index' }, 
	{'name': 'Chaves Livres', 'route': 'free' }, 
	{'name': 'Chaves em Uso', 'route': 'using' }, 
	{'name': 'Chaves Utilizadas', 'route': 'ok' }, 
	{'name': 'Empresas', 'route': 'companies' }]
		
legend = {'title_1': 'Identificador', 'title_2':'Status'}

@app.route("/")
def index():
	form = Form()
	return render_template('template.html', menus=menu, title="Home", form=form)

@app.route("/key/free")
def free():
	_keys = getFree()
	if _keys.ok:
		return render_template('list.html', menus=menu, title="Chaves Livres", table=legend, keys=_keys.json())
	return err(_keys.status_code)

@app.route("/key/using")
def using():
	_keys = getUsing()
	if _keys.ok:
		return render_template('list.html', menus=menu, title="Chaves em Uso", table=legend, keys=_keys.json())
	return err(_keys.status_code)

@app.route("/key/ok")
def ok():
	_keys = getOk()
	if _keys.ok:
		return render_template('list.html', menus=menu, title="Chaves Utilizadas", table=legend, keys=_keys.json())
	return err(_keys.status_code)

@app.route("/companies")
def companies():
	companies = getCompanies()
	if companies.ok:
		return render_template('list.html', menus=menu, title="Empresas", table=legend, keys=companies.json())
	return err(companies.status_code)

def err(status_code):
	if status_code == 400:
		return render_template('err.html', code=" 400 -  Sintaxe inválida. ")
	if status_code == 404:
		return render_template('err.html', code=" 404 -  O servidor não pode encontrar o recurso solicitado. ")
	if status_code == 406:
		return render_template('err.html', code=" 406 -  Valor inválido. ")
	if status_code == 500:
		return render_template('err.html', code=" 500 -  Erro interno do servidor. ")
	else:
		return render_template('err.html', code=" Erro não detectado. ")