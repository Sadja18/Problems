def list_augmentor(list_1, list_2):
  """
  This function takes in two lists,
  list1 and list2.
  It arranges the elements in second list based on the changes in the indices of items in the first list when the first list is sorted
  """
  dict1,dict2 = dict(), dict()
  index = 0
  list1 = get_new_list(list_1)
  list2 = get_new_list(list_2)
  list3 = []
  for a in list1:
    dict1[a] = list1.index(a)

  list1.sort()

  for a in list1:
    dict2[a] = list1.index(a)

  for a in dict1.keys():
    i = dict2[a]
    list3.insert(i, list2[index])
    index += 1
  return list3

def sort_compare(list_a, list_b):
  """
  This function is used to show the difference between the sorted list and the augmented list
  """
  list_c = list_augmentor(list_a, list_b)
  print("Augmented list : ",list_c)
  listb = get_new_list(list_b)
  listb.sort()
  print("Sorted List : ",listb)

def get_new_list(list_a):
  """
  This function is needed to generate a copy of the original list.
  Otherwise, all the processing will happen on the original lists.
  """
  list_new = [s for s in list_a]
  return list_new

list1 = [8,6,9,1,4,7,3,2,5]
list2 = ['a','i', 'e', 'f', 'b','g', 'h' ,'c', 'd',]

sort_compare(list2, list1)
print()
sort_compare(list1, list2)
