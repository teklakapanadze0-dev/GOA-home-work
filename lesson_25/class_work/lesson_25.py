1) შექმენით ფუნქცია სახელად greet, რომელიც დაბეჭდავს მისალმების ტექსტებს. "Hello World!" და "Hello {name}".
2) შექმენი ფუნქცია double, რომელიც მიიღებს პარამეტრად 1 ცალ რიცხვს და თქვენი დავალებაა დააბრუნებინოთ ამ
ფუნქციას აკვადრატებული რიცხვი.
3) შექმენი ფუნქცია checkOdd, რომელიც მიიღებს პარამეტრად 1 ცალ რიცხვს და თქვენი დავალებაა დააბრუნებინოთ
ფუნქიას "ლუწი" თუ რიცხვი ლუწია, და "კენტი" თუ კენტია.
4) შექმენი ფუნქცია BMI, რომელიც პარამეტრად მიიღებს 2 ცალ რიცხვს (height, weight),
თქვენი დავალებაა დააბრუნოთ ამ ადამიანის BMI --> formula: weight / (height * height)
1)
def greet(name):
print("Hello World!")
print(f"Hello {name}")
greet("TEKLA")
2)
def double(num):
return num ** 2
print(double(6))
3)
def checkOdd(num):
if num % 2 == 0:
return "luw"
else:
return "kento"
print(checkOdd(4))
print(checkOdd(7))
4)
def BMI(height, weight):
return weight / (height * height)
print(BMI(1.75, 70))