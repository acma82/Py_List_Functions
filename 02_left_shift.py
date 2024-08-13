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
list_1 = [[1,2,3,4,5,6]]

# Left Shift List
#---------------------------------------------------------------------------
print("original:", list_1, end=""); print("   left_shift 2, update=False")
newlist = lf.left_shift(list_1, 2, False)
print("new list:",newlist)
print("original:", list_1)

print("\n---------------------------------------------------------------------------------\n")

print("original:", list_1,end=""); print("   left_shift 2, update=True")
newlist = lf.left_shift(my_list=list_1, shift= 2, update= 1)
print("new list:",newlist)
print("original:", list_1)


'''
----------------------------------------------------------------------------
   import list_functions as lf

   This function shifts the elements in a list to the left.

   Update set to true is used to save the actual list with the shifted elements.
   Update defaults to false, and false is used if we wish to keep the original list
   and save the new list as another variable.
      
Options                             Results                   Cases
list_1 = "hello"                    incorrect_variable_type        1
list_1 = []                         empty_list                     2
list_1 = [5]                        one_item_no_row                3
list_1 = [[1]]                      one_item_one_row               4
list_1 = [1,2,3,4,5,6]              multiple_items_no_row          5
list_1 = [[1,2],[3,4],[5,6]]        multiple_items_multiple_rows   6
list_1 = [[1],[4],[5,6]]
list_1 = [10,[50],[250],["H"],100]  mix_items                      7
list_1 = [[1,2,3,4,5,6]]            multiple_items_one_row         8
   
Example:
   print("original:", list_1, end="")
   print("   left_shift 2, update=False")
   newlist = lf.left_shift(list_1, 2, False)
   print("new list:",newlist)
   print("original:", list_1)

   print("\n----------------------------------------------------------------\n")

   print("original:", list_1,end="")
   print("   left_shift 2, update=True")
   newlist = lf.left_shift(my_list=list_1, shift= 2, update= 1)
   print("new list:",newlist)
   print("original:", list_1)
----------------------------------------------------------------------------
'''