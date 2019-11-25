from flask import request
import requests


url = 'localhost'
port = '8080'


def getFree():
	get = requests.get('http://'+url+':'+port+'/free/')
	return get

def getUsing():
	get = requests.get('http://'+url+':'+port+'/using/')
	return get

def getOk():
	get = requests.get('http://'+url+':'+port+'/ok/')
	return get

def getCompanies():
	get = requests.get('http://'+url+':'+port+'/companies/')
	return get





