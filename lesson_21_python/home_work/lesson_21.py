# 2) კომენტარებით ახსენით თუ რას აკეთებს .upper(); .lower(); .capitalize(); .find(), .count(),
# len(), .endswith(), .startswith() ფუნქციები.

# 3) მომხმარებელს შემოატანინეთ წინადადება და დაბეჭდეთ იგი პატარა ასოებით.

# 4) მომხმარებელს შემოატანინეთ ელფოსტის მისამართი და გადაამოწმეთ შეიცავს თუ არა '@'
# სიმბოლოს, შედეგი კი დაბეჭდეთ დიდი ასოებით.

# 5) მომხმარებელს შემოატანინეთ წიგნის დასახელება და შედეგი დაბეჭდეთ სათაურის სტილში.

# 6) მომხმარებელს შემოატანინეთ წინადადება და სიმბოლო. თქვენი დავალებაა დაითვალოთ
# რამდენჯერ გვხვდება ეს სიმბოლო წინადადებაში.

# 7) მომხმარებელს შემოატანინეთ სიტყვა და შეამოწმეთ, არის თუ არა იგი დიდი ასოებით,
# თუ კი — დაბეჭდე "სიტყვა უკვე დიდია!", თუ არა — გადააქციე და დაბეჭდე.


# 1)
# upper ი ადიდებს  lower აპატარავებს capitalize მარტო პირველ ასოს ადიდებს find პოულობს ტექსტს და აბრუნებს მის ინდექსს
# count ითვლის რამდენჯერ გვხვდება ტექსტი len სიგრძეს აბრუნებს endswith რითი მთავრდება ტექსტი და startwidth რითი იწყება
# 2)
# name = input("enter your name")
# print(name.lower())
# # 3)
# email = input("dawere elfota: ")

# if "@" in email:
#     print("VALID EMAIL".upper())
# else:
#     print("INVALID EMAIL".upper())

# 4)
# SATAURIS STILI RARI?
# 5)
# text = input("seiyvane winadadeba")
# symbol = input("seiyvane simbolo")

# print(text.count(symbol))

# 6)
word = input("dawere winadaweba ")

if word.upper():
    print("sityva didia")
else:
    print(word.upper())