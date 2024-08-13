import list_functions as lf

msg = f'''
   Options                             Results                           Cases
   list_1 = "hello"                    incorrect_variable_type             1
   list_1 = []                         empty_list                          2
   list_1 = [5]                        one_item_no_row                     3
   list_1 = [[1]]                      one_item_one_row                    4
   list_1 = [1,2,3,4,5,6]              multiple_items_no_row               5
   list_1 = [[1,2],[3,4],[5,6]]        multiple_items_multiple_rows        6
   list_1 = [[1],[4],[5,6]]
   list_1 = [10,[50],[250],["H"],100]  mix_items                           7
   list_1 = [[1,2,3,4,5,6]]            multiple_items_one_row              8 
   '''
print(msg)

lst = [[1,2],[3,4],[5,6],[7,8]]
print("original: ", lst,end=""); print("   update=False, pos1=0, pos2=2")
newlist = lf.swap(my_list=lst, update= False, pos1= 0, pos2=2)
print("new list: ",newlist)
print("original: ", lst)

print("\n---------------------------------------------------------------------------------\n")

print("original: ", lst,end=""); print("   update=true, pos1=3, pos2=0")
newlist = lf.swap(my_list=lst, update=True, pos1=3, pos2=0)
print("new list: ",newlist)
print("original: ", lst)
'''
----------------------------------------------------------------------------
   import list_functions as lf

   This function swaps two elements in a list.

   Update set to true is used to save the actual list with the swapped elements.
   Update defaults to false, and false is used if we wish to keep the original list
   and save the new list as another variable.
      
Options                             Results                   Cases
lst = "hello"                    incorrect_variable_type        1
lst = []                         empty_list                     2
lst = [5]                        one_item_no_row                3
lst = [[1]]                      one_item_one_row               4
lst = [1,2,3,4,5,6]              multiple_items_no_row          5
lst = [[1,2],[3,4],[5,6]]        multiple_items_multiple_rows   6
lst = [[1],[4],[5,6]]
lst = [10,[50],[250],["H"],100]  mix_items                      7
lst = [[1,2,3,4,5,6]]            multiple_items_one_row         8
   
   Example:
   lst = [[1,2],[3,4],[5,6],[7,8]]
   print("original: ", lst,end="")
   print("   update=False, pos1=0, pos2=2")
   newlist = lf.swap(my_list=lst, update= False, pos1= 0, pos2=2)
   print("new list: ",newlist)
   print("original: ", lst)

   print("\n----------------------------------------------------------------\n")

   print("original: ", lst,end="")
   print("   update=true, pos1=3, pos2=0")
   newlist = lf.swap(my_list=lst, update=True, pos1=3, pos2=0)
   print("new list: ",newlist)
   print("original: ", lst)
----------------------------------------------------------------------------
'''