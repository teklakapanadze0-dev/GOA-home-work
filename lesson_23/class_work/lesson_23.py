# 1) მოცემულია სია: fruits = ["ვაშლი", "ბანანი", "ატამი"]. 
# insert() მეთოდით დაამატე "ფორთოხალი" მეორე ინდექსზე (ანუ მესამე ადგილას).

# 2) მოცემულია სია: cars = ["BMW", "Mercedes", "Audi", "Tesla"]. 
# pop() მეთოდით ამოშალე ბოლო ელემენტი და დაბეჭდე განახლებული სია.

# 3) გაქვს სტუდენტების სია: students = ["ანი", "ლუკა", "ნიკო", "ანი", "მარი"]. 
# count() მეთოდით დათვალე, რამდენჯერ გვხვდება სახელი "ანი" ამ სიაში.

# 4) მოცემულია ქალაქების სია: cities = ["თბილისი", "ქუთაისი", "ბათუმი", "რუსთავი"]. 
# remove() მეთოდით წაშალე "რუსთავი" სიიდან და დაბეჭდე განახლებული სია.

# 5) მოცემულია რიცხვების სია: nums = [45, 12, 89, 3, 27]. 
# დაალაგე სია ზრდადობის მიხედვით sort() მეთოდით და დაბეჭდე.

# 6) მოცემულია სია: colors = ["წითელი", "მწვანე", "ლურჯი"]. 
# გამოიყენე index() მეთოდი, რათა გაიგო რომელ ინდექსზეა სიტყვა "მწვანე".

# 7) მომხმარებელს ცალ-ცალკე შემოატანინე 3 საყვარელი კერძი და დაამატე სიაში. 
# ბოლოს დაბეჭდე ანბანის მიხედვით დალაგებული სია.

# 8) მოცემულია სია: languages = ["Python", "JS", "C++", "Java"]. 
# ამოშალე პირველი ელემენტი (ინდექსი 0) pop() მეთოდით.

# 9) მოცემულია სია: inventory = ["laptop", "mouse", "keyboard", "mouse"]. 
# თუ "mouse" სიაში ერთზე მეტჯერ გვხვდება (გამოიყენე count), ამოშალე მისი პირველი შემთხვევა remove()-ით.|

# 10) მოცემულია სია: names = ["ნიკა", "ელენე", "გიორგი"]. 
# მომხმარებელს შემოატანინე ახალი სახელი. თუ სახელი უკვე არის სიაში (გამოიყენე count), 
# დაბეჭდე "ეს სახელი უკვე გვაქვს", თუ არადა ჩაამატე სიაში.


# 1)
# fruits = ["vasli", "banana", "atam"]
# fruits.insert(2, "fortxoli")
# print(fruits)

# 2)
# cars = ["BMW", "Mercedes", "Audi", "Tesla"]
# cars.pop()
# print(cars)

# 3)
# students = ["ani", "luka", "niko", "ani", "mari"]
# count = students.count("ani")
# print(count)
# 4)

# cities = ["Tbilisi", "qutesisi", "batumi", "rustavi"]
# cities.remove("rustavi")
# print(cities)

# 5)
# nums = [45, 12, 89, 3, 27]
# nums.sort()
# print(nums)

# 6)
# colors = ["witeli", "mwvane", "lurji"]
# print(colors.index("mwvane"))

# 7)

# foods = []
# foods.append(input("seiyvane piurvel kerzi"))
# foods.append(input("seiyvane meore kerzi"))
# foods.append(input("seiyvane mesame kerzi"))
# foods.sort()
# print(foods)

# 8)
# languages = ["Python", "JS", "C++", "Java"]
# languages.pop(0)
# print(languages)

# 9)
# inventory = ["laptop", "mouse", "keyboard", "mouse"]
# if inventory.count("mouse") > 1:
#     inventory.remove("mouse")

# print(inventory)
# 10)
# names = ["nika", "elene", "giorgi"]
# new_name = input("dawere saxeli")

# if names.count(new_name) > 0:
#     print("es saxeli ukve aris")
# else:
#     names.append(new_name)

# print(names)