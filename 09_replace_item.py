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

lst = [[5],6,40,[45]]

print("Original:",lst)
result = lf.replace(my_list=lst, ref_value=[45], new_value=0.85, update=False)
print("Result  :",result,end="  "); print("mylist=lst, ref=[45], new_value=0.085, update=False")
print("Original:",lst)

print("\n---------------------------------------------------------------------------------\n")

print("Original:",lst)
result = lf.replace(my_list=lst, ref_value=40, new_value=0.85, update=True)
print("Result  :",result,end="  "); print("mylist=lst, ref=45, new_value=0.85, update=False")
print("Original:",lst)

