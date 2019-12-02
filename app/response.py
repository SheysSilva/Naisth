from flask import request
import requests

url = 'localhost'
port = '8080'

companies='/companies/'
numberDocuments='/numberDocuments/'
relationships='/relationships/'
keys = '/keys/'

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

def getKeys():
	get = requests.get('http://'+url+':'+port+keys)
	return get.json()

def getKeyId(id):
	get = requests.get('http://'+url+':'+port+keys+srt(id))
	return get.json()

def postKey(id):
	post = requests.post('http://'+url+':'+port+keys, data={'id': str(id)})
	return post.json()

def putKey(id, status):
	put = requests.put('http://'+url+':'+port+keys, data={'id': str(id), 'status': str(status)})
	return put.json()

def deleteKeys():
	delete = requests.delete('http://'+url+':'+port+keys)
	return delete.json()

def deleteKeyId(id):
	delete = requests.delete('http://'+url+':'+port+keys, data={'id': str(id)})
	returndelete.json()

def getCompanies():
	get = requests.get('http://'+url+':'+port+companies)
	return get

def postCompany(id, name):
	post = requests.post('http://'+url+':'+port+companies, data={'id': str(id), 'name': str(name)})
	return post

def getNumberDocumentsCompanyId(id_company):
	get = requests.get('http://'+url+':'+port+numberDocuments, data={'id_company': str(id_company)})
	return get

def postNumberDocument(id, id_company):
	post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': str(id), 'id_company': str(id_company)})
	return post


