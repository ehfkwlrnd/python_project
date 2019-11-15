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
                    groupId = input('groupId : ')
                    personName = input('personName : ')
                    r = fm.GetPersonByName(groupId, personName)
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
                    groupId = input('groupId : ')
                    groupName = input('groupName : ')
                    r = fm.CreateGroup(groupId, groupName)
                    print(r)

                # DeleteGroup
                elif work == 3:
                    print('select : DeleteGroup')
                    groupId = input('groupId : ')
                    r = fm.DeleteGroup(groupId)
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
                    personName = input('personName : ')
                    r = fm.GetPersonByName(groupId, personName)
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
                    print('select : CreatePerson & AddFace')
                    personName = input('personName : ')
                    password = getpass('password : ')
                    flowName = input('flowName : ')
                    personData = aes.encrypt(f'{{ "password" : "{password}", "flowname" : "{flowName}" }}')
                    r = fm.CreatePerson(groupId, personName, personData)
                    print(r)

                # CreatePerson & AddFace
                elif work == 3:
                    print('select : CreatePerson & AddFace')
                    personName = input('personName : ')
                    password = getpass('password : ')
                    flowName = input('flowName : ')
                    personData = aes.encrypt(f'{{ "password" : "{password}", "flowname" : "{flowName}" }}')
                    r = fm.CreatePerson(groupId, personName, personData)
                    print(r)

                    Tk().withdraw()
                    imgPath = tkdlg.askopenfilename()
                    
                    personId = r.get('personId')
                    r = fm.AddFace(groupId, personId, imgPath)
                    print(r)

                # DeletePerson
                elif work == 4:
                    print('select : DeletePerson')
                    personName = input('personName : ')
                    r = fm.GetPersonByName(groupId, personName)
                    personId = r.get('personId')
                    r = fm.DeletePerson(groupId, personId)
                    print(r)

                # UpdatePerson
                elif work == 5:
                    print('select : UpdatePerson')
                    personName = input('personName : ')
                    password = getpass('password : ')
                    flowName = input('flowName : ')
                    personData = aes.encrypt(f'{{ "password" : "{password}", "flowname" : "{flowName}" }}')
                    r = fm.GetPersonByName(groupId, personName)
                    personId = r.get('personId')
                    r = fm.UpdatePerson(groupId, personId, personData)
                    print(r.text)

                # AddFace
                elif work == 6:
                    print('select : AddFace')
                    personName = input('personName : ')
                    Tk().withdraw()
                    imgPath = tkdlg.askopenfilename()
                    r = fm.GetPersonByName(groupId, personName)
                    personId = r.get('personId')
                    r = fm.AddFace(groupId, personId, imgPath)
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
                    imgPath = tkdlg.askopenfilename()
                    r = fm.Identify(groupId, imgPath)
                    print(r)
                    personId = r.get('personId')
                    r = fm.GetPerson(groupId, personId)
                    print(r)
                    personData = json.loads(aes.decrypt(r.get('userData')))
                    print(personData.get('password'))
                    print(personData.get('flowname'))
            
            except Exception as e:
                print(e)
    
