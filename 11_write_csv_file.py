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

# lst = "hello"
lst = []
# lst = ["Miguel"]
# lst = [["Miguel"]]

# lst = [1,2,3,4]
# lst = [[1,2,3,4]]

# lst = [[1,2],[3,4]]
# lst = [[1],[4],[5,6]]

# lst = [["Name","Last","Age"],["Miguel","AC",42],["Alex","Call",32],["Amilcar","Burelo",43]]

path=lf.write_csv_file(lst)
print(path)

