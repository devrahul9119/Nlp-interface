from tkinter import *
from mydb import Db
from tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):
        # create database object
        self.dbo = Db()
        self.myapio = API()
        # Loading of GUI
        self.root = Tk()
        self.root.title('NLP App')
        # self.root.iconbitmap('image path')        # To add a image in app icon give image path
        self.root.geometry('500x600')
        self.root.configure(bg = 'purple')
        self.login_gui()
        self.root.mainloop()
    def login_gui(self):
        self.clear_gui()
        main_heading = Label(self.root,text='NLP Interface',bg='purple',fg='white')
        main_heading.pack(pady=(30,40))
        main_heading.configure(font= ('verdana',25,'bold'))

        email = Label(self.root,text = 'Enter Email',bg ='black',fg ='white')
        email.configure(font=('verdana',20))
        email.pack(pady=(10,10))


        self.email_input = Entry(self.root,width=60)
        self.email_input.pack(pady=(10,10),ipady=5)

        password = Label(self.root, text='Enter Password', bg='black',fg = 'white')
        password.configure(font=('verdana', 20),)
        password.pack(pady=(5,10))

        self.password_input = Entry(self.root, width=60,show='*')
        self.password_input.pack(pady=(10, 20), ipady=5)

        login_btn = Button(self.root,text='Login',bg = 'black',fg ='white',width=40,height=2,command=self.perform_login)
        login_btn.configure(font=('verdana',10,'bold'))
        login_btn.pack(pady=(10,10))

        message = Label(self.root,text='Not a member?')
        message.pack(pady=(10,10))
        message.configure(font=('verdana',20),bg='purple',fg='white')

        redirect_btn = Button(self.root,text='Register',width=15,height=1,command=self.register_gui)

        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear_gui()

        main_heading = Label(self.root, text='NLP Interface', bg='purple', fg='white')
        main_heading.pack(pady=(30, 40))
        main_heading.configure(font=('verdana', 25, 'bold'))

        name = Label(self.root, text='Enter Name', bg='black', fg='white')
        name.configure(font=('verdana', 20))
        name.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=60)
        self.name_input.pack(pady=(10, 10), ipady=5)

        email = Label(self.root, text='Enter Email', bg='black', fg='white')
        email.configure(font=('verdana', 20))
        email.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=60)
        self.email_input.pack(pady=(10, 10), ipady=5)

        password = Label(self.root, text='Enter Password', bg='black', fg='white')
        password.configure(font=('verdana', 20), )
        password.pack(pady=(5, 10))

        self.password_input = Entry(self.root, width=60, show='*')
        self.password_input.pack(pady=(10, 20), ipady=5)

        register_btn = Button(self.root, text='Register', bg='black', fg='white', width=40, height=2,command = self.perform_registeration)
        register_btn.configure(font=('verdana', 10, 'bold'))
        register_btn.pack(pady=(10, 10))

        message = Label(self.root, text='Already a member?')
        message.pack(pady=(10, 10))
        message.configure(font=('verdana', 20), bg='purple', fg='white')

        redirect_btn = Button(self.root, text='Login', width=15, height=1, command=self.login_gui)

        redirect_btn.pack(pady=(10, 10))

    def clear_gui(self):
        # clear the exiting Gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registeration(self):
        # Fetch data from Gui
        name = self.name_input.get()

        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo('Success','Registeration successful')
        else:
            messagebox.showerror('Error', 'Email already exists ')


    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email,password)
        if response:
            messagebox.showinfo('Success','Login Successfull')
            self.home_gui()
        else:
            messagebox.showerror('Error','Check email and password')
    def home_gui(self):
        self.clear_gui()
        main_heading = Label(self.root, text='NLP Interface', bg='purple', fg='white')
        main_heading.pack(pady=(30, 40))
        main_heading.configure(font=('verdana', 25, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', bg='black', fg='white', width=40, height=2,command=self.sentiment_gui)
        sentiment_btn.configure(font=('verdana', 10, 'bold'))
        sentiment_btn.pack(pady=(10, 10))

        nerr_btn = Button(self.root, text='Named Entity Recognition', bg='black', fg='white', width=40, height=2,command=self.ner_gui)
        nerr_btn.configure(font=('verdana', 10, 'bold'))
        nerr_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion detection', bg='black', fg='white', width=40, height=2,command=self.emotion_gui)
        emotion_btn.configure(font=('verdana', 10, 'bold'))
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', width=20, height=2,command=self.login_gui)
        logout_btn.configure(font=('verdana', 10, 'bold'))
        logout_btn.pack(pady=(10, 10))



    def sentiment_gui(self):
        self.clear_gui()
        main_heading = Label(self.root, text='Sentiment Analysis', bg='purple', fg='white')
        main_heading.pack(pady=(30, 40))
        main_heading.configure(font=('verdana', 25, 'bold'))

        text = Label(self.root, text='Enter Your Text', bg='black', fg='white')
        text.configure(font=('verdana', 20), )
        text.pack(pady=(5, 10))

        self.sentiment_input = Entry(self.root, width=60)
        self.sentiment_input.pack(pady=(10, 10), ipady=5)

        sentiment_btn = Button(self.root, text='Analyse Sentiment', bg='black', fg='white', width=40, height=2,command=self.do_sentiment_analysis)
        sentiment_btn.configure(font=('verdana', 10, 'bold'))
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='', bg='purple', fg='white')
        self.sentiment_result.configure(font=('verdana', 20))
        self.sentiment_result.pack(pady=(10, 10))

        goback_btn = Button(self.root, text='Home-page',width=20, height=2,command=self.home_gui)
        goback_btn.configure(font=('verdana', 10, 'bold'))
        goback_btn.pack(pady=(10, 10))


    def ner_gui(self):
        self.clear_gui()
        main_heading = Label(self.root, text='Named Entity Recognition', bg='purple', fg='white')
        main_heading.pack(pady=(30, 40))
        main_heading.configure(font=('verdana', 25, 'bold'))

        text = Label(self.root, text='Enter Your Text', bg='black', fg='white')
        text.configure(font=('verdana', 20), )
        text.pack(pady=(5, 10))

        self.ner_input = Entry(self.root, width=60)
        self.ner_input.pack(pady=(10, 10), ipady=5)

        ner_btn = Button(self.root, text='Analyse NER', bg='black', fg='white', width=40, height=2,command=self.do_ner)
        ner_btn.configure(font=('verdana', 10, 'bold'))
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='purple', fg='white')
        self.ner_result.configure(font=('verdana', 20))
        self.ner_result.pack(pady=(10, 10))

        goback_btn = Button(self.root, text='Home-page',width=20, height=2,command=self.home_gui)
        goback_btn.configure(font=('verdana', 10, 'bold'))
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.myapio.sentiment_analysis(text)
        print(result)
        final_result = ''
        for i in result['sentiment']:
            final_result = final_result + i + ' : ' + str(result['sentiment'][i]) + '\n'

        self.sentiment_result['text'] = final_result

    def do_ner(self):
        text = self.ner_input.get()
        result = self.myapio.ner(text)
        new = result['entities']
        final_result = ''

        for i in new:
            name = i['name']
            final_result = final_result + 'name' +' : ' + name +'\n'

        self.ner_result['text'] = final_result

    def emotion_gui(self):
        self.clear_gui()
        main_heading = Label(self.root, text='Emotion Detection', bg='purple', fg='white')
        main_heading.pack(pady=(30, 40))
        main_heading.configure(font=('verdana', 25, 'bold'))

        text = Label(self.root, text='Enter Your Text', bg='black', fg='white')
        text.configure(font=('verdana', 20), )
        text.pack(pady=(5, 10))

        self.emotion_input = Entry(self.root, width=60)
        self.emotion_input.pack(pady=(10, 10), ipady=5)

        emotion_btn = Button(self.root, text='Detect emotion', bg='black', fg='white', width=40, height=2, command=self.do_emotion)
        emotion_btn.configure(font=('verdana', 10, 'bold'))
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg='purple', fg='white')
        self.emotion_result.configure(font=('verdana', 20))
        self.emotion_result.pack(pady=(10, 10))

        goback_btn = Button(self.root, text='Home-page', width=20, height=2, command=self.home_gui)
        goback_btn.configure(font=('verdana', 10, 'bold'))
        goback_btn.pack(pady=(10, 10))

    def do_emotion(self):
        text = self.emotion_input.get()
        result = self.myapio.emotion(text)
        final_result = ''
        for i in result['emotion']:
            results = result['emotion'][i]
            final_result = final_result + i + " : " + str(results) + '\n'

        self.emotion_result['text'] = final_result









nlp = NLPApp()