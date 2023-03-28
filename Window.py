from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import encryption_methods as em
import decryption_methods as dm
import checking_keys as ck

# TODO: add save decrypted text to file in some path
# TODO: add errors

# constant path to saving out text
PATH = 'outfile.txt'

class Win:
    # encrypting passed text from textFieldIn
    # then writes to textFieldOut
    def crypt_text(self):
        self.textFieldOut.delete(1.0, END)
        key = self.entrKeyField.get()
        if self.cbCheck.get() == 0:
            # Vigenere
            new_key = ck.edit_key_for_Venigere(key)
            if new_key:
                self.add_text_to_keyEntry(new_key)
                inStr = self.textFieldIn.get(1.0, END)
                outStr = em.encrypt_Vigenere(inStr, new_key)
                self.textFieldOut.insert(1.0, outStr)
            else:
                messagebox.showwarning("Key error", "Wrong key value")
                pass
        elif self.cbCheck.get() == 1:
            # Decimatiy
            new_key = ck.edit_key_for_Decimatiy(key)
            if new_key:
                self.add_text_to_keyEntry(new_key)
                inStr = self.textFieldIn.get(1.0, END)
                outStr = em.encrypt_Decimatiy(inStr, new_key)
                self.textFieldOut.insert(1.0, outStr)
            else:
                messagebox.showwarning("Key error", "Wrong key value")
        elif self.cbCheck.get() == 2:
            # Col
            new_key = ck.edit_key_column_cipher(key)
            inStr = ck.edit_instr_column_cipher(self.textFieldIn.get(1.0, END))
            if new_key and inStr:
                self.add_text_to_keyEntry(new_key)
                outStr = em.encrypt_columns_cipher(inStr, new_key)
                self.textFieldOut.insert(1.0, outStr)
            else:
                messagebox.showwarning("Key error", "Wrong key or initial string value")

        # saving out text to file
        self.save_text_to_file(PATH)

    # decrypting passed text from textFieldIn
    # then writes to textFieldOut
    def decrypt_text(self):
        self.textFieldOut.delete(1.0, END)
        key = self.entrKeyField.get()
        if self.cbCheck.get() == 0:
            # Vigenere
            new_key = ck.edit_key_for_Venigere(key)
            if new_key:
                self.add_text_to_keyEntry(new_key)
                inStr = self.textFieldIn.get(1.0, END)
                outStr = dm.decrypt_Vigenere(inStr, new_key)
                self.textFieldOut.insert(1.0, outStr)
            else:
                messagebox.showwarning("Key error", "Wrong key value")
        elif self.cbCheck.get() == 1:
            # Decimatiy
            new_key = ck.edit_key_for_Decimatiy(key)
            if new_key:
                self.add_text_to_keyEntry(new_key)
                inStr = self.textFieldIn.get(1.0, END)
                outStr = dm.encrypt_Decimatiy(inStr, new_key)
                self.textFieldOut.insert(1.0, outStr)
            else:
                messagebox.showwarning("Key error", "Wrong key value")
        elif self.cbCheck.get() == 2:
            # Col
            new_key = ck.edit_key_column_cipher(key)
            inStr = ck.edit_instr_column_cipher(self.textFieldIn.get(1.0, END))
            if new_key and inStr:
                self.add_text_to_keyEntry(new_key)
                outStr = dm.decrypt_columns_cipher(inStr, new_key)
                self.textFieldOut.insert(1.0, outStr)
            else:
                messagebox.showwarning("Key error", "Wrong key or initial string value")

        # saving out text to file
        self.save_text_to_file(PATH)

    # adding value to key entry field
    def add_text_to_keyEntry(self, key):
        self.entrKeyField.delete(0, END)
        self.entrKeyField.insert(0, key)

    # getting text from file to textFieldIn
    def get_text_from_file(self):
        filename = askopenfilename()
        if filename:
            with open(filename, "r") as f:
                self.textFieldIn.delete(1.0, END)
                self.textFieldIn.insert(1.0, f.read())

    # saving out text to file
    def save_text_to_file(self, path):
        out_text = self.textFieldOut.get(1.0, END)
        if out_text:
            with open(path, "w") as f:
                f.write(out_text)

    # initializer of window
    def __init__(self, width, height, title='Cipher'):
        # constants
        # self.filename = ''
        self.color = '#c0c0c0'

        self.root = Tk()
        self.root['bg'] = self.color  # цвет фона
        self.root.title(title)
        self.root.geometry(f'{width}x{height}')  # размер окна

        self.frame = Frame(self.root, bg=self.color)  # frame fot textFiledIn
        self.frame1 = Frame(self.root, bg=self.color)  # frame fot textFiledOut
        self.btnFrame = Frame(self.root, bg=self.color)  # frame for buttons (crypt, decrypt)
        self.btnLoadFrame = Frame(self.root, bg=self.color)  # frame for load button
        self.entryFrame = Frame(self.root, bg=self.color)  # frame for entry
        self.cbFrame = Frame(self.root, bg=self.color)  # frame for checkboxes
        self.txtFrame = Frame(self.root, bg=self.color)  # frame for labels

        # TODO: add hint labels before Text and Entry
        self.textFieldIn = Text(self.frame, height=30, width=20, font='Consolas 15', wrap=WORD)
        self.lblTextIn = Label(self.txtFrame, text='Initial text', font="Cosolas 20", bg=self.color, fg='black')
        self.lblTextOut = Label(self.txtFrame, text='Out text', font="Cosolas 20", bg=self.color, fg='black')
        self.textFieldOut = Text(self.frame1, height=30, width=20, font='Consolas 15', wrap=WORD)
        self.btnEcnrypt = Button(self.btnFrame, height=2, width=8, text="Encrypt", font="Consalas 20",
                                 command=self.crypt_text)
        self.btnDecrypt = Button(self.btnFrame, height=2, width=8, text="Dencrypt", font="Consalas 20",
                                 command=self.decrypt_text)
        self.btnLoadFile = Button(self.btnLoadFrame, height=2, width=10, text="Load from file", font="Consalas 20",
                                  command=self.get_text_from_file)
        self.entrKeyField = Entry(self.entryFrame, font="Cosolas 20")
        self.lblKey = Label(self.entryFrame, text='Key', font="Cosolas 20", bg=self.color, fg='black')
        # self.textFieldOut.configure(state='disabled')

        # check boxes
        self.cbCheck = IntVar()
        self.cbCheck.set(0)

        self.cbVigenere = Radiobutton(self.cbFrame, height=1, width=17, text="Vigenere(RU)", font="Consalas 20",
                                      bg=self.color, variable=self.cbCheck, value=0)
        self.cbDecimatiy = Radiobutton(self.cbFrame, height=1, width=17, text="Decimatiy(EN,NUM)", font="Consalas 20",
                                       bg=self.color, variable=self.cbCheck, value=1)
        self.cbUpgradedCol = Radiobutton(self.cbFrame, height=1, width=17, text="Upgraded column(EN)",
                                         font="Consalas 20",
                                         bg=self.color, variable=self.cbCheck, value=2)

    def draw_win(self):  # реализация функций и кнопок
        self.txtFrame.place(relx=0.1, rely=0.03, relwidth=0.4, relheight=0.05)
        self.frame.place(relx=0.03, rely=0.1, relwidth=0.3, relheight=0.7)
        self.frame1.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.7)
        self.btnFrame.place(relx=0.65, rely=0.80, relwidth=0.3, relheight=0.2)
        self.btnLoadFrame.place(relx=0.26, rely=0.80, relwidth=0.2, relheight=0.2)
        self.entryFrame.place(relx=0.70, rely=0.1, relwidth=0.25, relheight=0.15)
        self.cbFrame.place(relx=0.67, rely=0.30, relwidth=0.30, relheight=0.15)
        self.textFieldIn.pack()
        self.textFieldOut.pack()
        self.btnEcnrypt.pack(side="left")
        self.btnDecrypt.pack(side="right")
        self.btnLoadFile.pack(side="left")
        self.lblKey.pack()
        self.entrKeyField.pack()
        self.cbVigenere.pack()
        self.cbDecimatiy.pack()
        self.cbUpgradedCol.pack()
        self.lblTextIn.pack(side="left")
        self.lblTextOut.pack(side="right")

    def run(self):  # запуск стартового окна
        self.draw_win()
        self.root.mainloop()

    # Creating first window


window = Win(800, 500)
window.run()
