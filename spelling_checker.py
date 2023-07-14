from tkinter import *
from textblob import TextBlob
def spelling_checker():
    a=TextBlob(spell_check.get())
    spell=Label(window,text="the correct spelling is:",font=("Arial",20,"bold"),bg="white",fg="darkblue")
    spell.pack()
    correct_spelling=Label(window,text=str(a.correct()),font=("Arial",20,"bold"),bg="green",fg="white")
    correct_spelling.pack()
    spell_check.delete(first=0,last=100)



    

window=Tk()
window.title("spelling checker")
window.geometry("500x300")
window.config(background="lightblue")
text_heading=Label(window,text="Spelling Checker" , font=("Arial",20,"bold"), bg="black",fg="white")
text_heading.pack()
text_check=Label(window,text="Enter spelling",font=("Arial",15,"bold"),bg="black",fg="white")
text_check.pack()
spell_check=Entry(window,font=("Arial",25,"bold"),width=35,bg="white")
spell_check.pack()
check_button=Button(window, text="check ! !", command=(spelling_checker),font=("Arial",15,"bold"),bg="black",fg="white")
check_button.pack()
window.mainloop()



