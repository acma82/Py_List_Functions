import copy
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

lst = [[1,2],[3,4],[5,6],[0]]
print("Original:",lst)
# result = lf.num_to_str(lst, "199", False)
result = lf.num_to_str(my_list=lst, fill_value=None, update=True)
print("Result  :",result)
print("Original:",lst)



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