import HotListFuns as fp
fun = fl.FancyList()

# Options                          # Results                           Cases
# lst = "hello"                    # incorrect_variable_type             1
# lst = []                         # empty_list                          2
# lst = [5]                        # one_item_no_row                     3
# lst = [[1]]                      # one_item_one_row                    4
# lst = [1,2,3,4,5,6]              # multiple_items_no_row               5     this one
# lst = [4,5]
# lst = [[1,2],[3,4],[5,6],[7,8]]  # multiple_items_multiple_rows        6       this one
lst = [[1],[4],[5,6]]                                                          #this one
# lst = [10,[50],[250],["H"],100]  # mix_items                           7
# lst = [5,[50,40],45] 
# lst = [[5],6,40,[45]]                                                  #        this one
# lst = [[1,2,3,4,5,6]]              # multiple_items_one_row              8

print("original_list: ", lst)
fun.print_fancy_list(lst)

'''
transpose, when autofill is false it will cut the data
when autofill is true it will fill the empty spot with the fill_chr 
'''

#transpose_l1 = fl.transpose(lst, update= True, autofill=False)
transpose_l1 = fl.transpose(lst, update= True, autofill=True, fill_chr="910", type="number")
print("transpose_l1 : ", transpose_l1)
fun.print_fancy_list(transpose_l1)

print("original_list: ", lst)
fun.print_fancy_list(lst)

transpose_l2 = fl.transpose(transpose_l1)
print("transpose_l2 : ", transpose_l2)
fun.print_fancy_list(transpose_l2)


transpose_l3 = fl.transpose(transpose_l2, type = "number")
print("transpose_l3 : ", transpose_l3)
fun.print_fancy_list(transpose_l3)

print("original_list: ", lst)
fun.print_fancy_list(lst)


listita = [["Miguel", "Aguilar", "Cuesta"],[1,2,3],[7,9]]
print(listita)
print(fl.transpose(listita, True, "100", False, "number"))


'''
----------------------------------------------------------------------------
   import fancylist as fl
   fl.transpose(list, bool, str, bool)

   This function get the transpose list.

   update is used to replace original list with the transpose list.
   update is set to False to keep the original list and save
   the new list into another variable.

   Note: When the list is not square or rectangular, the autofill will be
         used. If the autofill is set to False, some data will be lost.
         If the autofill is set to True, the fill_chr will be used
         to fill those spot needed. The fill_chr can be replace as 
         needed, by default is set to four dash. 

      
Options                          
lst = [1,2,3,4,5,6]
lst = [[1,2],[3,4],[5,6],[7,8]]
lst = [[1,2,3,4,5,6]]
lst = [[1],[4],[5,6]]
lst = [5,[50,40],45]
lst = [[5],6,40,[45]]

   Example:
         print("original_list: ", lst)
         fun.print_fancy_list(lst)

         transpose_l1 = fl.transpose(lst, update= True, autofill=True)
         
         print("transpose_l1 : ", transpose_l1)
         fun.print_fancy_list(transpose_l1)

         print("original_list: ", lst)
         fun.print_fancy_list(lst)

         transpose_l2 = fl.transpose(transpose_l1)
         print("transpose_l2 : ", transpose_l2)
         fun.print_fancy_list(transpose_l2)


         transpose_l3 = fl.transpose(transpose_l2)
         print("transpose_l3 : ", transpose_l3)
         fun.print_fancy_list(transpose_l3)
----------------------------------------------------------------------------
'''