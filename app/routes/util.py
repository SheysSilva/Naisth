from flask import render_template, redirect, url_for
from datetime import datetime
now = datetime.now()

menu = [
	{'name': 'Home', 'route': 'index' }, 
	{'name' : 'Empresa', 'route': 'companies'}]
		
legend = {'title_1': 'Identificador', 'title_2':'Status'}
legend_company ={'title_1': 'Nome', 'title_2':'CNPJ', 'title_3': 'Status'}

options = [
	{'name': 'Chaves Livres'}, 
	{'name': 'Chaves em Uso'}, 
	{'name': 'Chaves Utilizadas'}, 
	{'name': 'Empresas'}]

years = range(1989, int(now.year)+1)

months_model = [
	{'name': 'Janeiro', 'value' : '01'},
	{'name': 'Fevereiro', 'value' : '02'},
	{'name': 'Março', 'value' : '03'},
	{'name': 'Abril', 'value' : '04'},
	{'name': 'Maio', 'value' : '05'},
	{'name': 'Junho', 'value' : '06'},
	{'name': 'Julho', 'value' : '07'},
	{'name': 'Agosto', 'value' : '08'},
	{'name': 'Setembro', 'value' : '09'},
	{'name': 'Outubro', 'value' : '10'},
	{'name': 'Novembro', 'value' : '11'},
	{'name': 'Dezembro', 'value' : '12'}
]

random = [
	{'name': 'COD 001', 'value' : '001'},
	{'name': 'COD 002', 'value' : '002'},
	{'name': 'COD 003', 'value' : '003'},
]

models = [
	{'name': 'NFE', 'value': 55},
	{'name': 'NFCE', 'value': 65},
	{'name': 'CTE', 'value': 57}
]

issues = [
	{'name': 'normal', 'value': 1}, 
	{'name': 'contingencia 1', 'value': 2},
	{'name': 'contingencia 2', 'value': 3}
]

series = [105, 106, 124, 125]

ufs = [
	{'name':'PB', 'value': 25}
]

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

def isNull(a):
	a = str(a)
	if not a or not a.strip() or a == 'None':
		return True
	return False