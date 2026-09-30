# 2) აუცილებლად უყურეთ ჩანაწერს თავიდან, და გაიზარეთ ყველაფერი რაც გაკვეთილზე ვისაუბრეთ და ავხსენით.
# 3) კომენტარების სახით ჩამოთვალეთ ყველა შედარებითი ოპერატორები და გააკეთეთ 5-5 მაგალითი თითოეულზე.
# 4) კომენტარების სახით ახსენით რა არის logical operators, ჩამოწერეთ თითოეული და განმარტეთ რომელი რა დროს რა შედეგს გვიბრუნებს.
# 5) გააკეთეთ 3-3 მაგალითი logical operator-ებზე.
# 6) მომხმარებელს შემოატანინეთ რიცხვი, შეინახეთ იგი ცვლადში და შეადარეთ იგი მეტია თუ არა თქვენს მიერ წინასწარ გამზადებულ რიცხვზე.
# 7) მომხმარებელს შემოატანინეთ სახელი, შეინახეთ იგი ცვლადში და მკაცრად შეამოწმეთ უდრის თუ არა იგი თქვენს სახელს.
# 8) მომხმარებელს შემოატანინეთ თავისი ასაკი, შეინახეთ იგი ცვლადში და შეამოწმეთ მეტია თუ არა იგი 18.

# < (metoba),>(nakleboba), <= (metia an tolia), >=(naklebia an tolia), ==(toloba)
print(123 < 832)
print(12444 < 82)
print(1243 < 8)
print(23 < 32)
print(868 < 832)

print(43 > 12)
print(5233 > 832634)
print(12653 > 752)
print(2353 > 8634)
print(1243 > 832)

print(1 <= 832)
print(3 <= 832)
print(143 <= 82)
print(643 <= 8)
print(123 <= 832)

print(12523 >= 8352)
print(1223 >= 8342)
print(1236 >= 8632)
print(123 >= 832)
print(123 >= 85632)

print(123 == 832)
print(123 == 832)
print(123 == 832)
print(823 == 812)
print(1233 == 1233)

# 4) logican operators aris igive boolean i anu true da false magalitad  print(1233 == 1233) am semtxvevasi
# pasuxi iqneba True imitom rom sworia pasuxi magram print(123 == 832) am semtxvevasi gvicvenebs
# Falses anu arasworia paxuxi

# 5)   True
print(123 == 123)
print(823 == 823)
print(1233 == 1233)
    #  false

print(123 == 832)
print(123 == 832)
print(123 == 832)

# 6)
my_number = 50
user_number = int(input("enter your num: "))
if user_number > my_number:
    print("tqvenu ricxvi metia winaswar gamzadebul ricxvze")
else:
    print("tqveni ricxvi ar aris meti winaswar gamzadebul ricxvze")

# 7)
my_name = "Tekla"

# მომხმარებლისგან სახელის მიღება
user_name = input("enter yout name: ")

# მკაცრი შედარება
if user_name == my_name:
    print("we names are same")
else:
    print("we names are not same")    

# 8)

age = int(input("enter yout age: "))
if age > 18:
    print("your age is 18 meti")
else:
    print("you are age 18 naklebi")