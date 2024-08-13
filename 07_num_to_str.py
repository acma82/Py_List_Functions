import copy
import HotListFuns as fp

# Options                          Results                           Cases
lst = "hello"                    # incorrect_variable_type             1
# lst = []                         # empty_list                        2
# lst = [5]                        # one_item_no_row                   3
# lst = [[1]]                      # one_item_one_row                  4
# lst = [1,2,3,4,5,6]              # multiple_items_no_row             5
# lst = [4,5]

# lst = [[1,2],[3,4],[5,6],[7,8]]  # multiple_items_multiple_rows      6
# lst = [[9,8,7,7],[4],[5,6]]                                           
# lst = [10,[50],[250],["H"],100]  # mix_items                         7
# lst = [5,[50,40],45] 
# lst = [[5],6,40,[45]]                                                 
# lst = [[1,2,3,4,5,6]]             # multiple_items_one_row           8


# def num2str(my_list, fill_chr, update=False):
#    tempo = []; str_list = []
   
#    n_rows = len(my_list)
#    n_cols = 0
#    for n in my_list:
#       if len(n) > n_cols:
#          n_cols = len(n)

#    for row in range(n_rows):
#       for col in range(n_cols):
#          try:
#             tempo.append(str(my_list[row][col]))
#          except:
#             tempo.append(str(fill_chr))
#       str_list.append(tempo)
#       tempo = []


   

#    if update == True:
#       my_list.clear()
#       [my_list.append(n) for n in str_list]
#    else:
#       pass
 
#    return str_list

# print(lst)
# resultado = num2str(lst, "99", True)
# print(resultado)
# print(lst)

print(lst)
result = fl.num2str(lst, 99, False)
# result = fl.num2str(lst, 99, True)
print(result)
print(lst)

'''
----------------------------------------------------------------------------
import fancylist as fl
result = fl.num2str(data_list, fill_chr=----, update=False)

This Function convert every single item in the list to string type.


Options                          Cases
lst = "hello"                      1
lst = []                           2
lst = [5]                          3
lst = [[1]]                        4
lst = [1,2,3,4,5,6]                5
lst = [[1,2],[3,4],[5,6]]          6
lst = [[1],[4],[5,6]]              7
lst = [[9,8,7],[4],[5,6]]          8
lst = [10,[50],[250],["H"],100]    9
lst = [[1,2,3,4,5,6]]              10
----------------------------------------------------------------------------
'''