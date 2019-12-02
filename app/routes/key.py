from flask import render_template, redirect, url_for
from app.routes.util import *
from app.response import *

def addKeys(cnpj):
	month_min = request.args.get('select-month-min')
	month_max = request.args.get('select-month-max')
	year_min = request.args.get('select-year-max')
	year_max = request.args.get('select-year-max')
	model = request.args.get('select-model')
	serie = request.args.get('select-issue')
	serie = request.args.get('select-serie')
	uf = request.args.get('select-uf')

	if request.method == 'POST' and (int(month_min) > int(month_max) or int(year_min) > int(year_max)):
		return err(406)

	return render_template('company/key/register.html', menus=menu, title="Cadastrar", months=months, years=years, models=models, issues=issues, series=series, ufs=ufs)
