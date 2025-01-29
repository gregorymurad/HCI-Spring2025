professors = ["greg","kianoosh","debra","richard","leo","patricia"]

myFavoriteProf = professors[3]

print(myFavoriteProf,"is my favorite professors in KFSCIS")

firstName = "greg"
lastName = "reis"

print(firstName + lastName) # concatenation
print(firstName + " " + lastName)
print(firstName, lastName)

message = f"{firstName} {lastName} is my HCI professor."
print(message)

a = 5
b = 2
print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a // b) # integer division
print(a ** b) # exponentiation: a to the power of b
print(a % b) # modulo: the remainder of the division of a by b

print(len(professors))
print(professors[0])
print(professors[-1])
print(professors[2:4]) # accessing indices 2 and 3
print(professors[1:5]) # accessing indices 1, 2, 3, and 4
print(professors[:3]) # accessing from 0 to 2
print(professors[3:]) # accessing from 3 all the way to the end

print("leo" in professors)

for i in professors:
    print(i.title())
print("FIU")

professors[3] = "trevor"
print(professors)
professors.insert(3,"jason")
print(professors)
professors.append("charlyne")
print(professors)
professors.extend(["kaoutar","mustafa"])
print(professors)