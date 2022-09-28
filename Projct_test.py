# Category 2€ 5€ 10€ 20€ 50€ 100€ 200€ 500€
print("Please enter from categories (50,100,200,500) Euro")
money = int(input("Please enter the money: " ))
if money < 38 :
    print("Not enough")
    
else:
    if money in [50,100,200,500]:
        current = money - 38 
        print(f"Current  (total): ({current} €) ")
        after_mod100 = current%100
        Category_100 = current - after_mod100
        print(f"Category (100 €): ({int(Category_100/100)}) *100€  or {Category_100} Euro")
        after_mod50 = after_mod100 % 50
        Category_50 = after_mod100 - after_mod50
        print(f"Category  (50 €): ({int(Category_50/50)}) *50€   or {Category_50} Euro")
        after_mod10=after_mod50%10
        Category_10 = after_mod50 - after_mod10
        print(f"Category  (10 €): ({int(Category_10/10)}) *10€   or {Category_10} Euro")
        print(f"Category   (2 €): ({int(after_mod10/2)}) *2€    or {after_mod10} Euro")
        print("Thanks for using our services")
        
    else:
        print("Sorry,You must enter from the categories (50,100,200,500) Euro")   
        
        # Test (1) 
        # Please enter the money: 200
        # Current  (total): (162 €) 
        # Category (100 €): (1) *100€  or 100 Euro
        # Category  (50 €): (1) *50€   or 50 Euro 
        # Category  (10 €): (1) *10€   or 10 Euro 
        # Category   (2 €): (1) *2€    or 2 Euro  
        # Thanks for using our services



# Project With Function

def sodaMachine(Money):      
    
    money = int(Money)
    print(money)
    if money < 38 :
        print("Not enough")
        
    else:
        if money in [50,100,200,500]:
            current = money - 38 
            print(f"Current  (total): ({current} €) ")
            after_mod100 = current%100
            Category_100 = current - after_mod100
            print(f"Category (100 €): ({int(Category_100/100)}) *100€  or {Category_100} Euro")
            after_mod50 = after_mod100 % 50
            Category_50 = after_mod100 - after_mod50
            print(f"Category  (50 €): ({int(Category_50/50)}) *50€   or {Category_50} Euro")
            after_mod10=after_mod50%10
            Category_10 = after_mod50 - after_mod10
            print(f"Category  (10 €): ({int(Category_10/10)}) *10€   or {Category_10} Euro")
            print(f"Category   (2 €): ({int(after_mod10/2)}) *2€    or {after_mod10} Euro")
            print("Thanks for using our services")
            
        else:
            print("Sorry,You must enter from the categories (50,100,200,500) Euro")   

# Test (1) 
sodaMachine(200)  

print("\n") 

# Test (2)       
sodaMachine(20)          
         