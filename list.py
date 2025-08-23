my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending elements:", my_list)

my_list.insert(1, 15)
print("After inserting 15 at second position:", my_list)

my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

my_list.pop()
print("After removing last element:", my_list)

my_list.sort()
print("After sorting in ascending order:", my_list)


index_of_30 = my_list.index(30)
print("Index of value 30 in my_list:", index_of_30)
