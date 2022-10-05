
# საკლასო დავალევა
# მომხმარებელს შემოატანინეთ ორისახელი და ისინი დაპრინტეთ
# რომელ სახელშიც მეტი ხმოვანია. (დააფორმარტეთ პასუხი)

intput1 = input("enter  words 1: ")    
intput2 = input("enter  words 2: ")   

vowel_word1 = 0
vowel_word2 = 0

# for chart in intput1:
#     if chart == "a" or chart == "e" or chart == "i" or chart == "o" or chart == "u":
#         vowel_word1 += 1

# for chart in intput2:
#     if chart == "a" or chart == "e" or chart == "i" or chart == "o" or chart == "u":
#         vowel_word2+= 1

# იგივე ფორმულა უფრო მოკლე კოდით
for chart in intput1:
    if chart in "aeiou":
        vowel_word1+= 1

for chart in intput2:
    if chart in "aeiou":
        vowel_word2+= 1

if vowel_word1 > vowel_word2:      
     print ("in input1  is more vowel_word and it is {})" .format(vowel_word1))
elif vowel_word1 < vowel_word2: 
    print ("in input2  is more vowel_word and it is {})" .format(vowel_word2))
else:
    print("they have equl emount")



# საკლასო დავალება
# შემოიტანეთ სახელი და დათვალეთ რამდენი "ა" გხვდებათ
word = input("entre word")
summ = 0
for char in word:
    if "a" == char:
       summ += 1
print('there is {} "a" in my text' .format(summ))

# საშინაო დავალება
# მომხმარებელს შემოატანინეთ ორისახელი და ისინი დაპრინტეთ
# #რომელ სახელშიც მეტი თნხმოვანია. (დააფორმარტეთ პასუხი)

intput1 = input("enter  words 1: ")    
intput2 = input("enter  words 2: ")   

Consonant_word1 = 0
Consonant_word2 = 0


for char in intput1:
    if char not in "aeiou":
        Consonant_word1 += 1

for char in intput2:
    if char not in "aeiou":
        Consonant_word2 += 1

if Consonant_word1 > Consonant_word2:      
    print ("in input1  is more Consonant_word and it is {})" .format(Consonant_word1))
elif Consonant_word1 < Consonant_word2: 
    print ("in input2  is more Consonant_word and it is {})" .format(Consonant_word2))
else:
    print("they have equl emount")