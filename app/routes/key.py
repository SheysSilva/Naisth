from flask import render_template, redirect, url_for
from app.routes.util import *
from app.response import *
from app.routes import generateKey


def addKeys(cnpj, month_min, month_max, year_min, year_max, model, issue, serie_min, serie_max, state):
	if isNull(cnpj) or isNull(year_min) or isNull(year_max) or isNull(month_min) or isNull(month_max) or isNull(model) or isNull(issue) or isNull(serie_min) or isNull(serie_max) or isNull(state):
		return render_template('key/register.html', menus=menu, title="Cadastrar", months=months, years=years, models=models, issues=issues, series=series, ufs=ufs)
	else:
		if int(month_min) > int(month_max) or int(year_min) > int(year_max) or int(serie_min) > int(serie_max):
			return err(406)

		numbers = getNumberDocumentsCompanyId(cnpj)

		if numbers.ok:
			for number in numbers.json():
				for year in range(int(year_min), int(year_max)+1):
					for month in range(int(month_min), int(month_max)+1):
						for serie in range(int(serie_min), int(serie_max)+1):
							key = generateKey.generate(state, year, month, cnpj, model, serie, number['id'], issue)
							postKey(key, state, str(year)[2:4], month, model, serie, issue, number['id'], cnpj)
		
		return render_template('key/register.html', menus=menu, title="Cadastrar", months=months, years=years, models=models, issues=issues, series=series, ufs=ufs)
	return render_template('key/register.html', menus=menu, title="Cadastrar", months=months, years=years, models=models, issues=issues, series=series, ufs=ufs)
