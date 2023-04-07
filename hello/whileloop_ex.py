# name = 'Jims@123'
# guess = input("So I'm thinking of person's name.Try to guess it:")
# pos = 0
# while guess != name and pos<len(name):
#     print("Nope,that's not it! Hint: letter", end='')
#     print(pos+1,"is",name[pos]+".",end='')
#     guess = input("Guess again!")
#     pos=pos+1
# if pos == len(name) and name!=guess:
#     print("Too bad, you couldn't get it. The name was",name+".")
# else:
#     print("\nGreat, you got it in",pos+1,"guesses!")
#     
# 
# for i in [12,16,17,24,29]:
#     if i%2==1:
#         break;
#     print(i)
# print("done")

# Create a infinity loop to get name by age 
# Step 1:- create first while loop for search 
# Step 2:-  inside first loop create loop to create a dictionary for five family members with their age.
# Step 3: after completion of creating dictionary print dataset is ready to fatch name by age 
# Step 4. Get age from user and print their name* (key)
# 
# Step5 :- create condition if user wants to stop loop  
# 
# 
# Step 6:- ones loop stopped print thanks for using python ...
# 
# *If two names contains same age return both names

for i in [12,16,17,24,29,30]:
    if i%2==1:
        continue;
    print(i)
print("done")