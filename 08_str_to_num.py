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

# Options                                       # Results                           Cases
# lst = "hello"                                 # incorrect_variable_type             1
# lst = []                                      # empty_list                          2

# lst = ["5"]                                   # one_item_no_row                     3
# lst = ["-5.7"]                                # one_item_no_row                     3

# lst = [["1"]]                                 # one_item_one_row                    4
# lst = [["-1.1"]]                              # one_item_one_row                    4

# lst = ["-1.5",2,"3","4.5","5",6]              # multiple_items_no_row               5
# lst = ["4",5]

# lst = [["-1.1","2.5","-3","4",5,6]]           # multiple_items_one_row              6

# lst = [["1",2],["3.3",4],["-5",6],["-7.7",8]] # multiple_items_multiple_rows        7
# lst = [["t",2],["-4",3],["-5.5","6.0",5]]

lst = ["-10.5","-40",["50"],[250],["H"],"10"] # mix_items                           8


print("original: ", lst)
number_list = lf.str_to_num(my_list=lst, fill_value="0.1", update=False)
print("result:",number_list)
print("original: ", lst)

print("\n---------------------------------------------------------------------------------\n")

print("original: ", lst)
number_list = lf.str_to_num(my_list=lst, fill_value="0.1", update=True)
print("result:",number_list)
print("original: ", lst)