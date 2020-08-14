import psycopg2
from random_name import random_name
from tkinter import *
import tkinter.messagebox as MessageBox
import random
import datetime
import sys
from tkinter import messagebox

from tkinter import messagebox as ms

sys.setrecursionlimit(10000)

tokens = []

random_name1 = random_name()
random_name1.islem()
tokens = random_name1.mixed_words

print("------")
print(len(tokens))

try:
    connection = psycopg2.connect(user="postgres", password="123", host="localhost", port=5432, database="postgres")
    print(connection)

    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), "\n")

    # query = "create table customer(customer_id int primary key, firstName varchar(20) not null, lastName varchar(20) not null, phone varchar(11) not null, province varchar(20) not null);"
    # query = "create table order(order_number int primary key, "
    # query = "CREATE TABLE Orders (order_number int primary key, customer_id int not null, customer_name varchar(20) not null, to_city varchar(20) not null, ship_date date not null, product_id int not null, FOREIGN KEY(customer_id) REFERENCES customer(customer_id),FOREIGN KEY(product_id) REFERENCES product(product_id));"

    # query = "CREATE TABLE Orders (order_number int primary key, customer_id int not null, customer_name varchar(20) not null, to_city varchar(20) not null, ship_date date not null, product_id int not null, FOREIGN KEY(customer_id) REFERENCES customer(customer_id),FOREIGN KEY(product_id) REFERENCES product(product_id));"
    # query = "create table employees(employee_id int primary key not null, firstname varchar(20) not null, lastname varchar(20), birth_date date not null, gender varchar(6))"
    # query = "create table salary(employee_id int not null, salary int not null, FOREIGN KEY(employee_id) REFERENCES employees(employee_id));"

    # query = "alter table employees add FOREIGN KEY (salary) REFERENCES salary(salary);"
    # query = "alter table employees add unique (salary)"

    """
    query = "create table employees(" \
            "employee_id int primary key not null," \
            "firstname varchar(20) not null," \
            "lastname varchar(20) not null," \
            "birth_date date not null," \
            "gender varchar(6) not null," \
            "salary int not null);" \
    """
    """
    query = "create table salaries(" \
            "employee_id int not null," \
            "salary int not null," \
            "FOREIGN KEY (employee_id) REFERENCES employees(employee_id));"
    """

    # query = "INSERT INTO public.employees(" \
    #        "	employee_id, firstname, lastname, birth_date, gender, salary)" \
    #        "VALUES (1, 'Mehmet', 'Akkürek', '1995-06-27', 'Male', 4500);"
    num_list = []


    def create_random_number(list):
        for i in range(0, 5000):
            rand_numb = random.randint(2300, 8500)
            list.append(rand_numb)
        return list


    """
    num_list = create_random_number(num_list)
    z = 22
    for i in range(2,67):
        olusturulan_sayi = 0
        for j in range(2,5000):
            if num_list[j] %100 == 0:
                olusturulan_sayi = num_list[j]
                num_list.remove(olusturulan_sayi)
                break
            else:
                continue

        #query = "INSERT INTO public.salaries(employee_id, salary) VALUES (" + i + "," + olusturulan_sayi + ");"
        query = f"INSERT INTO public.salaries(employee_id, salary) VALUES({z}, {olusturulan_sayi});"
        z+=1
        cursor.execute(query)
        connection.commit()
    """
    """
    salaries = []
    salaries.append(6100)
    salaries.append(6600)
    salaries.append(5100)
    salaries.append(8100)
    salaries.append(6600)
    salaries.append(3800)
    salaries.append(4100)
    salaries.append(7500)
    salaries.append(3300)
    salaries.append(4600)
    salaries.append(8300)
    salaries.append(6500)
    salaries.append(7400)
    salaries.append(6400)
    salaries.append(7300)
    salaries.append(7800)
    salaries.append(7200)
    salaries.append(5500)
    salaries.append(7100)
    salaries.append(5800)
    salaries.append(3500)
    salaries.append(8500)
    salaries.append(5700)
    salaries.append(2400)
    """
    """
    start_date = datetime.date(1968, 1, 1)
    end_date = datetime.date(2000, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    dates = []
    for i in range(0,23):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        dates.append(random_date)
    for i in range(0,23):
        print(dates[i])
    """
    """
    for i in range(0, 23):
        kelime1 = ''.join(map(str, tokens[i]))
        print(kelime1)
        ad = kelime1.split()
        print(ad[-1])
        name = ''.join(map(str, ad[-1]))
        ad.pop(-1)
        ad.insert(1," ")
        surname = ''.join(map(str, ad))
        print(surname)
        query = f"INSERT INTO public.employees(employee_id, firstname, lastname, birth_date, gender, salary) VALUES ({i+1},'{surname}', '{name}', '{dates[i]}', 'Male', {salaries[i]});"

        cursor.execute(query)
        connection.commit()
    """
    """
    titles = []
    titles.append("Financial Manager")
    titles.append("Quality Control Man.")
    titles.append("General Manager")
    titles.append("Production Manager")
    titles.append("Project Engineer")
    titles.append("Associate Scientist")
    titles.append("Relationship Manager")
    titles.append("Sales Director")
    titles.append("Software Engineer")
    titles.append("Human Resources Man.")
    titles.append("R & D Engineer")
    titles.append("Factory Worker")
    titles.append("Factory Worker")
    titles.append("Factory Worker")
    titles.append("Factory Worker")
    titles.append("Factory Worker")
    titles.append("Factory Worker")
    titles.append("Factory Worker")
    titles.append("Factory Worker")
    titles.append("Factory Worker")
    titles.append("Factory Worker")
    titles.append("Factory Worker")
    titles.append("Factory Worker")

    for i in range(0, 23):
        kelime1 = ''.join(map(str, tokens[i]))
        print(kelime1)
        ad = kelime1.split()
        print(ad[-1])
        name = ''.join(map(str, ad[-1]))
        ad.pop(-1)
        ad.insert(1, " ")
        surname = ''.join(map(str, ad))
        print(surname)
        query = f"INSERT INTO public.employee_title(employee_id, title_name) VALUES ({i+1}, '{titles[i]}');"

        cursor.execute(query)
        connection.commit()
    """
    #    query = f"INSERT INTO public.employee_title(employee_id, title_name) VALUES ({i + 1}, '{titles[i]}');"

    #    cursor.execute(query)
    #    connection.commit()

    # rows = cursor.fetchall()

    # for r in rows:
    #    print(f"location id: {r[0]}\naddress: {r[1]}\npostal_code: {r[2]}\nstate: {r[3]}\ncountry_id: {r[4]}")
    #    print(f"department_id : {r[0]} : {r[1]}\n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected into the - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error connecting to PostgreSQL database", error)
    connection = None


finally:
    if (connection != None):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is now closed")
class main:



    """
    def create_window():
        window = tk.Toplevel(root)
    def open_new_window():
        top = Toplevel()
        top.title("Second Window")
        my_label = Label(top, image=None).pack()
    
    screen = Tk()
    screen.geometry("1920x1080")
    screen.title("Python Company Tkinter")
    Label(text = "Notes 1.0", bg = "grey", font = ('Calibri', 13)).pack()
    Label(text = "").pack()
    Button(text = "Login").pack()
    Button(text = "Register").pack()
    Button(screen, text="Create new window", command=create_window).pack()
    
    Button(screen, text="Open New Window", command=open_new_window).pack()
    
    mainloop()
    """
    #THE LAST SCREEN PAGE
    """
    def command1():
        if entry1.get() == "admin" and entry2.get() == "password":
            root.deiconify()
            top.destroy()
    def command2():
        top.destroy()
        root.destroy()
        sys.exit()
    
    root = Tk()
    top = Toplevel()
    
    top.geometry('300x260')
    top.title('Login Screen')
    top.configure(background='white')
    #photo2 = PhotoImage(file="C:\\Users\\berka\\Desktop\\image.jpg")
    #photo = Label(top, image=photo2, bg='white')
    photo = Label(top, image=None, bg='white')
    label1 = Label(top, text='Username:', font=('Helvetica', 10))
    entry1 = Entry(top)
    label2 = Label(top, text='Password:', font=('Helvetica', 10))
    entry2 = Entry(top, show="*")
    button2 = Button(top, text='Cancel', command=lambda:command2())
    
    entry2.bind('<Return>', command1)
    
    label3 = Label(top, text='Copyright Login Screen 2020', font=('Arial', 9))
    
    
    photo.pack()
    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    button2.pack()
    label3.pack()
    
    root.title('Main Screen')
    root.configure(background='white')
    root.geometry("855x650")
    
    root.withdraw()
    root.mainloop()
    """

    def __init__(self, master):
        # Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Create Widgets
        self.widgets()

        # Login Function

    def login(self):

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        cursor.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Loged In'
            self.head['pady'] = 150

        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):

        # Find Existing username if any take proper action
        find_user = ('SELECT username FROM user WHERE username = ?')
        cursor.execute(find_user, [(self.n_username.get())])
        if cursor.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        cursor.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        connection.commit()

        # Frame Packing Methords

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

        # Draw Widgets

    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)

    if __name__ == '__main__':
        # Create Object
        # and setup window
        root = Tk()
        root.title('Login Form')
        root.geometry('400x350+300+300')
        main(root)
        root.mainloop()
