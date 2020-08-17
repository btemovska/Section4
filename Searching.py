shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break  #once it is found have the program no longer search

print("Item found at position {}".format(found_at)) #Item found at position 3



#what about if item is not on the list?
shopping_list2 = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find2 = "cheese"
found_at2 = None #none is a constant that represents nothing

if item_to_find2 in shopping_list2:
    found_at2 = shopping_list2.index(item_to_find2)
if found_at2 is not None:
    print("Item found at position {}".format(found_at2))
else:
    print("{} not found".format(item_to_find2)) #cheese not found
