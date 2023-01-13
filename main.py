import random

#initialization for key
master=[]
seed=['A','a','0','@']
for i in range(0,24):
  temp1=seed.copy()
  temp2=[]
  temp2.append(temp1[i//6])
  temp1.pop(i//6)
  temp2.append(temp1[(i%6)//2])
  temp1.pop((i%6)//2)
  temp2.append(temp1[(i%6)%2])
  temp1.pop((i%6)%2)
  temp2+=temp1
  master.append(temp2)
print(master)

def to95(x):
  if x<=1 and 95>=x:
    return x
  elif x>95:
    if x<1000:
      return to95(x-95)
    else:
      return (x%96+1)
  else:
    if x>-1000:
      return to95(x+95)
    else:
      return (-x)%96+1

def facList(x):
  listFac=[]
  for i in range(1,x+1):
    if x%i==0:
      listFac.append(i)
  return listFac

def ranFact(x):
  factRan=[]
  for i in range(0,3):
    r=(random.choice(facList(x)))
    factRan.append(r)
    x//=r
  factRan.append(x)
  return factRan
  
class Key:
  def __init__(self, key_list):
    self.dict={}
    count = 1
    for i in key_list:
      if i=="A":
        for j in range(0,26):
          self.dict[count]=chr(65+j)
          count+=1

      elif i=="a":
        for j in range(0,26):
          self.dict[count]=chr(97+j)
          count+=1

      elif i=="0":
        for j in range(0,10):
          self.dict[count]=chr(48+j)
          count+=1

      else:
        for j in range(0,16):
          self.dict[count]=chr(32+j)
          count+=1
        for j in range(0,7):
          self.dict[count]=chr(58+j)
          count+=1
        for j in range(0,6):
          self.dict[count]=chr(91+j)
          count+=1
        for j in range(0,4):
          self.dict[count]=chr(123+j)
          count+=1

  def printKey(self):
    pListT=list(self.dict.items())
    pListF=sorted(pListT, key=lambda a: a[0])
    for i in pListF:
      print(i[0],"\t:\t", i[1])

  def shift(self, pin):
    for i in list(self.dict.items()):
      if i[1]=="A":
        n1=i[0]
      elif i[1]=="a":
        n2=i[0]
      if i[1]=="0":
        n3=i[0]
      if i[1]==" ":
        n4=i[0]

    sKey1={}
    for i in range(0,26-pin[0]):
      sKey1[n1+pin[0]+i]=self.dict[n1+i]
    for i in range(0,pin[0]):
      sKey1[n1+i]=self.dict[n1+26-pin[0]+i]

    sKey2={}
    for i in range(0,26-pin[1]):
      sKey2[n2+pin[1]+i]=self.dict[n2+i]
    for i in range(0,pin[1]):
      sKey2[n2+i]=self.dict[n2+26-pin[1]+i]

    sKey3={}
    for i in range(0,10-pin[2]):
      sKey3[n3+pin[2]+i]=self.dict[n3+i]
    for i in range(0,pin[2]):
      sKey3[n3+i]=self.dict[n3+10-pin[2]+i]

    sKey4={}
    for i in range(0,33-pin[3]):
      sKey4[n4+pin[3]+i]=self.dict[n4+i]
    for i in range(0,pin[3]):
      sKey4[n4+i]=self.dict[n4+33-pin[3]+i]

    self.dict.update(sKey1)
    self.dict.update(sKey2)
    self.dict.update(sKey3)
    self.dict.update(sKey4)
  
  def encode(self, m_str):
    c_list=[]
    for i in m_str:
      for j in list(self.dict.items()):
        if i==j[1]:
          c_list.append(j[0])
          break
    return c_list
  
  def decode(self, c_list):
    m_str=""
    for i in c_list:
      m_str+=self.dict[i]
    return m_str

def cipher(message, k1=1, k2=1, k3=1, k4=1, pinn="0000", passw="password"):
  pin=[]
  for i in pinn:
    pin.append(int(i))
  

keyone=Key(master[14])
keyone.shift([1,0,5,9])
print(keyone.encode("Hello! Test Case scenario"))
for i in keyone.encode("Hello! Test Case scenario"):
  print(ranFact(i))