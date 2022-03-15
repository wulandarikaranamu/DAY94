#membuat list dengan perulangan

#list
print("=======tidak pakai perulangan=======")
buah = ["apel","pisang","mangga"]
print(buah)
print("========pakai perulangan============")
for i in (buah):
    print(i)

#tuple
print("=======tidak pakai perulangan=======")
buah = ("apel","pisang","mangga")
print(buah)
print("========pakai perulangan============")
for i in (buah):
    print(i)

#set
print("=======tidak pakai perulangan=======")
buah = {"apel","pisang","mangga"}
print(buah)
print("========pakai perulangan============")
for i in (buah):
    print(i)

#dictionary
print("=======tidak pakai perulangan=======")
biodata = {'nama':'merry','umur':18,'suka':'ngoding'}
print("biodata['nama']:",biodata["nama"])
print("biodata['umur']:",biodata["umur"])
print("biodata['suka']:",biodata["suka"])
print("========pakai perulangan============")
for i in (biodata):
    print(i)


