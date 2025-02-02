# import csv

# class Item:

#     all=[]
#     discount_rate= 0.8

    
#     def __init__(self, name, price: float, quantity=0):

#         assert price >= 0
#         assert quantity >=0

#         self.name = name
#         self.price = price
#         self.quantity = quantity


#         # action to execute
#         Item.all.append(self)

#     def inclement_quantity(self, amount):
#         if amount>0:
#             self.quantity+=amount
#         else:
#             print("the quantity must be positive and not zero")

#     def total_price(self):
#         return self.price * self.quantity
    
#     def discount (self):
#         return self.price * self.discount_rate
    
# # item1 = Item("Phone", 2000, 8)
# # # # print(item1.name, item1.price)

# # # # Item.inclement_quantity =int(input("enter the new stock"))
# # # # print(f"the new stock is{Item.inclement_quantity}") 

# # # print(item1.total_price())



# # # print(Item.__dict__) #used to print all the atribute of a particular object
# # # print(item1.__dict__)

# # #discount
# # item1.discount()
# # item1.discount_rate= 0.4
# # print(item1.discount())
    
#     @classmethod
#     def instantiate_from_csv(cls):
#         cls.all=[]
#         with open("C:/Users/Derrick/alx/alx_be_python/store_management/items.csv", "r") as new_ls:
#             reader= csv.DictReader(new_ls)
#             items=list(reader)

#         for item  in items:
            
#             Item(
#                 name= item.get('name'),
#                 price= float(item.get(' price')),
#                 quantity= float(item.get(' quantity'))
#             )
            

#     def __repr__(self):
#         return f"Item('{self.name}', {self.price}, {self.quantity})"
# # item1 = Item("Phone", 100, 1)
# # item2 = Item("Laptop", 1000, 3)
# # item3 = Item("Cable", 10, 5)
# # item4 = Item("Mouse", 50, 5)
# # item5 = Item("Keyboard", 75, 5)

# # for instance in Item.all:
# #     print(instance.name, instance.price)

# # print(Item.all)

# Item.instantiate_from_csv()
# print(Item.all)



# inheritance


# class Animal: #parent class
#   def __init__(self, name):
#     self.name = name

#   def make_sound(self):
#     print("Generic animal sound")

# class Dog(Animal):
#   def make_sound(self):
#     print(f"{self.name} says Woof!")

# lassie = Dog("Lassie")
# lassie.makes_sound()  # Output: Woof!



# @classmethod

class person:
    count = 0

    def __init__(self, name):
        self.name= name
        person.count +=1

    @classmethod
    def display_count(cls):
        print(f"Total persons created: {cls.count}")


person1= person("Alice")
person2= person("COCO")
person.display_count