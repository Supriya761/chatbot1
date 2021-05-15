from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp



engine = pp.init()


voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

 #pyttsx3
bot = ChatBot("My_bot")

convo = [
   'hello',
    'hi there !',
    'what is your name',
    'im Bot created by Supriya',
    'how are you?',
    'im doing great these days',
    'good to hear',
    'where you live',
    'I live in chennai',
    'tell me about yourself',
    'im created by Supriya. im quite in nature, i use to help other.how can i help u sir/madam?',
    '@4wyeg',
    'sorry ..i didnt get you..please ask again',
    'thank you ',
    'thank you.ask again',
    'what is data science?',
    'Data science is an inter-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from many structural and unstructured data. Data science is related to data mining, deep learning and big data.',
    'thank you so much',
    'its my pleasure!',
    'had your breakfast?',
     'yes. what about yours?'
]
trainer = ListTrainer(bot)
#now training the bot with help of trainer

trainer.train(convo)

#answer = bot.get_response("what is your name")
#print(answer)
#print("Talk to BOT")
#while(True):
    #query=input()
    #if query=='exit':
        #break
    #answer=bot.get_response(query)
    #Print("bot :", answer)

main = Tk()

main.geometry("500x650")

main.title("MY CHATBOT")
img=PhotoImage(file="bot2.png")

photoL = Label(main, image=img)
photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)

    msgs.insert(END, "you : " + str(query))
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame=Frame(main)

sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=10,yscrollcommand=sc.set)

sc.pack(side=RIGHT,fill=Y)

msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

#creating text field

textF=Entry(main,font=("Verdena",20))
textF.pack(fill=X,pady=5)

btn=Button(main,text="Ask from bot",font=("Verdena",20),command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

#going to bind main window with enter key
main.bind('<Return>', enter_function )

main.mainloop()




