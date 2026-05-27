# 1) მომხმარებელს შემოატანინეთ input-ის მეშვეობით თავისი სახელი, შეინახეთ იგი ცვლადში და ბეჭდეთ მიღებული მნიშვნელობა.
# 2) მომხმარებელს შემოატანინეთ თავისი სახელი, გვარი, ასაკი, ქალაქი, ქვეყანა. შეინახეთ ეს მონაცემები ცვლადებში და როგორც წინა გაკვეთილზე ავაწყეთ დიდი წინადადება, ამ მონაცემებისგან ანალოგიურად ააწყეთ იგივე წინადადება მონაცემებზე დაყრდნობით.
# 3) შექმენით 3 ცვლადი, თითოულ ცვლადში შეინახეთ 1 მონაცემთა ტიპის მნიშვნელობა, თქვენი დავალებაა კი საბოლოოდ დაბეჭდოთ ამ ცვლადების მონაცემთა ტიპები type() ფუნქციის მეშვეობით.

# 1) 
# name = input("enter your name")
# print(name)
# 2)
name = input("enter your name")
lastname = input("enter your lastname")
age = input("enter your age")
contury = input("enter your contury")

print("hallo my name is",name,"and my lastname is",lastname,"my age is",age,"and my contury is",contury)

# 3)
name = "Tekla"      
age = 11           
height = 1.54     

# ვბეჭდავთ თითოეული ცვლადის ტიპს
print(type(name))
print(type(age))
print(type(height))