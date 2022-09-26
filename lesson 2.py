name ="pavle"
# len გამოაქვს სტრიქონის სიგრძე
print(len(name)) 

# გრძელი STR-ის, წინადადების და მრავალხაზიანი წინადადების წერის პრინციპი
my_sentense = """ good morning,
I am Pavle Eprikian
I was born in 1984
and I am 38 years old """
print(my_sentense)

knows_programing = True

# if ფუნქციის გამოყენება
# tab-ის საშუალებით მოვახდინეთ ინდენტაცია (indentation)
if 10 < 5:
    print("hello")

if True:
    print("hello") 

# სტრიქონებში ინდექსების ადგილების განსაზღვრა
# ყველა სტრინგი შეგვიძლია მივიჩნიოთ სიად
# ციფრები   0123456789.... განსაზღვრავს დაბლა მდგომ არპებს
# შეგვიძლის სტრიქონების დასლაისება ანუ ამოჭა ინდექსების
full_name = "pavle eprikian"
print(len(full_name)) 

# პირველი ინდექსის დაბეჭვდვა
print(full_name[0])

# პირველიდან ბოლო ინდექსის ჩათვლის დაბეჭვდვა
print(full_name[0:14])

# პირველიდან ბოლო ინდექსის ჩათვლის ყოველი მე-2 ინდექსის დაბეჭვდვა
# start:finish:step
print(full_name[0:14:2])

# მე-2 ინდექსიდან მე-7 ინდექსამდე დაბეჭვდვა
print(full_name[2:7])

# პირველიდან ბოლო ინდექსამდე დაბეჭვდვა
print(full_name[0:-1])

# პირველიდან ბოლო ინდექსამდე დაბეჭვდვა
print(full_name[:-1])

# პირველიდან მე-5 ინდექსამდე დაბეჭვდვა
print(full_name[:5])

#  მე-5 ინდექსიდან მოლო ინდექსამდე დაბეჭვდვა
print(full_name[5:])

# მხოლოდ ბოლო ინდექსის დაბეჭვდვა
# ნეგატიური სიმბოლოების ბეჭვდვა ანუ ბოლოდან თვლა
print(full_name[-1])

# სრტიქონის ნეგატიური ბეჭვდვა ანუ ბოლოდან თვლა
print(full_name[-1:-10:-1])

# სტრიწონებში ასოს ძებნა "p" in full_name, გამოიტანს True რადგან ჭეშმარიტია
print("p" in full_name) 

# ასევე გამოიყენება სტრიწონებში ასოს ძებნა, გამოიტანს True რადგან ჭეშმარიტია
print("p" not in full_name) 

# სტრინგებს აქვთ მეთოდები
# სტრინგ.upper() ყველა სიმბოლოს გაზრდა
full_name = "pavle eprikian"
print(full_name.upper())

# სტრინგ.lower() ყველა სიმბოლოს დაპატარავება
full_name = "PAVLE EPRIKIAN"
print(full_name.lower())

# სფეისების ჩამოჭრა თავში და ბოლოში 
full_name = "  pavle eprikian "
print(full_name.strip())

# ჩანაცვლების ფუნქცია replace()
full_name = "pavle eprikian"
print(full_name.replace(" ", "+"))
print(full_name.replace("a", "*"))