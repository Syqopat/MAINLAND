import random



while True:
    print("Welcome to min to sec!\nType minute with no dots like (2.30m = 230)")



    num1 = int(input("NUMBER : "))
    
    calc1 = (num1 // 100)
    num2 = (calc1 * 40)
    calc3 = (num1-num2)

    print("\n", calc3)

    sel = input("Do you want to exit? (y/n)").lower()
    if sel != "y" and sel != "n":
        print("Invalid input!")
    elif sel == "n":
        continue
    else:
        break
     
        
