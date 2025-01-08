from tabulate import tabulate
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
       

    def get_cost(self):
        
        with open("inventory.txt","r",encoding= "utf-8") as read:
            
            lines = read.readlines()

            price = []
            lines.pop(0)
            for line in lines:
                temp = line.strip()
                temp = temp.split(",") 
                price.append(temp[:4])
    
            for pr in price:
                self.cost = ' '.join(map(str, pr))
                print(self.cost)     

        
    def get_quantity(self):
        
        with open("inventory.txt","r",encoding= "utf-8") as read:
            
            lines = read.readlines()

            quantity = []
            lines.pop(0)
            for line in lines:
                temp = line.strip()
                temp = temp.split(",") 
                temp.pop(3)
                quantity.append(temp)
    
            for pr in quantity:
                self.quantity = ' '.join(map(str, pr))
            print(self.quantity)
       

    def __str__(self):

        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"
    

shoe_list = []

def read_shoes_data():

    shoe = Shoe("South Africa","SKU44386","Air Max 90","2300","20")
    
    try:
        with open("inventory.txt","r", encoding= "utf-8") as read:
            
            lines = read.readlines()
            
            lines.pop(0)
            for line in lines:
                temp = line.strip()
                temp = temp.split(",")
                shoe_list.append(shoe)
                sh = ' '.join(map(str,shoe_list))
            print(sh)
    except Exception:
        print("Error returning data.")
  
def capture_shoes():
    
    country = input("Enter country of the shoe: ")
    code = input("Enter the code of the shoe:  ")
    brand = input("Enter shoe brand: ")
    cost = int(input("Enter shoe price: "))
    quant = int(input("Enter number of pairs: "))

    with open("inventory.txt", "a",encoding= "utf-8") as append:
    
        append.write(f"{country},{code},{brand},{cost},{quant}\n")

def view_all():

    with open("inventory.txt", "r",encoding= "utf-8") as r:
    
        lines = r.readlines()
        new_line = []

        for line in lines:
            temp = line.strip()
            temp = temp.split(",")
            new_line.append(temp)

        headers = ("Country", "Code", "Product", "Price", "Qunatity")
        print(tabulate(new_line, headers = headers))


# The function below will find the lowest quantity of shoes
# then ask the user if they would like to add to the quantity.
def re_stock():
            
   with open("inventory.txt","r",encoding= "utf-8") as read:
            
        lines = read.readlines()

        quantity = []
        # First we remove the first line as it only contains
        # categories. Then append the quantity values to the
        # variable 'quantity'.
        lines.pop(0)
        for line in lines:
            temp = line.strip()
            temp = temp.split(",")
            quantity.append(temp[4])

        # This function will find the lowest quantity. The variable
        # 'new_quant' will convert the quantities in the list from
        # string to int, making it possible to use the 'min' function
        # to find the lowest quantity.  
        new_quant = [int(i) for i in quantity]
        low_quant = min(new_quant)
        for j in lines:

          k = j.strip()
          k = k.split(",")
        
          if str(low_quant) in k:
            print(j)
                       
        user = input("Enter 'y' to add to quantity or 'n' to exit: ")

        # The function below will allow the user to add to the quantity
        # of the lowest pair.
        if user == 'y':

            with open("inventory.txt", "w",encoding= "utf-8") as write:
                add_quant = int(input("Enter quantity: "))
                new_val = low_quant + add_quant

                for j in lines:

                    k = j.strip()
                    k = k.split(",")
        
                    if str(low_quant) in k:
                        k[-1] = str(new_val)
                    new_line = ','.join(map(str, k))
                    write.write(new_line + "\n")
             
        elif user == 'n':
            print("Goodbye!")

        else:
            print("Incorrect selection.")

# This function will allow the user to search for shoes
# by entering the shoe's code.
def seach_shoe():

    try:
        with open("inventory.txt","r",encoding= "utf-8") as read:
            
            lines = read.readlines()

            code_only = []
            lines.pop(0)
            for line in lines:
                temp = line.strip()
                temp = temp.split(",")
                code_only.append(temp[1])      
        
            code = input("Enter code of the pair: ").upper()
            for codes in lines:
                if code in codes:
                    print(codes)
                else:
                    print(f"{code} not found.")
    except Exception:
        print("Incorrect input.")
        
# The function below will calculate each pair's value by
# multiplying the quantity with the price.
def value_per_item():

    with open("inventory.txt","r",encoding= "utf-8") as read:
            
        lines = read.readlines()

        price = []
        quantity = []
        new_lines = []
        lines.pop(0)
        for line in lines:
            temp = line.strip()
            temp = temp.split(",")
            quantity.append(temp[4]) 
            price.append(temp[3])
            new_lines.append(temp) 
  
        # This function will return the quantity and price as 
        # two lists of integers.
        int_quant = [int(i) for i in quantity]
        float_price = [int (j) for j in price]

        # The function below will calculate the value of each 
        # pair using a for loop and apeending the values to
        # the 'tot_val' empty list.
        tot_val = []
        for j in range(len(int_quant)):
            tot_val.append(int_quant[j] * float_price[j])
   
        new = ' '.join(map(str, tot_val))
        new_str = list(new.split(" "))
    
        str_line = []

        # This function will join the two lists into one string.
        for i in range(len(lines)):

            new_line = lines[i] + "," +  new_str[i]
            ne = list(new_line.split(","))
            str_line.append(ne)
        
        header = ("Country", "Code", "Product", "Cost", "Quantity", "Value")
        print(tabulate(str_line, headers = header))
        

def highest_qty():

    with open("inventory.txt","r",encoding= "utf-8") as read:
            
        lines = read.readlines()

        quantity = []
        lines.pop(0)

        for line in lines:
            temp = line.strip()
            temp = temp.split(",")
            quantity.append(temp[4])

        new_quant = [int(i) for i in quantity]
        max_quant = max(new_quant)
        for j in lines:

          k = j.strip()
          k = k.split(",")
        
          if str(max_quant) in k:
            print("For sale: ",j)
                    
shoe = Shoe("South Africa","SKU44386","Air Max 90","2300","20")
while True:

    try:
        menu = int(input("Select option:\n" 
                     "1. To view the cost of the shoes\n"
                     "2. To get the quantity of the shoes\n"
                     "3. To get the data of the shoes\n"
                     "4. To add new shoe data\n"
                     "5. To view all the shoes in stock\n"
                     "6. To see lowest quantity shoe and/or add\n"
                     "7. To search for specific shoe\n"
                     "8. To view value of shoes\n"
                     "9. To get highest quantity shoe\n"
                     "-1. To exit:  "))

        if menu == 1:

            shoe.get_cost()

        elif menu == 2:

            print(shoe.get_quantity())

        elif menu == 3:

            read_shoes_data()

        elif menu == 4:

            capture_shoes()

        elif menu == 5:

            view_all()

        elif menu == 6:

            re_stock()

        elif menu == 7:

            seach_shoe()

        elif menu == 8:

            value_per_item()

        elif menu == 9:

            highest_qty()
    
        elif menu == -1:
            print("Goodbye!")
            exit()
        else:
            print("Incorrect selection. Please try again.")

    except ValueError:
        print("Incorrect value entered.")

