shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item !="spam":
#         print("Buy " + item)


for item in shopping_list:
    if item == "spam":
        continue #milk, pasta, egs, bread, rice
    print("Buy " + item)


for item in shopping_list:
    if item == "spam":
        break #milk, pasta, eggs and that is it
    print("Buy " + item)
