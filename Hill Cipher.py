from tkinter import *
from tkinter import messagebox
import numpy as np

root = Tk()
root.geometry('1200x6000')
root.title('Message Encryption and Decryption')
Tops = Frame(root,width=1600)
Tops.pack(side=TOP)

f1 = Frame(root,width=800)
f1.pack(side=LEFT)

lblMsg = Label(Tops,font=('helvetica',50,'bold'),text="SECRET MESSAGE\n Hill Cipher",fg='black',bd=10,anchor='w')
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
  
EAM = {chr(i):i-97 for i in range(97,97+26)}
EAM_rev = {i-97:chr(i) for i in range(97,97+26)}

def encrypt(PT,key):
  #encryption
  PT = PT.replace(" ","")
  PT = PT.lower()
  print(PT)

  PT_num = [EAM[i] for i in PT]
  key_num = [EAM[i] for i in key]

  #convert PT into blocks
  #convert key into matrix
  BL = len(key_num)//2
  key_matrix = np.array(key_num).reshape(BL,BL)
  print(key_matrix)

  #convert PT into array to separate into blocks for multiplication
  PT_array = np.array(PT_num)
  PT_blocks = np.split(PT_array,len(PT_array)/BL)
  print(PT_blocks)

  CT_blocks = [np.matmul(PT_blocks[i],key_matrix) % 26 for i in range(len(PT_blocks))]
  print(CT_blocks)

  CT_array = np.concatenate(CT_blocks)
  print(CT_array)

  CT = [EAM_rev[CT_array[i]] for i in range(len(CT_array))]
  CT=''.join(CT) # join the separated letters into one word
  print(CT)
  return CT

def mod_inv_cal(deter):
  mod_inv = 0
  try:
    mod_inv = pow(deter,-1,26)
  except:
    messagebox.showerror('showerror','Modulo Inverse not Exists')
    print('error')
  return mod_inv

def decrypt(CT,key):
  #Decryption
  #key matrix
  key_num = [EAM[i] for i in key]
  BL = len(key_num)//2
  key_matrix = np.array(key_num).reshape(BL,BL)
  print(key_matrix)

  #adjacency of key matrix
  adj_key_matrix = np.linalg.inv(key_matrix)* round(np.linalg.det(key_matrix))
  print(adj_key_matrix)

  #find determinant to find inverse modulo of derterminant
  deter = round(np.linalg.det(key_matrix))

  #mod by 26 of deter
  mod_val = deter % 26

  #inverse modulo
  mod_inv = mod_inv_cal(deter)

  # key inverse to get plain text
  key_inverse = (mod_inv*adj_key_matrix) % 26

  #find PT from CT
  CT_num = [EAM[i]  for i in CT]
  CT_array = np.array(CT_num)
  CT_blocks = np.split(CT_array,len(CT_array)/BL)

  #calculate PT
  PT_blocks = [np.matmul(CT_blocks[i],key_inverse) % 26 for i in range(len(CT_blocks))]

  #convert into array
  PT_array = np.concatenate(PT_blocks)
  print(PT_array)

  PT1 = [EAM_rev[round(i)] for i in PT_array]
  PT1 = ''.join(PT1)
  print(PT1)
  return PT1

  
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
