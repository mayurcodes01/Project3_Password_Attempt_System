#Project 3 : Password Attempt System (3 attepmts at max.) 

password = "123"
attempts = 0
while attempts<3:
    entering_pwd=input("Enter your password: ")
    print()
    if entering_pwd==password:
        print("Password correct.")        
        print('~'*17)
        break
    else:
        attempts += 1
        print(f"Incorrect password Attempts left: {3-attempts}")
if attempts==3:
    print("No attempts left")
    
    print('-'*50,'X','-'*50)
