# ეს არის str (string) ტიპის ცვლადი
name = "Pavle" 
surname = "Eprikian"
profession = "a Military Officer"
eye_color = " Dark honey color"

# ეს არის int (intejer) მთელი სიცხვები
born = 1984 
age = 38

# ეს არის float (ათწილადი) ტიპის ცვლადი
height = 181.5
weight = 80.5

# boolean (bool) ტიპის ცვლადი
i_wiil_learn_programing = True
i_can_not_learn_programing = False

if i_wiil_learn_programing == True and i_can_not_learn_programing == False:
     print("I am " + name + " " + surname + "," + " I was born in" + " " + str(born) + "," + 
    " and I am " + str(age) + " years old" + "," + " I am " + profession 
     + "," + " my height is " + str(height) + " sm " + "," + " my wweight is " 
     + str(weight) + " kg" + "," + " my eye color is " + eye_color + "," + " and I live in Rustavi city.")


print(type(name))
print(type(born))
print(type(height))
print(type(i_wiil_learn_programing))

one = 5
two = "5"
tree = int(two)
two = tree
print(one)
print(two)
print(one + int(two))
print(two)

print(type(two))