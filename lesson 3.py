# ფორმატის გამოყენება რდესაც გვაქვს გრძელი STR ტიპის ცვალდი და {} ფრჩხილები .format გამოყენებით ხორციელდება
# თთოეულ {} განხორციელდება ცვადის ჩასმა
my_sentence = "AA {} BB {} CC {}".format("xx", "yy", "zz")
print(my_sentence)

# საკლასო დავალება
# .format მეთოდი უნდა მოვახდინთ სახელის, გვარის და ასაკის ჩასმა {} ფრჩხილებში
name = "pavle"
surname = "eprikian"
age = 38
class_work = "my name it = {} my surname is = {} my age is = {}".format(name,  surname, age)
print(class_work)


# if და esle  ახსნა. 
# if გამოყენება ხდება მაშინ როცა გვინდა გავიგოთ ხორციელდება თუ არა რაღაც პირობა, მაშინ განხორციელდეს მომდევნო პირობა.
# esle გამოყენება ხდება მაშინ როცა არ ხორციელდება if ფუნქცია
my_name ="pavle"
if "k" in my_name:
    print(" Sheicavs k asos")
else:
    print(" ar Sheicavs k asos")

# input და uotput მეთოდები
# input მეთოდი გამოიყენება როდესაც მომხმარებელს ვთხოვთ STR ტიპის ცვლადების შემოყვანას.
# int(input) მეთოდი გამოიყენება როდესაც მომხმარებელს ვთხოვთ INT ტიპის ცვლადების შემოყვანას.
my_name = input("enter your name: ")
my_age = int(input("enter your age"))
print(my_name, my_age)

# საკლასო დავალება
# შემოატანინეთ მომხმარებელს სახელი, გვარი და ასაკი.
# დაპრინტეთ წინადადებაში ეს ცვლადები, .format მეთოდის გამოყენებით.
# გავიდეს 3 წელი და გაზარდეთ ასაკი, დაპრინტეთ ახალი წინადადება.
# გავიდა 3 წელი და მე გავხდო xx წლის. 
your_name = input("enter your name: ")
your_surname = input("enter your surname: ")
your_age = int(input("enter your age: "))
class_work = "your name it = {} your surname is = {} your age is = {}".format(your_name,  your_surname, your_age)
print(class_work)
after_tree_year_age_is = your_age + 3
print("after tree year age will be" , after_tree_year_age_is)

# საკლასო დავალება
# მომხმარებელს შემოატანიონეთ ორი რიცხვი და დაპრინტეთ,
# მათი ნამრავლი თუ ის 100-ზე მეტია, თუ არადა დაპრინტეთ რომ მან წააგო
number1 = int(input("enret number1: "))
number2 = int(input("enret number2: "))
if number1 * number2 > 100:
    print("it is more then 100")
else:
    print("you lose")

# საშინაო დავალება
# მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი.
# აქედან მხოლოდ კენტი რიცხვები შეკრიბოს და დაპრინტოს ჯამი
number1 = int(input("enret number1: "))
number2 = int(input("enret number2: "))
number3 = int(input("enret number3: "))
sum_of_odd_numbers = 0
if number1 % 2 == 1:
    sum_of_odd_numbers += number1
if number2 % 2 == 1:
    sum_of_odd_numbers += number2
if number3 % 2 == 1:
    sum_of_odd_numbers += number3
print (sum_of_odd_numbers)
