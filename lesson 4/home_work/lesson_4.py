# 1)მომხმარებელს სთხოვეთ input-ის გამოყენებით შეიყვანოს თავისი სახელი და print-ის (output) გამოყენებით მიესალმეთ მას.
# 2)კომენტარების სახით ახსენით რა არის კონკატენაცია (concatenation) და მოიყვანეთ შესაბამისი მაგალითი.
# 3)შექმენით ორი ცვლადი, სადაც input ინსტრუქციით შეინახავთ მომხმარებლის სახელსა და გვარს. დაბეჭდეთ ისინი ერთ წინადადებაში კონკატენაციის (+) გამოყენებით.
# 4)შექმენით ცვლადი, სთხოვეთ მომხმარებელს input-ით საყვარელი ფერის შეყვანა. შემდეგ კონკატენაციის გამოყენებით დაბეჭდეთ ტექსტი: "შენი საყვარელი ფერია " და მიუერთეთ შემოტანილი მნიშვნელობა.
# 5)input-ის საშუალებით მომხმარებელს შემოატანინეთ 3 განსხვავებული სიტყვა სხვადასხვა ცვლადში. კონკატენაციის დახმარებით შეაერთეთ ეს სიტყვები ისე, რომ მიიღოთ ერთი სრული წინადადება (space)-ის გათვალისწინებით და დაბეჭდეთ.


# 1)
# name = input("enter your name")
# print("gamarjoba",name)

# 2)
# კონკატენაცია არის როდესაც ორ სიტყვას ვაერთებთ ერთად ( ორზე მეტიც შეიძლება ) მაგალითად
name = "tekla"
lastname = "kapanadze"
print("hallo your name is", name, "and you lastname is", lastname)

# 3)
name = input("what is your name")
lastname = input("what is your name")
print(name +" "+ lastname)

# 4)
color = input("what is your fav color?")
print("your fav color is", color)
# 5)
subject = "art"
subject_2 = "sport"
subject_3 = "history"
print("my favorite subjects is" +" "+ subject+" "+subject_2+" "+"and"+" "+subject_3)