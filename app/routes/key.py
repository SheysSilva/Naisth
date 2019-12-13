from flask import render_template, redirect, url_for
from app.routes.util import *
from app.response import *
from app.routes import generateKey
import json

def addKeys(cnpj, month_min, month_max, year_min, year_max, model, issue, serie_min, serie_max, state, inicial):
	if isNull(cnpj) or isNull(year_min) or isNull(year_max) or isNull(month_min) or isNull(month_max) or isNull(model) or isNull(issue) or isNull(serie_min) or isNull(serie_max) or isNull(state):
		return render_template('key/register.html', menus=menu, title="Cadastrar", months=months_model, years=years, models=models, issues=issues, series=series, ufs=ufs)	
		
	if int(month_min) > int(month_max) or int(year_min) > int(year_max) or int(serie_min) > int(serie_max):
		return err(406)

	if not inicial:
		inicial = 1

	for month in range(int(month_min), int(month_max)+1):
		for year in range(int(year_min), int(year_max)+1):
			for serie in range(int(serie_min), int(serie_max)+1):
				postMonth(month, year, serie, model, issue, state,  1, cnpj)

	createKey(cnpj)

		
	return render_template('key/register.html', menus=menu, title="Cadastrar", months=months_model, years=years, models=models, issues=issues, series=series, ufs=ufs)	

def createKey(cnpj):
	month = getMonthCompany(cnpj)
	if not month:
		print("SEM RETORNO")
	else:
		month=month.json()
		month=month[0]
		inicial=month['inicial']
		fin = inicial
		while fin <= (inicial+1000):
			fin+=64
			for number in range(inicial, fin):
				key = generateKey.generate(month['state'], month['year'], month['id'], cnpj, month['model'], month['serie'], number, month['issue'])
				postKey(key, month['state'], str(month['year'])[2:4], month['id'], month['model'], month['serie'], month['issue'], number, cnpj)
		

