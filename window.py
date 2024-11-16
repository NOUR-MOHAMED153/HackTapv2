import customtkinter as ctk
import PIL
from methods import *
from tkinter import StringVar
from tkinter import messagebox

def main():
    #======= main window =========
    window = ctk.CTk()
    ctk.set_appearance_mode('dark')
    window.geometry('1000x650+300+70')
    window.resizable(False,False)
    window.title(' NM-Tool T505N  v2.1')
    window.iconbitmap(r'Photos\logo.ico')

    main_frame = ctk.CTkFrame(window)
    main_frame.pack(padx=0,pady=0,fill="both",expand=True)
    #======== left section ===============
    left_frame = ctk.CTkFrame(main_frame,width=80,height=650,fg_color="#181818",corner_radius=0)
    left_frame.place(x=0,y=0)

    logo_img = PIL.Image.open(r'Photos\logo.ico')
    logo_imag = ctk.CTkImage(logo_img,size=(50,50))
    logo_image = ctk.CTkLabel(left_frame,text='',image=logo_imag)
    logo_image.place(x=15,y=20)

    home_img = PIL.Image.open(r'Photos\home.png')
    home_image = ctk.CTkImage(home_img,size=(30,30))
    home_btn = ctk.CTkButton(left_frame,
    width=20,
    height=26,
    text='',
    image=home_image,
    corner_radius=7,
    fg_color='#d3d2d5',
    cursor="hand2",
    bg_color="transparent",
    hover=True,
    hover_color='gray')
    home_btn.place(x=15,y=250)
    home_border = ctk.CTkLabel(left_frame,text="|",font=("arial",35))
    home_border.place(x=5,y=245)

    inst_img = PIL.Image.open(r'Photos\inst.png')
    inst_imag = ctk.CTkImage(inst_img,size=(33,37))
    inst_btn = ctk.CTkButton(left_frame,
    width=20,
    height=26,
    text='',
    image=inst_imag,
    corner_radius=7,
    fg_color='#d3d2d5',
    cursor="hand2",
    bg_color="transparent",
    hover=True,
    hover_color='gray',
    command=inst_butn)
    inst_btn.place(x=14,y=300)

    about_img = PIL.Image.open(r'Photos\about.png')
    about_imag = ctk.CTkImage(about_img,size=(30,35))
    about_btn = ctk.CTkButton(left_frame,
    width=20,
    height=26,
    text='',
    image=about_imag,
    corner_radius=7,
    fg_color='#d3d2d5',
    cursor="hand2",
    bg_color="transparent",
    hover=True,
    hover_color='gray',
    command=about_butn)
    about_btn.place(x=14,y=355)

    exit_img = PIL.Image.open(r'Photos\exit.png')
    exit_imag = ctk.CTkImage(exit_img,size=(25,25))
    exit_btn = ctk.CTkButton(left_frame,
    width=20,
    height=26,
    text='',
    image=exit_imag,
    corner_radius=10,
    fg_color='white',
    cursor="hand2",
    bg_color="transparent",
    hover=True,
    hover_color='gray',
    command=exit_butn)
    exit_btn.place(x=16,y=600)
    #===================== right section ==========================
    right_frame = ctk.CTkFrame(main_frame,width=920,height=650)
    right_frame.place(x=80,y=0)

    main_img = PIL.Image.open(r'Photos\bg.jpg')
    main_imag = ctk.CTkImage(main_img,size=(1000,650))
    main_image = ctk.CTkLabel(right_frame,text='',image=main_imag)
    main_image.pack()

    format_tap = ctk.CTkFrame(
    right_frame,
    width=300,
    height=270,
    fg_color="#d3d2d5",
    bg_color='#27007a',
    corner_radius=10,
    border_width=2,
    border_color="#181818")
    format_tap.place(x=30,y=50)
    format_btn = ctk.CTkButton(
    format_tap,
    width=170,
    height=50,
    cursor='hand2',
    corner_radius=7,
    text='Format Tap',
    fg_color='#464646',
    border_width=2,
    border_color='black',
    font=('popins',15,'bold'),
    hover=True,
    hover_color='gray',
    command=open_AndroidUtility)
    format_btn.place(x=35,y=30)
    format_img = PIL.Image.open(r'Photos\android.png')
    format_imag = ctk.CTkImage(format_img,size=(55,55))
    format_image = ctk.CTkLabel(
    format_tap,
    text='',
    image=format_imag,
    fg_color='#d3d2d5',
    corner_radius=7)
    format_image.place(x=220,y=30)
    format_txt="""Open AndroidUtility app\nto format the tap.           """
    format_label=ctk.CTkLabel(format_tap,
    text=format_txt,
    text_color="black",
    fg_color='#d3d2d5',
    font=('popins',18,'bold'))
    format_label.place(x=35,y=200)

    qr_code = ctk.CTkFrame(
    right_frame,
    width=300,
    height=230,
    fg_color="#d3d2d5",
    bg_color='#27007a',
    corner_radius=10,
    border_width=2,
    border_color="#181818")
    qr_code.place(x=30,y=355)
    qr_btn = ctk.CTkButton(
    qr_code,
    width=140,
    height=45,
    cursor='hand2',
    corner_radius=7,
    text='QR Code',
    fg_color='#464646',
    border_width=2,
    border_color='black',
    font=('arial',15,'bold'),
    hover=True,
    hover_color='gray',
    command=qr_method)
    qr_btn.place(x=35,y=30)
    qr_img = PIL.Image.open(r'Photos\qr.png')
    qr_imag = ctk.CTkImage(qr_img,size=(100,100))
    qr_image = ctk.CTkLabel(
    qr_code,
    text='',
    image=qr_imag,
    fg_color='#d3d2d5',
    corner_radius=7)
    qr_image.place(x=180,y=10)
    qr_txt="Open QR code."
    qr_label=ctk.CTkLabel(qr_code,
    text=qr_txt,
    text_color="black",
    fg_color='#d3d2d5',
    font=('arial',18,'bold'))
    qr_label.place(x=35,y=170)

    change_time=ctk.CTkButton(
    right_frame,
    width=220,
    height=50,
    cursor='hand2',
    corner_radius=7,
    border_width=2,
    border_color='black',
    fg_color='#464646',
    bg_color='#27007a',
    hover_color='gray',
    text='Change time',
    font=('popins',15,'bold'),
    command=change_time_method)
    change_time.place(x=400,y=50)

    reset_time=ctk.CTkButton(
    right_frame,
    width=220,
    height=50,
    cursor='hand2',
    corner_radius=7,
    border_width=2,
    border_color='black',
    fg_color='#464646',
    bg_color='#27007a',
    hover_color='gray',
    text='Reset time',
    font=('popins',15,'bold'),
    command=reset_time_method)
    reset_time.place(x=640,y=50)

    defult_formatType_txt = StringVar(value='Format Type : ')
    format_type = ctk.CTkComboBox(
    right_frame,
    width=460,
    height=40,
    values=['فك مؤقت','فك نهائي'],
    variable=defult_formatType_txt,
    bg_color='#27007a',
    border_color='black',
    state='readonly',
    border_width=2,
    font=('popins',15,'bold'),
    fg_color='#464646',
    dropdown_font=('popins',15,'bold'))
    format_type.place(x=400,y=120)

    stop_knox = ctk.CTkFrame(
    right_frame,
    width=460,
    height=290,
    fg_color="#d3d2d5",
    bg_color='#27007a',
    corner_radius=10,
    border_width=2,
    border_color="#181818")
    stop_knox.place(x=400,y=200)
    #========== exeption method =======
    def stop_knox_method():
        if defult_formatType_txt.get() == 'فك مؤقت' :
            open_file(r"Tools\SamFwTool\SamFwFRPTool.exe")
            show_notfiy("T505N Hack by Nour",'SamFWTool opend succesfully!')
        elif defult_formatType_txt.get() == 'فك نهائي' :
            open_file(r'Tools\SamFwToolSN\SamFwTool.exe')
            show_notfiy("T505N Hack by Nour",'SamFWTool opend succesfully!')
        else :
            messagebox.showerror('خطأ','لازم تختار اذا كنت هتفك نهائي او مؤقت')
    #====================================================================================
    samfw_btn = ctk.CTkButton(
    stop_knox,
    width=290,
    height=45,
    cursor='hand2',
    corner_radius=7,
    text='Stop KNOX',
    fg_color='#464646',
    border_width=2,
    border_color='black',
    font=('arial',15,'bold'),
    hover=True,
    hover_color='gray',
    command=stop_knox_method)
    samfw_btn.place(x=35,y=30)
    samfw_img = PIL.Image.open(r'Photos\samfw.png')
    samfw_imag = ctk.CTkImage(samfw_img,size=(65,65))
    samfw_image = ctk.CTkLabel(
    stop_knox,
    text='',
    image=samfw_imag,
    fg_color='#d3d2d5',
    corner_radius=7)
    samfw_image.place(x=340,y=20)
    stop_knox_txt="""Open SamFW tool to stop KNOX\nOr change serial numper             """
    samfw_label=ctk.CTkLabel(stop_knox,
    text=stop_knox_txt,
    text_color="black",
    fg_color='#d3d2d5',
    font=('arial',18,'bold'))
    samfw_label.place(x=35,y=210)

    dev_frame = ctk.CTkFrame(right_frame,
    fg_color='#d3d2d5',
    corner_radius=10,
    width=250,
    height=90,
    bg_color='#27007a')
    dev_frame.place(x=660,y=550)
    dev_txt="""Dev By: Nour Mohamed\n\nAll copyrights saved @2025"""
    dev_label = ctk.CTkLabel(dev_frame,
    width=245,
    height=85,
    bg_color='#d3d2d5',
    fg_color='#202020',
    corner_radius=10,text=dev_txt,font=('popins',15,'bold')).place(x=2.5,y=2.5)
    #======================================================================
    window.mainloop()
