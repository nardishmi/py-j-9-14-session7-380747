

products = []
prices = []

while True:
    menu=("1.add Product 2.Show Shopping list 3.remove Product 4.Count Products 5.Search Product 6.Total Price 7.Exit :")
    while True:
        match menu:
            case "1":
                product=input("Enter product name: ")
                price=int(input("Enter product price: "))
                products.append(product)
                prices.append(price)
                print("Product Added Successfully.")
            case "2":
                for i in range(len(products)):
                    print(products[i], ":", prices[i])
            case "3":
                product=input("Enter product name: ")
                if product in products:
                    index=products.index(product)
                    products.pop(index)
                    prices.pop(index)
                    print("Product Removed Successfully.")
                else:
                    print("Product Not Found.")
            case "4":
                print("Number of Products:", len(products))
            case "5":
                product=input("Enter product name: ")
                if product in products:
                    print("Product Found.")
                else:
                    print("Product Not Found.")
            case "6":
                print("Total Price:", sum(prices))
            case "7":
                print("goodbye!")
                break
            case _:
                print("invalid Choice.")
                