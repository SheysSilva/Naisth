from flask import request
import requests

url = 'localhost'
port = '8081'

companies='/companies'
keys = '/keys'
months = '/months'


def setUrl(url_):
	global url
	url = url_

def getUrl():
	return url

def getFree():
	get = requests.get('http://'+url+':'+port+'/free/')
	return get

def getUsing():
	get = requests.get('http://'+url+':'+port+'/using/')
	return get

def getOk():
	get = requests.get('http://'+url+':'+port+'/ok/')
	return get

def setStatus(id, status):
	sett = requests.get('http://'+url+':'+port+'/set/')
	return sett.json()

def getkeysFree():
	get = requests.get('http://'+url+':'+port+keys)
	return get

def getKeys(id_company):
	get = requests.get('http://'+url+':'+port+companies+"/"+str(id_company)+keys)
	return get.json()

def getKeyId(id):
	get = requests.get('http://'+url+':'+port+keys+"/"+srt(id))
	return get.json()

def postKey(id, state, year, month, model, serie, issue, numberDocumentId, id_company):
	post = requests.post('http://'+url+':'+port+companies+'/'+str(id_company)+keys, 
		data={
			'id': str(id), 
			'state': str(state), 
			'year': str(year), 
			'month': str(month), 
			'model': str(model), 
			'serie': str(serie), 
			'issue': str(issue)
		})
	return post.json()

def putKey(id, status):
	put = requests.put('http://'+url+':'+port+keys, data={'id': str(id), 'status': str(status)})
	return put.json()

def deleteKeys():
	delete = requests.delete('http://'+url+':'+port+keys)
	return delete.json()

def deleteKeyId(id):
	delete = requests.delete('http://'+url+':'+port+keys, data={'id': str(id)})
	return delete.json()

def getCompanies():
	get = requests.get('http://'+url+':'+port+companies)
	return get

def getCompanyId(id):
	get = requests.get('http://'+url+':'+port+companies+"/"+str(id))
	return get

def postCompany(id, name, random):
	post = requests.post('http://'+url+':'+port+companies, data={'id': str(id), 'name': str(name), 'random': str(random)})
	return post

def getMonths():
	get = requests.get('http://'+url+':'+port+months)
	return get

def getMonthsId(id_month):
	get = requests.get('http://'+url+':'+port+months+'/'+str(id_month))
	return get

def getMonthCompany(id_company):
	get = requests.get('http://'+url+':'+port+companies+'/'+str(id_company)+months)
	return get

def getMonthId(id_company, id_month):
	get = requests.get('http://'+url+':'+port+companies+'/'+str(id_company)+months+'/'+str(id_month))
	return get

def postMonth(id, year, serie, model, issue, state, inicial, id_company):
	post = requests.post('http://'+url+':'+port+companies+'/'+str(id_company)+months, data={'id': str(id), 'year': str(year), 'serie': str(serie), 'model': str(model), 'issue': str(issue), 'state': str(state), 'inicial': int(inicial)})
	return post
