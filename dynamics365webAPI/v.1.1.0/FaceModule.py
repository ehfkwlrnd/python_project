import requests, json

class FaceAPI:
    def __init__(self, key, endPoint):
        self.key = key
        self.endPoint = endPoint

    def Detect(self, imgPath):
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self.key,
        }

        params = 'returnFaceId=true&returnFaceAttributes=age,gender'
        url = self.endPoint + '/detect?' + params
        response = requests.post(url, open(imgPath, 'rb').read(), headers=headers).json()
        if len(response) == 0:
            raise Exception('Face was not detected')
        if len(response) > 1:
            raise Exception('More than one face was detected')
        return response[0]

    def DetectMulti(self, imgPath):
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self.key,
        }
        params = 'returnFaceId=true&returnFaceAttributes=age,gender'
        url = self.endPoint + '/detect?' + params
        response = requests.post(url, open(imgPath, 'rb').read(), headers=headers).json()
        if len(response) == 0:
            raise Exception('Face was not detected')
        return response

    def GetGroupInfo(self, groupName):
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }

        params = 'returnRecognitionModel=true'
        url = self.endPoint + '/persongroups/' + groupName + '?' + params
        response = requests.get(url, headers=headers).json()
        return response

    def GetPerson(self, groupId, personId):
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = url = self.endPoint + '/persongroups/' + groupId + '/persons/' + personId
        response = requests.get(url, headers=headers).json()
        return response

    def GetPersonByName(self, groupId, personName):
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/persongroups/' + groupId + '/persons?'
        response = requests.get(url, headers=headers).json()
        if type(response) == dict:
            return response
        personList = [person for person in response if person.get('name') == personName]
        if len(personList) == 0:
            return {'error':{'code':'NotFoundPerson'}}
        return personList[0]

    def GetPersonList(self, groupId):
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/persongroups/' + groupId + '/persons?'
        response = requests.get(url, headers=headers).json()
        if type(response) == dict:
            return response
        return [e.get('name') for e in response]

    def GetGroupList(self):
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/persongroups/'
        response = requests.get(url, headers=headers).json()
        if type(response) == dict:
            return response
        return [e.get('personGroupId') for e in response]

    def Training(self, groupId):
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/persongroups/' + groupId + '/train?'
        response = requests.post(url, headers=headers)
        return response

    def Identify(self, groupId, imgPath):
        faceId = self.Detect(imgPath).get('faceId')
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/identify?'
        response = requests.post(url, data='{ "personGroupId": "' + groupId + '",\
                                                "faceIds": ["' + faceId + '"],\
                                                "maxNumOfCandidatesReturned": 1,"confidenceThreshold": 0.5}', headers=headers).json()
        if type(response) == dict:
            raise Exception(str(response))
        candidates = response[0].get('candidates')
        if len(candidates) == 0:
            raise Exception(str({'error':{'code' : 'NotFoundCandidates'}}))
        return candidates[0]

    def IdentifyMulti(self, groupId, imgPath):
        persons = self.DetectMulti(imgPath)
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/identify?'
        candidateList = []
        for person in persons:
            faceId = person.get('faceId')
            response = requests.post(url, data='{ "personGroupId": "' + groupId + '",\
                                                    "faceIds": ["' + faceId + '"],\
                                                    "maxNumOfCandidatesReturned": 1,"confidenceThreshold": 0.5}', headers=headers).json()
            if type(response) == dict:
                candidateList.append(response)
            else:
                candidates = response[0].get('candidates')
                if len(candidates) == 0:
                    candidateList.append({'error':{'code' : 'NotFoundCandidates'}})
                else:
                    candidateList.append(candidates[0])
        return candidateList
        
    def CreateGroup(self, groupId, groupName):
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/persongroups/' + groupId + '?'
        response = requests.put(url, data='{ "name": "' + groupName + '" }', headers=headers).json
        return response

    def CreatePerson(self, groupId, personName, userData=''):
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/persongroups/' + groupId + '/persons?'
        data = {'name' : personName, 'userData' : userData }
        response = requests.post(url, data=str(data), headers=headers).json()
        return response

    def DeleteGroup(self, groupId):
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/persongroups/' + groupId
        response = requests.delete(url, headers=headers)
        return response

    def DeletePerson(self, groupId, personId):
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/persongroups/' + groupId + '/persons/' + personId
        response = requests.delete(url, headers=headers)
        return response

    def UpdatePerson(self, groupId, personId, userData):
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/persongroups/' + groupId + '/persons/' + personId
        data = { 'userData' : userData }
        response = requests.patch(url, data=str(data), headers=headers)
        return response

    def AddFace(self, groupId, personId, imgPath):
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self.key,
        }
        url = self.endPoint + '/persongroups/' + groupId + '/persons/' + personId + '/persistedFaces?'
        response = requests.post(url, data=open(imgPath, 'rb').read(), headers=headers)
        return response

    
##class Person:
##    def __init__(self, groupId, personName):
##        self.groupId = groupId
##        self.personName = personName
##
##        self.me = GetPersonByName(groupId, personName)
##        if self.me.get('error') != None:
##            raise Exception(self.me.get('error').get('code'))
##        print(self.me)
##
##    def AddFace(self, imgPath):
##        headers = {
##            'Content-Type': 'application/octet-stream',
##            'Ocp-Apim-Subscription-Key': key,
##        }
##        url = endPoint + '/persongroups/' + self.groupId + '/persons/' + self.me.get('personId') + '/persistedFaces?'
##        response = requests.post(url, data=open(imgPath, 'rb').read(), headers=headers)
##        return response

    
