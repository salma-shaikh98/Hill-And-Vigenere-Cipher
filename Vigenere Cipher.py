#Vignere Cipher

from tkinter import *
import numpy as np

root = Tk()
root.geometry('1200x6000')
root.title('Message Encryption and Decryption')
Tops = Frame(root,width=1600)
Tops.pack(side=TOP)

f1 = Frame(root,width=800)
f1.pack(side=LEFT)

lblMsg = Label(Tops,font=('helvetica',50,'bold'),text="SECRET MESSAGE\n Vignere Cipher",fg='black',bd=10,anchor='w')
lblMsg.grid(row=0,column=0)

lblCT = Label(f1,font=('arial',16,'bold'),text="MESSAGE",bd=16,anchor='w')
lblCT.grid(row=1,column=0)

Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

txtMsg = Entry(f1,font=('arial',16,'bold'),textvariable=Msg,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtMsg.grid(row=1,column=1)

lblkey = Label(f1,font=('arial',16,'bold'),text="KEY",bd=16,anchor='w')
lblkey.grid(row=2,column=0)

txtkey = Entry(f1,font=('arial',16,'bold'),textvariable=key,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtkey.grid(row=2,column=1)

lblmode = Label(f1,font=('arial',16,'bold'),text="MODE(e for encrypt,d for decrypt)",bd=16,anchor='w')
lblmode.grid(row=3,column=0)

txtmode = Entry(f1,font=('arial',16,'bold'),textvariable=mode,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtmode.grid(row=3,column=1)

lblresult = Label(f1,font=('arial',16,'bold'),text="Result",bd=16,anchor='w')
lblresult.grid(row=2,column=2)

txtresult = Entry(f1,font=('arial',16,'bold'),textvariable=Result,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtresult.grid(row=2,column=3)

def encrypt(plain_text,key):
    cipher_text=''
    n = len(plain_text)
    ceil_val = np.math.ceil(n/len(key))
    key = ceil_val*key
    for i in range(n):
      if plain_text[i] == ' ':
        cipher_text+=plain_text[i]
      else:
        if plain_text[i].isupper():
            pi = ord(plain_text[i])-65
            ki = ord(key[i])-65
            ei = (pi+ki)%26
            cipher_text += chr(65+ei)
        else:
            pi = ord(plain_text[i])-97
            ki = ord(key[i])-97
            ei = (pi+ki)%26
            cipher_text += chr(97+ei)
    print('Encrypted text:',cipher_text)
    return cipher_text

def decrypt(cipher_text,key):
    plain_text=''
    n = len(cipher_text)
    ceil_val = np.math.ceil(n/len(key))
    key = ceil_val*key
    for i in range(n):
      if cipher_text[i] == ' ':
        plain_text+=cipher_text[i]
      else:
        if cipher_text[i].isupper():
            ei = ord(cipher_text[i])-65
            ki = ord(key[i])-65
            di = (ei-ki)
            ## For handling -ve values
            if (di>=0):
                di = di%26
            else:
                di = (di+26)%26
            plain_text += chr(65+di)
        else:
            ei = ord(cipher_text[i])-97
            ki = ord(key[i])-97
            di = (ei-ki)
            if (di>=0):
                di = di%26
            else:
                di = (di+26)%26
            plain_text += chr(97+di)
    print('Decrypted text:',plain_text)
    return plain_text

def Results():
  msg = Msg.get()
  k = key.get()
  m = mode.get()

  if (m == 'e'):
    Result.set(encrypt(msg,k))
  else:
    Result.set(decrypt(msg,k))


def Reset():
  Msg.set("")
  key.set("")
  mode.set("")
  Result.set("")
  
def qExit():
  root.destroy()

btnShowMsg = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),
                    width=10,text='Show Message',bg='powder blue',
                    command=Results).grid(row=7,column=1)

btnReset = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),
                    width=10,text='Reset',bg='green',
                    command=Reset).grid(row=7,column=2)

btnExit = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),
                    width=10,text='Exit',bg='red',
                    command=qExit).grid(row=7,column=3)

