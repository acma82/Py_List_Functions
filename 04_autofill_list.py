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

lst = [[9,8,7],[4],[5,6]]
print("Original:",lst)
result = lf.autofill_data(lst, fill_value=9.8, update=False)
print("mylist=lst, fill_value=9.8, update=False")
print("Result  :",result)
print("Original:",lst)

print("\n---------------------------------------------------------------------------------\n")

print("Original:",lst)
result = lf.autofill_data(my_list=lst, fill_value=99, update=True)
print("mylist=lst, fill_value=99, update=True")
print("Result  :",result)
print("Original:",lst)


print("\n---------------------------------------------------------------------------------\n")
lst = [[1,2],['miguel','angel'],[1]]
print("Original:",lst)
result = lf.autofill_data(my_list=lst, fill_value=99, update=True)
print("mylist=lst, fill_value=99, update=True")
print("Result  :",result)
print("Original:",lst)

'''
----------------------------------------------------------------------------
   import list_functions as lf
   lf.autofill_data(list, str/int/float)

   This function will fill all the empty columns from the list.
   fill_chr is the chr to be used to fill those columns. It can be str,
   int, float, or bool. By default it's a str type (----).

example:
   lst = [[9,8,7],[4],[5,6]]
   print("Original:",lst)
   result = lf.autofill_data(lst, fill_value=9.8, type= lf.Fill_Type.NUMBER, update=False)
   print("mylist=lst, fill_value=9.8, type= \"number\", update=False")
   print("Result  :",result)
   print("Original:",lst)

   print("\n----------------------------------------------------------------\n")

   print("Original:",lst)
   result = lf.autofill_data(my_list=lst, fill_value=99, type=lf.Fill_Type.STRING, update=True)
   print("mylist=lst, fill_value=99, type= \"string\", update=True")
   print("Result  :",result)
   print("Original:",lst)
----------------------------------------------------------------------------
'''