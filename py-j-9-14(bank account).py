

balance = 0
transactions = []

while True:
    menu = input("1.variz 2.bardasht 3.namayesh mojoodi 4.namayesh tarakonesh ha 5.majmoe variz ha 6.exit: ")
    
    match menu:
        case "1":
            amount = float(input("mablagh variz: "))
            if amount > 0:
                balance += amount
                transactions.append(f"+{amount}")
                print("variz anjam shod. mojoodi:", balance)
            else:
                print("mablagh bayad mosbat bashe!")
            
        case "2":
            amount = float(input("mablagh bardasht: "))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    transactions.append(f"-{amount}")
                    print("bardasht anjam shod. mojoodi:", balance)
                else:
                    print("mojoodi kafi nist!")
            else:
                print("mablagh bayad mosbat bashe!")
            
        case "3":
            print("mojoodi feli:", balance)
            
        case "4":
            print("tarakonesh ha:")
            if not transactions:
                print("hich tarakoneshi sabt nashode!")
            else:
                for t in transactions:
                    print(t)
            
        case "5":
            sum_variz = 0
            for t in transactions:
                if t.startswith("+"):
                    sum_variz += float(t[1:])
            print("majmo variz ha:", sum_variz)
            
        case "0":
            print("exit")
            break
            
        case _:
            print("gozine eshtebah!")
            # break