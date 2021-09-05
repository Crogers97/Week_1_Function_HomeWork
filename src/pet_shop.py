# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(name_of_pet):
    return name_of_pet["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_status):
    return pet_status["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_list, breed):
    result_breed=[]
    for pet in pet_list["pets"]:
        if pet["breed"] == breed:
            result_breed.append(pet)
    return result_breed

def find_pet_by_name(pet_list, name):
    for pet in pet_list["pets"]:
        if pet["name"] ==name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, amount):
    customers["cash"] -= amount

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)
    
def customer_can_afford_pet(customers, new_pet):
     return customers ["cash"] >= new_pet["price"]

def sell_pet_to_customer(pet_shop, pets, customers):
    if pets != None and customer_can_afford_pet(customers, pets):
        add_pet_to_customer(customers, pets)
        increase_pets_sold(pet_shop, 1)
        remove_customer_cash(customers, pets["price"])
        add_or_remove_cash(pet_shop, pets["price"])

    
   
                    


    



    


    

         
    
    
    
