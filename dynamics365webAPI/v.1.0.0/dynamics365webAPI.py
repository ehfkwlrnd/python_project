import requests
import json

class D365():
    def __init__(self, crmOrg, clientId, tenantId, userName, userPassword):
        self.crmOrg = crmOrg
        self.userName = userName
        self.apiEndPoint = crmOrg + '/api/data/v9.0'
        
        tokenEndPoint = 'https://login.microsoftonline.com/' + tenantId + '/oauth2/token'
        tokenPost = {
            'client_id':clientId,
            'resource':crmOrg,
            'username':userName,
            'password':userPassword,
            'grant_type':'password'
        }
        tokenRes = requests.post(tokenEndPoint, data=tokenPost)
        accessToken = tokenRes.json().get('access_token')
        if tokenRes == None:
            raise Exception("Couldn't get accessToken")
        self.headers = {
            'Authorization': 'Bearer ' + accessToken,
            'OData-MaxVersion': '4.0',
            'OData-Version': '4.0',
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8',
            'Prefer': 'odata.maxpagesize=500',
            'Prefer': 'odata.include-annotations=OData.Community.Display.V1.FormattedValue'
        }

    def getRecord(self, query):
        crmRes = requests.get(self.apiEndPoint+query, headers=self.headers).json().get('value')
        return crmRes

    def createRecord(self, query, data):
        crmRes = requests.post(self.apiEndPoint + query, data=str(data), headers=self.headers)
        return crmRes

    def updateRecord(self, query, data):
        crmRes = requests.patch(self.apiEndPoint + query, data=str(data), headers=self.headers)
        return crmRes

    def deleteRecord(self, query):
        crmRes = requests.delete(self.apiEndPoint + query, headers=self.headers)
        return crmRes
