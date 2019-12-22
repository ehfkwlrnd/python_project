# -*- coding: utf-8 -*-

from FaceModule import FaceAPI
from tkinter import Tk
import tkinter.filedialog as tkdlg
import aes
import json
from getpass import getpass

key = ''
endPoint = ''
fm = FaceAPI(key, endPoint)
done = True

while done:
    
        while done:
            try:
                print('****GroupWork*****')
                print('0. GetPerson')
                print('1. GroupList')
                print('2. CreateGroup')
                print('3. DeleteGroup')
                print('4. PersonWork')
                print('-1 : exit')
                print('******************')

                work = int(input('work : '))
                if work == -1:
                    done = False

                # GetPerson
                elif work == 0:
                    print('select : GetPerson')
                    r = fm.GetPersonByName(input('groupId : '), input('personName : '))
                    print(r)

                # GroupList
                elif work == 1:
                    print('select : GroupList')
                    groupList = fm.GetGroupList()
                    print('===Group List===')
                    for group in groupList:
                        print('groupId :', group)
                    print('=================')

                # CreateGroup
                elif work == 2:
                    print('select : CreateGroup')
                    r = fm.CreateGroup(input('groupId : '), input('groupName : '))
                    print(r)

                # DeleteGroup
                elif work == 3:
                    print('select : DeleteGroup')
                    r = fm.DeleteGroup(input('groupId : '))
                    print(r)

                # PersonWork
                elif work == 4:
                    print('select : GroupWork')
                    groupId = input('groupId : ')
                    break
            
            except Exception as e:
                print(e)

    
        while done:
            try:
                print('****PersonWork****')
                print('0. GetPerson')
                print('1. PersonList')
                print('2. CreatePerson')
                print('3. CreatePerson & AddFace')
                print('4. DeletePerson')
                print('5. UpdatePerson')
                print('6. AddFace')
                print('7. Training')
                print('8. Identify')
                print('-1 : back')
                print('******************')

                work = int(input('work : '))
                if work == -1:
                    break
                
                # GetPerson
                elif work == 0:
                    print('select : GetPerson')
                    r = fm.GetPersonByName(groupId, input('personName : '))
                    print(r)

                # PersonList
                elif work == 1:
                    print('select : PersonList')
                    personList = fm.GetPersonList(groupId)
                    print('===Person List===')
                    for person in personList:
                        print('personName :', person)
                    print('=================')

                # CreatePerson
                elif work == 2:
                    print('select : CreatePerson')
                    r = fm.CreatePerson(groupId,
                                        personName=input('personName : '),
                                        userData=json.dumps({'password' : aes.encrypt(getpass('password : ')),
                                                               'flowname' : input('flowName : ')}))
                    print(r)

                # CreatePerson & AddFace
                elif work == 3:
                    print('select : CreatePerson & AddFace')
                    r = fm.CreatePerson(groupId,
                                        personName=input('personName : '),
                                        userData=json.dumps({'password' : aes.encrypt(getpass('password : ')),
                                                               'flowname' : input('flowName : ')}))
                    print(r)

                    Tk().withdraw()
                    
                    r = fm.AddFace(groupId, r.get('personId'), imgPath=tkdlg.askopenfilename())
                    print(r)

                # DeletePerson
                elif work == 4:
                    print('select : DeletePerson')
                    r = fm.GetPersonByName(groupId, input('personName : '))
                    r = fm.DeletePerson(groupId, r.get('personId'))
                    print(r)

                # UpdatePerson
                elif work == 5:
                    print('select : UpdatePerson')
                    r = fm.GetPersonByName(groupId, personName=input('personName : '))
                    r = fm.UpdatePerson(groupId, r.get('personId'),
                                        userData=json.dumps({'password' : aes.encrypt(getpass('password : ')),
                                                               'flowname' : input('flowName : ')}))
                    print(r)

                # AddFace
                elif work == 6:
                    print('select : AddFace')
                    r = fm.GetPersonByName(groupId, input('personName : '))
                    Tk().withdraw()
                    r = fm.AddFace(groupId, r.get('personId'), imgPath=tkdlg.askopenfilename())
                    print(r)

                # Training
                elif work == 7:
                    print('select : Training')
                    r = fm.Training(groupId)
                    print(r)

                # Identify
                elif work == 8:
                    print('select : Identify')
                    Tk().withdraw()
                    r = fm.Identify(groupId, imgPath=tkdlg.askopenfilename())
                    print(r)
                    r = fm.GetPerson(groupId, r.get('personId'))
                    print(r)
                    userData = json.loads(r.get('userData'))
                    print(aes.decrypt(userData.get('password')))
                    print(userData.get('flowname'))
            
            except Exception as e:
                print(e)
    
