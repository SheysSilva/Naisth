from flask import request
import requests

url = 'localhost'
port = '8081'

companies='/companies'
numberDocuments='/numberDocuments'
keys = '/keys'

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

def getKeys(id_company):
	get = requests.get('http://'+url+':'+port+companies+"/"+str(id_company)+keys)
	return get.json()

def getKeyId(id):
	get = requests.get('http://'+url+':'+port+keys+"/"+srt(id))
	return get.json()

def postKey(id, state, year, month, model, serie, issue, numberDocumentId, id_company):
	post = requests.post('http://'+url+':'+port+companies+'/'+str(id_company)+numberDocuments+'/'+str(numberDocumentId)+keys, 
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

def getNumberDocumentsCompanyId(id_company):
	get = requests.get('http://'+url+':'+port+companies+"/"+str(id_company)+numberDocuments)
	return get

def postNumberDocument(id, id_company):
	post = requests.post('http://'+url+':'+port+companies+"/"+str(id_company)+numberDocuments, data={'id': str(id)})
	return post


