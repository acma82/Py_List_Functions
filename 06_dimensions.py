import list_functions as lf

# Options                          # Results                           Cases
# lst = "hello"                    # incorrect_variable_type             1
# lst = []                         # empty_list                          2
# lst = [5]                        # one_item_no_row                     3
# lst = [[1]]                      # one_item_one_row                    4
# lst = [1,2,3,4,5,6]              # multiple_items_no_row               5
# lst = [4,5]
# lst = [[1,2],[3,4],[5,6],[7,8]]  # multiple_items_multiple_rows        6
lst = [[9,8,7],[4],[5,6]]                                                
# lst = [10,[50],[250],["H"],100]  # mix_items                           7
# lst = [5,[50,40],45] 
# lst = [[5],6,40,[45]]                                                  
# lst = [[1,2,3,4,5,6]]              # multiple_items_one_row            8

rows, cols = lf.dimensions(lst, "max")
print("rows: ", rows, "     cols: ", cols)
rows, cols = lf.dimensions(my_list=lst, option=lf.Length_Col.MAX)
print("rows: ", rows, "     cols: ", cols)


print()
rows, cols = lf.dimensions(lst, "min")
print("rows: ", rows, "     cols: ", cols)
rows, cols = lf.dimensions(my_list=lst, option=lf.Length_Col.MIN)
print("rows: ", rows, "     cols: ", cols)

'''
----------------------------------------------------------------------------
   import fancylist as fl

   This function return the number of rows and cols in a list.
   It will take the longest number for the columns as the case 7 or 8.
   However, it can be adjusted to use the smallest number for the columns.

      
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
   
   Example:
            rows, cols = fl.dimensions(lst)
            print("rows: ", rows, "     cols: ", cols)
----------------------------------------------------------------------------
'''
