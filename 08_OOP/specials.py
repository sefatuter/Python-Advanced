mylist = [1,2,3]
# myString = 'my str'


# print(len(mylist))
# print(len(myString))
# print(type(mylist))
# print(type(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie object created.')

    def __str__(self): # str metodunu özelleştirdik
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print('Movie deleted.')

m = Movie('Movie name', 'Director', 120)

# print(type(m))
# print(len(m)) # movie objesi için len metodu yok

print(mylist)
print(m) # ram üzerinde hangi konumda oluşturulduğu
print(str(mylist))
print(str(m)) 
# Movie class'i içinde tanımladığımız özel metod ile
# str metodunun yapacağı işi değiştirdik

print(len(mylist))
print(len(m)) 
# Başlangıçta len metodu yok idi 
# ama biz len metoduna filmin süresini return'lamasi özelligini yükledik


# del m # m objesi silindi
#print(m)


