list1 = [1, 2, 3, 4, 5, 6]
print("----- Access List -----")
print(f"list1[3] = {list1[3]}, list1[-2] = {list1[-2]}")
print("---- update List ----")
list1[3],list1[-2] = 55, 88
print(f"list1[3] = {list1[3]}, list1[-2] = {list1[-2]}")

print("---- delete item from list ----")
print(list1)
print(f"{list1.pop()} delete from last now the list is {list1}")
print(f"{list1.pop(0)} delete from starting now the list is {list1}")
print(f"removing any existing element 55 ",end="")
list1.remove(55)
print(f"now the list is {list1}")
print(f"index of 88 is {list1.index(88)}")


