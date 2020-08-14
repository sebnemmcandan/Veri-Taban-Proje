import psycopg2
from random_name import random_name
from tkinter import *
import tkinter.messagebox as MessageBox
import random
import datetime
import sys
from tkinter import messagebox
from tkinter import messagebox as ms

from tkinter import *
from tkinter import messagebox as ms

connection = psycopg2.connect(user="postgres", password="123", host="localhost", port=5432, database="postgres")
print(connection)

cursor = connection.cursor()

#cursor.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
connection.commit()
connection.close()


class main:
    def __init__(self, master):
        self.master = master
        self.mail = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    def open(self):
        top = Toplevel()
        top.title("Yeni Pencere")
        top.geometry("500x500")
        my_label = Label(top, image=None).pack()

    def login(self):
        connection = psycopg2.connect(user="postgres", password="123", host="localhost", port=5432, database="postgres")
        print(connection)

        cursor = connection.cursor()

        mail1 = self.mail.get()
        password1 = self.password.get()
        find_user = f"SELECT * FROM users WHERE mail = '{mail1}' and password = '{password1}'"
        cursor.execute(find_user)
        result = cursor.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.mail.get() + '\n Giriş Yapıldı...'
            button_new_screen = Button(root, text="Yeni Pencere Aç", command=self.open).pack()
            root.geometry("300x300")
            #self.head['pady'] = 500

        else:
            ms.showerror('Hata!', 'Kullanıcı Bulunamadı.')

    def new_user(self):
        connection = psycopg2.connect(user="postgres", password="123", host="localhost", port=5432, database="postgres")
        print(connection)

        cursor = connection.cursor()

        name = self.n_username
        find_user = f"SELECT mail FROM users WHERE mail = '{name}'"
        cursor.execute(find_user)

        if cursor.fetchall():
            ms.showerror('Hata!', 'Kullanıcı Adı Başka Birisi Tarafından Kullanılmaktadır Lütfen Başka Bir Kullanıcı Adı Girin!.')
        else:
            ms.showinfo('Başarılı!', 'Hesap Oluşturuldu!')
            self.log()
        username1 = self.n_username.get()
        password1 = self.n_password.get()
        insert = f"INSERT INTO users(mail,password) VALUES('{username1}','{password1}')"
        cursor.execute(insert)
        connection.commit()


    def log(self):
        self.mail.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'GİRİŞ'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'HESAP OLUŞTUR'
        self.crf.pack()

    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Kullanıcı Adı: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.mail, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Şifre: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Giriş ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Hesap Oluştur ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Kullanıcı Adı: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Şifre: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Hesap Oluştur', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Giriş Ekranına Dön', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)


if __name__ == '__main__':
    # Create Object
    # and setup window
    root = Tk()
    root.title('Giriş Formu')
    # root.geometry('400x350+300+300')
    main(root)
    root.mainloop()
