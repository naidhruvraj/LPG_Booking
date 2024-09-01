import pickle
"""d={"admin":"admin"}
f=open("admin","wb")
pickle.dump(d,f)
f.close()"""
f=open("database","rb")
l=[]
while True:
    try:
        data=pickle.load(f)
        l.append(data)
    except EOFError:
        break
f.close()
for i in l:
    print(i)

