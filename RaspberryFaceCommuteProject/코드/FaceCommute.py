#_*_ coding:utf-8
#FaceAPI, D365API이용을 위한 커스텀 라이브러리
from FaceModule import FaceAPI
from dynamics365webAPI import D365
#AES암호화를 위한 커스텀 라이브러리
import aes
#라즈베리 파이 기기 제어를 위한 모듈
from picamera import PiCamera
#GUI 핸들링을 위한 tkinter 모듈
from Tkinter import *
import tkFont
#기본 모듈
from datetime import datetime
from time import sleep
import json
import sys
import traceback

groupId = ''
#Azure FaceAPI
key = ''
endPoint = ''
fm = FaceAPI(key, endPoint)
#Dynamics365 WebAPI
crmOrg = ''
clientId = ''
tenantId = ''

#Tkinter 윈도우 창
root = Tk()
root.title('IoT for Raspberry Pi 출근/퇴근')
root.attributes('-fullscreen', True)
menubar = Menu(root, background='#000099', foreground='white',
               activebackground='#004c99', activeforeground='white')
filemenu = Menu(menubar, tearoff=0, background='#000099',
foreground='white',
                activebackground='#004c99', activeforeground='white')
menubar.add_cascade(label="사용자 대기 중 입니다. 카메라를 실행하여 주세요.")
root.config(bg='#2A2C2B', menu=menubar, cursor='none')

# 전역 변수
msg = ''
cam = PiCamera()

def UpdateClock():
    clock.configure(text=datetime.now().strftime('%H:%M:%S'))
    root.after(1000, UpdateClock)

def DefaultSet():
    start_btn.place(relx=0.5, rely=0.9, anchor=CENTER)
    label.configure(text='대기중..')

def AnalyzeState():
    label.configure(text='분석중..')
    identify_btn.place_forget()
    root.after(1, IdentifyClick)

def StartClick():
    start_btn.place_forget()
    identify_btn.place(relx=0.5, rely=0.9, anchor=CENTER)
    cam.rotation = 180
    cam.brightness = 50
    cam.start_preview(fullscreen=False, window=(100,60,600,300))
    

def IdentifyClick():
    msg = u''
    wait = 0
    now = datetime.now()
    try:
        cam.capture('image01.jpg')
        cam.stop_preview()
        
        candidateList = fm.IdentifyMulti(groupId, 'image01.jpg')

        for r in candidateList:
            wait += 1
            try:
                #d365 시스템 사용자인지 확인
                personId = r.get('personId') #personId
                r = fm.GetPerson(groupId, personId)
                userName = r.get('name') #userName (d365 ID)
                userData = json.loads(r.get('userData'))
                userPassword = aes.decrypt(userData.get('password')) #userPassword (d365 PW)
                flowName = userData.get('flowname')
                d365 = D365(crmOrg, clientId, tenantId, userName, userPassword)
                query = "/systemusers?$select=domainname&$filter=domainname eq '" + userName + "'"
                crmRes = d365.getRecord(query)
                if len(crmRes) == 0:
                    raise Exception('You are not a member of organization')

                #출근부 엔티티에서 식별된 사람계정으로 오늘짜 생성된 레코드 가져옴 
                ownerId = crmRes[0].get('ownerid')
                query = "/iui_commutes?$orderby=createdon%20desc&$top=1&$filter=_ownerid_value eq '" + str(ownerId) +\
                                                                                        "'and createdon ge " +\
                                                                                        now.strftime('%Y-%m-%d')
                crmRes = d365.getRecord(query)

                #레코드가 없으면 출근, 있으면 퇴근, 출근이면 시간확인해서 정시, 지각 판별 
                query = '/iui_commutes?'
                iui_inout = 0 if len(crmRes)==0 else 1
                iui_checktime = 0 if iui_inout==1 or now.hour*60+now.minute <= 9*60+10 else 1
                data = { 'iui_inout' : iui_inout, 'iui_checktime' : iui_checktime, 'iui_flowname' : flowName }
                crmRes = d365.createRecord(query, data)
                
                msg += flowName
                if iui_inout == 0:
                    msg += (u' 정시' if iui_checktime==0 else u' 지각') + u' 출근 하셨습니다.'
                else:
                    msg += u' 퇴근 하셨습니다.'
                msg += u'\n'
            
            except:
                with open('log.txt', 'a') as f:
                    traceback.print_exc(file=f)
        
    except Exception as e:
        msg += str(e) + '\n'
        with open('log.txt', 'a') as f:
            traceback.print_exc(file=f)

    except:
        msg += 'Unexpected Error\n'
        with open('log.txt', 'a') as f:
            traceback.print_exc(file=f)

    finally:
        label.configure(text=msg)
        root.after(2000 + wait*1000, DefaultSet)

#메세지창(label), 시간표시창(label)과  버튼들(button)
font = tkFont.Font(size=20)

label = Label(root, text='대기중..', fg='white', bg='#2A2C2B', font=font)
label.place(relx=0.5, rely=0.1, anchor=CENTER)

clock = Label(root, text='', fg='white', bg='#2A2C2B', font=font)
clock.place(relx=0.5, rely=0.3, anchor=CENTER)
    
start_btn = Button(root, text='카메라 실행', width=15, height=3, command=StartClick, fg='white', bg='#2A2C2B', font=font)
start_btn.place(relx=0.5, rely=0.9, anchor=CENTER)

identify_btn = Button(root, text='촬영', width=15, height=3, command=AnalyzeState, fg='white', bg='#2A2C2B', font=font)

root.after(1000, UpdateClock)
root.mainloop()
cam.close()
