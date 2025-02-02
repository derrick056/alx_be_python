# import csv

# # with open('C:/Users/Derrick/alx/alx_be_python/store_management/items.csv','r') as csv_file: # to read the file
# #     csv_reader = csv.reader(csv_file)

# #     # next(csv_reader) # to skip the field names

# #     with open('new_names.csv', 'w') as new_file:
# #         csv_write= csv.writer(new_file,delimiter='\t')
        
# #         for line in csv_reader:
# #             # print (line[2])
# #             csv_write.writerow(line)

 


# #using the dictionary reader

# with open('C:/Users/Derrick/alx/alx_be_python/store_management/items.csv','r') as csv_file: # to read the file
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         print(line['name'])
#     # with open('new_names.csv', 'w') as new_file:
#     #     fieldnames= ['name', ' price']
#     #     csv_write= csv.DictWriter(new_file, fieldnames=fieldnames,delimiter='\t')
#     #     csv_write.writeheader()
        
#     #     for line in csv_reader:
#     #         # print (line[2])
#     #         del line[' quantity']
#     #         csv_write.writerow(line)

# decorators



def turn_on(func):
    def key(*args, **kwargs):
        print("first turn on the engine")
        func(*args, **kwargs)
    return key

def warm_start(engine):    
    def warm(*args, **kwargs):
        print("its warm now")
        engine(*args, **kwargs)
    return warm

@turn_on
@warm_start
def move_the_car(car):
    print(f"{car} on the move")

move_the_car("hellcat")