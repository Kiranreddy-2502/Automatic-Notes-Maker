import speech_recognition as rvkk 
from tkinter import *
import pyttsx3
from PIL import Image, ImageTk
def recognize(p):
    rec=rvkk.Recognizer()

    with rvkk.AudioFile(p) as src:
        audio=rec.record(src)
        txt=rec.recognize_google(audio)
        print(txt)
    from collections import Counter as c
    x="beautiful morning children playing happily in the delicious treats the women washing firms in the weather and singing about the lazy husband's the great chief MS into the two men sitting in front of him great chief the man next to me is a field is the real reason it is a great then tell me what's the history of a one of my sheep and the old man and what is your answer to that the great cheese as younger man voiced Yoshi greatly admired the young man I have lots of them"
    s=txt.lower()
    s=s.split()
    
    res="beautiful african morning children were playing happily in the village streets the women were washing clothes in the river and singing about the lazy husbands the great cheif listened to the two men sitting in front of him great cheif the man next to me is a thief is that really so replied the great chief then tell me what did he steal from you one of my sheep answered the old man and what is your answer to that the great chief asked the younger man why steal sheep great chief replied the young man i have lots of them".split()
    s=c(s)
    res=c(res)
    total=sum(list(res.values()))
    for i in res:
        res[i]-=s[i]
    li=res.values()
    su=0
    for i in li:
        su+=abs(i)
    print(((total-su)/total)*100)

def path():
    s=input("enter path here:")
    print("working.......")
    recognize(s)
    
def reco():
    rec=rvkk.Recognizer()
    while(1):
        try:        
            with rvkk.Microphone() as srce:
                aud=rec.listen(srce)
                txt=rec.recognize_google(aud)
                txt=txt.lower()
                print(txt)
        except:pass                    

w=Tk()
can=Canvas(w,width=400,height=400)
#f=Frame(w,height=700,width=1600).pack(padx=800,pady=800)
w.geometry("800x800")
b1=Button(can,text="specify path",width=10,height=6,command=path)
b1.pack(side='bottom')
b1.place(x=400,y=350)
b2=Button(can,text="start recording",width=10,height=6,command=reco)
b2.pack(side='right')
b2.place(x=300,y=350)
bgi=Image.open(r"C:\Users\Student\Desktop\New folder\images.png")
bgi=bgi.resize((800,800))
bg=ImageTk.PhotoImage(bgi)
#image = image.resize((450, 350), Image.ANTIALIAS)
can.pack(fill='both',expand=True)
can.create_image(0,0,image=bg,anchor="nw")
