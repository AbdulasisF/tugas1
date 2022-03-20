(1)
#list
list=["Python", 100, 1.99, False]
for i in (list):
  print(i)

#update
list[1]= 200
list[3]= True
print(list)  

#hapus
list.remove(200)
print(list)

#nambah
list.append(400)
print(list)


(2)
#set
set= {"Python", 100, 1.99, False}

print(set)

#remove
set.remove ("Python")
print(set)

#tambah
set.add("ikmal")
print(set)


(3)
#tuple
tuple= ("Python", 100, 1.99, False)
print(tuple)

#update
tuple= list(tuple)
tuple[1]= 400
print(tuple)

#hapus
tuple.remove(False)
print(tuple)

#menambhkan
tuple.append (True)
print(tuple)




(4)
#dictionary
dict={"saya":"dia","mereka":"kamu"}

print(dict)

#update
dict["saya"] = "teknik"
print(dict)

#hapus
dict.pop("saya")
print(dict)

#nambah
dict ["ikmal"] = "al"
print(dict)