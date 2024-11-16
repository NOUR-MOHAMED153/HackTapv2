import tkinter as tk
import sys
import os
from datetime import datetime
import win32api as win
from win10toast import ToastNotifier


dt=datetime.now()
current_year=dt.year
current_month=dt.month
current_day=dt.day

def inst_butn():
    inst_window= tk.Toplevel()
    inst_window.configure(bg="#181818")
    inst_window.geometry('600x450+450+180')
    inst_window.resizable(False,False)
    inst_window.title(' تعليمات المستخدم ')
    inst_txt="""
    : قبل استخدام البرنامج برجاء اتباع التعليمات الاتية 

    تثبيت برنامج تعريفات سامسونج المرفق مع الملف المضغوط -1

    2- ولطريقة التفعيل يوجد فيديو مرفق مع الملف المضغوط samfwtool تفعيل برنامج

    3- التأكد من جميع الادوات في ملف توولز تعمل بشكل صحيح

    4- طريقة التعامل مع البرنامج يوجد لها ايضا فيديو مرفق

    5- لخروج التابلت خارج المنظومة نهائيا يتطلب الاتصال بالانترنت 

    6- ايقاف تشغيل برنامج الحماية اذا كان يتدخل في التشغيل

    6- اذا واجهتك اي مشكلة برجاء التواصل مع المطور عن طريق : +201140622391
    """
    label= tk.Label(inst_window,text=inst_txt,bg="#181818",fg="white")
    label.pack(pady=50)
def about_butn():
    about_window= tk.Toplevel()
    about_window.configure(bg="#181818")
    about_window.geometry('450x300+450+180')
    about_window.resizable(False,False)
    about_window.title(' عن المطور ')
    inst_txt="""
    تم تطوير هذا البرنامج عن طريق المطور نور محمد -
    وهو مجاني بالكامل وغير مسموح بالتلاعب بمصدر الكود 

    وهو مطور لكي يجمع لك ادوات خروج التابلت من المنظومة -
    ولتسهيل هذه العملية علي المستخدم 

    للتواصل والاستفسارات برجاء التواصل واتس اب 
    +عن طريق : 201140622391

    
    
    جميع الحقوق محفوظة @2025
    """
    label= tk.Label(about_window,text=inst_txt,bg="#181818",fg="white")
    label.pack(pady=50)
def exit_butn():
    sys.exit(0)
    reset_time_method()
def open_file(path):
    os.system(f"start {path}")
def open_AndroidUtility():
    open_file(r"Tools\AndroidUtility\AndroidUtility.exe")
    show_notfiy("T505N Hack by Nour",'AndroidUtility opend succesfully!')
def original_change_time_method(year,month,day):
    dt=datetime.now()
    hour=dt.hour-3
    minute=dt.minute
    second=dt.second
    milleseccond=dt.microsecond//1000
    dow=dt.isoweekday()
    win.SetSystemTime(year,month,dow,day,hour,minute,second,milleseccond)
def change_time_method():
    original_change_time_method(2023,7,15)
    show_notfiy("T505N Hack by Nour",'Time changed succesfully!')
def reset_time_method():
    original_change_time_method(current_year,current_month,current_day)
    show_notfiy("T505N Hack by Nour",'Time reset succesfully!')
def qr_method():
    open_file(r"Tools\QR.jpg")
    show_notfiy("T505N Hack by Nour",'QR Code opend succesfully!')
def show_notfiy(title,msg):
    toaster = ToastNotifier()
    toaster.show_toast(title,msg,icon_path=r'Photos\logo.ico',duration=5,threaded=True)
