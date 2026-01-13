#Strings are immutable

a="Narendra &&& !!! Narendra"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!")) #delete trailing char

print(a.replace("Narendra", "Naru"))

print(a.split(" "))

Name= "nArEnDRa jAgtaP "
print(Name.capitalize()) #first char upper case and other lower case


print(len(a))
print(len(a.center(50)))

print(a.count("Narendra"))

print(Name.endswith("!!!"))  #TRUE or False

print(Name.find("j"))

#Insdex Method 
# print(Name("nArEnDRa"))


Name1="NarendraJagtap"
#is alnum means used of A-z and 1-infi 
print(Name1.isalnum())

name="naru1106"
#isalpha used for only A-z Not for Numbers
print(Name1.isalpha())
print(name.isalpha())

print(name.islower())
print(name.isupper())

str="Narendra Jagtap"
str1="Narendra \njagtap"
print(str.isprintable())
print(str1.isprintable())


#is title is return true only when first letter is capital
print(str.istitle())

#swap case is used for upper to lower and lower to upper
print(str.swapcase())

#used for title  capitalize the first letter
print(str.title())
