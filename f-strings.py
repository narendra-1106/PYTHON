letter="My name is {} and I am from {} "
name="Narendra"
country="India"

print(letter.format(name,country))

#Using f-string

print(f"Hey my name is {name} and I am from {country}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.02929828)) #it will take only 2 decimal points

price=99.8888
txt1=f"for only {price:.2f}"
print(txt1)


print(type(f"{2 * 30}"))

letter1="My name is {{}} and I am from {{}} "   # for printing as it is 
print(letter1)