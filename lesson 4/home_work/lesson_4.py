# 2) კომენტარების სახით ახსენით რა არის input-ი და output-ი, მოიყავნეთ შესაბამისი მაგალითები.
# 3) კომენტარების სახით ახსენით რა არის snake_case წერის სტილი და როგორ ხდება ჩანაწერების გაკეთება.
# 3) შექმენით ცვლადი, რომელშიც შეინხავთ input ინსტრუქციით შემოტანილ მნიშვნელობას, შემდეგ შეამოწმებთ თუ რა ტიპის მონაცემი ინახება ამ ცვლადში და დაბეჭდავთ.
# 4) თიოთეული მონაცემთა ტიპისთვის (str,int,float), შექმენით 5 ცვლადი და დაუწერეთ კომენტარი თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.
# 5) აიღეთ 3 ცვლადი, შეინახეთ განსხავებული მონაცემთა ტიპები (str,int,float), შემდეგ type ინსტრუქციის გამოყენებით შეამოწმეთ, თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.
# 6) მომხმარებელს შემოატანინეთ ორი სიტყვა, შეინახეთ ისინი ცვლადებში, მოახდინეთ მათი კონკატინაცია და დაბეჭდეთ.
# 7) მომხმარებელს შემოატანინეთ სახელი, გვარი, ასაკი, სიმაღლე, წონა და ამ მონაცემების გამოყენებით დაბეჭდეთ ერთი დიდი წინადადება.

# 1)
# input ი არის კოდის წერის გარემო სადაც მომხმარებელს შეგვიძლია მოვთხოვოთ ინფორმაციის შემოტანა
# ხოლო Output ი არის უკვე შედეგი რასაც ჩვენ ვხედავთ 

# # 2)
# snake_case სტილი კოდის წერის არის _ ესეთი ტირე რომელიც გამოიყენება ცვლადების შესაქმნელად
# 3)
# name = input("enter your name: ")

# print(type(name))
# # 4)
# name = "fruit"        # str 
# city = "tbilisi"       # str 
# fruit = "apple"        # str
# color = "red"       # str 
# animal = "dog"       # str 


# age = 15               # int 
# score = 100            # int 
# year = 2026            # int 
# apples = 7             # int 
# cars = 3               # int 


# height = 1.75          # float 
# weight = 60.5          # float 
# price = 9.99           # float 
# temperature = 23.4     # float 
# 5)

# name = "TEKLA"
# age = 11.11
# qalaqsi_misasvleli_nomeri  = 22

# print(type(name))
# print(type(age))
# print(type(qalaqsi_misasvleli_nomeri))

# 6)
# name = input("enter your name")
# lastname = input("enter your lastname")
# print("hallo my name is",name,"and my lastname is",lastname)

# სახელი, გვარი, ასაკი, სიმაღლე, წონა
name = input("enter your name")
lastname = input("enter your lastname")
height = input("enter your height")
kg = input("enter your kg")

print("hallo my name is",name,"and my lastname is",lastname,"my height is",height,"and my kg is",kg)