from tkinter import *
import tkinter.messagebox

class Forms(Frame):
    def __init__(self, master):
        super(Forms,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        line = 1
        self.lbl_empty = Label(self, text= "").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_lastname = Label(self, text= 'Lastname:')
        self.lbl_lastname.grid(row=line, column=0, sticky=W)
        self.lastname = Entry(self, width=15, text='')
        self.lastname.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_firstname = Label(self, text='Firstname:')
        self.lbl_firstname.grid(row=line, column=0, sticky=W)
        self.firstname = Entry(self, width=15, text='')
        self.firstname.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_username = Label(self, text='Username:')
        self.lbl_username.grid(row=line, column=0, sticky=W)
        self.username = Entry(self, width=15, text='')
        self.username.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_pswrd = Label(self, text='Password:')
        self.lbl_pswrd.grid(row=line, column=0, sticky=W)
        self.pswrd = Entry(self, width=15, show='*')
        self.pswrd.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_gend = Label(self, text='Gender:')
        self.lbl_gend.grid(row=line, column=0, sticky=W)
        self.gend = StringVar()
        self.frm_gender = Frame(self)
        self.rad_female = Radiobutton(self.frm_gender, text="Female", variable=self.gend, value="Female")
        self.rad_female.grid(row=0, column=0, sticky=W)
        self.rad_male = Radiobutton(self.frm_gender, text="Male", variable=self.gend, value="Male")
        self.rad_male.grid(row=0, column=1, sticky=W)
        self.rad_female.select()
        self.frm_gender.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_ms = Label(self, text="Marital Status: ")
        self.lbl_ms.grid(row=line, column=0, sticky=W)
        self.ms = StringVar()
        self.m_stat = ["Single", "Married", "Separated", "Divorced"]
        self.ms.set(self.m_stat[0])
        self.drpdwn_ms = OptionMenu(self, self.ms, *self.m_stat)
        self.drpdwn_ms.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_hobbs = Label(self, text='Hobbies:')
        self.lbl_hobbs.grid(row=line, column=0, sticky=W)
        self.hobbies = ['Singing', 'Watching Movies', 'Dancing', 'Flexing']
        self.chkVar = list(self.hobbies)
        self.chk = list(self.hobbies)
        for i in range(len(self.hobbies)):
            self.chkVar[i] = BooleanVar()
            self.chk[i] = Checkbutton(self, text=self.hobbies[i], variable=self.chkVar[i])
            self.chk[i].grid(row=line, column=1, sticky=W)
            line += 1

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_psnlstmnt = Label(self, text="Personal Statement : ")
        self.lbl_psnlstmnt.grid(row=line, column=0, sticky=W)
        self.psnlstmnt = Text(self, height=3, width=20)
        self.psnlstmnt.grid(row=line, column=1, sticky=W)
        self.yscrollbar = Scrollbar(self, command=self.psnlstmnt.yview)
        self.yscrollbar.grid(row=line, column=2, sticky='nsew')
        self.psnlstmnt['yscrollcommand'] = self.yscrollbar.set

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.btn_reset = Button(self, text="Reset", width=12, command=self.reset)
        self.btn_reset.grid(row=line, column=0, sticky=E)
        self.btn_submit = Button(self, text="Submit", width=12, command=self.submit)
        self.btn_submit.grid(row=line, column=1, sticky=W)

    def reset(self):
        self.lastname.delete(0, END)
        self.firstname.delete(0, END)
        self.username.delete(0, END)
        self.pswrd.delete(0, END)

        self.rad_female.select()

        self.ms.set(self.m_stat[0])

        for i in range(len(self.hobbies)):
            self.chk[i].deselect()

        self.psnlstmnt.delete(1.0, END)

    def submit(self):
        data = 'Lastname: {}\n'.format(self.lastname.get())
        data += 'Firstname: {}\n'.format(self.firstname.get())
        data += 'Username: {}\n'.format(self.username.get())
        data += 'Password: {}\n'.format(self.pswrd.get())
        data += 'Gender: {}\n'.format(self.gend.get())
        data += 'Marital Status: {}\n'.format(self.ms.get())

        hobbies = ''

        for i in range(len(self.hobbies)):
            if self.chkVar[i].get():
                hobbies += self.chk[i]['text'] + ''

        data += 'Hobbies: {}\n'.format(hobbies)
        data += 'Personal Statement: {}\n'.format(self.psnlstmnt.get(1.0, END))
        #print(data)

        file = open('formdata.txt', 'w+')
        file.write(data)
        file.close()

        f = open('formdata.txt', 'r')
        print(f.read())
        f.close()

        tkinter.messagebox.showinfo("Submission Status", "Submitted Successfully!!!")
        self.reset()


window = Tk()
window.title("Forms")
window.geometry('400x600')
app = Forms(window)
app.mainloop()