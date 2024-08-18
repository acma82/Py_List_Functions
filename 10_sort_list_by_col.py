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

lst = [["Name", "Last","Dpt.","Age"],\
       ["Miguel","aguilar", "1",43],\
       [98,97,0],\
       [100,100,-10,2.58]]

 # multiple_items_multiple_rows      6[["5","12","9","4"]]
print("original: ",lst)
lista1 = lf.sort_by_col(my_list=lst, ref_col=2, fill_value=2500, type = "number", update=True)
print("result  :",lista1)
print("original: ",lst)

print("\n----------------------------------------------------------------------------\n")
lst = [["Name", "Last","Dpt.","Age"],\
       ["Miguel","Aguilar", "1",43],\
       ["Alex","Call",0],\
       ["Amilcar","Burelo",-10,2.58]]
print("original: ",lst)
lista1 = lf.sort_by_col(my_list=lst, ref_col=1, fill_value=2500, type = "string", update=True)
print("result  :",lista1)
print("original: ",lst)

