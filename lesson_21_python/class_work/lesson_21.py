# 1)
name = input("enter your name")
print(name.lower())

# 2)
color = input("enter your color")
print(color.upper())
# 3)
city = input("enter your city")
print(city.capitalize())
# 4)
email = "student@university.ge"
print(email.index("@"))   

# 5)
word = "Programming"
print(word.index("r")) 
# 6)
sentence = "me miyvars msaxli da vasli"
print(sentence.find("banana"))
# 7)
info = "Error 404: Page not found"
print(info.find("404"))
# 8)
url = "https://www.google.com"
print(url.startswith("https://"))
# 9)
phone = "+995555123456"
print(phone.startswith("+995"))
# 10)
file_name = "document.pdf"
print(file_name.endswith(".pdf"))
# 11)
winadadeba = input("dawere winadadeba ")
print(winadadeba.endswith("?"))
# 12)
word = "abracadabra"
print(word.count("a"))
# 13)
data = "100110101011"
print(data.count("1"))
# 14)
products = "pru,rze,kvercxi,yveli"
print(products.split(","))
# 15)
word = "hello world"
print(len(word))
log_record = ">ERROR: user MARIAM@COMPANY.GE failed to load the backup file. #backup #Server #backup #urgent"

# 16.1
print(log_record.startswith(">ERROR:"))

# 16.2
print(log_record.endswith("#urgent"))

# 16.3
print(log_record.count("#backup"))

# 16.4
print(log_record.find("failed"))

# 16.5
print(log_record.find("@"))

# 16.6
words = log_record.split()

# 16.6.1
print(words[7].upper())

# 16.6.2
email = words[2].lower()
print(email)

# 16.6.3
name = email.split("@")[0].capitalize()
print(name)