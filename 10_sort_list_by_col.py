import HotListFuns as fl
fun = fl.FancyList()
# Options                          Results                           Cases
# lst = "hello"                    # incorrect_variable_type           1
# lst = []                         # empty_list                        2
# lst = [5]                        # one_item_no_row                   3
# lst = [[1]]                      # one_item_one_row                  4
# lst = [1,2,1,4,15,"6t"]              # multiple_items_no_row             5
# lst = [4,5]

# lst = [[1,2],[9,4],[5,6],[7,8]]  # multiple_items_multiple_rows      6
lst = [[9,8,7,7],[4,0,],[5,6,5],[1,108,99,99]]                                           
# lst = [10,[50],[250],["H"],100]  # mix_items                         7
# lst = [5,[50,40],45] 
# lst = [[5],6,40,[45]]                                                 
# lst = [[10,2,9,4,5,"4.6"]]             # multiple_items_one_row           8


#my_list = ["miguel", "4","angel", "2","aguilar", "cuesta","----"] #[[1,2],[3,4],[5,6],[1,8]]  # multiple_items_multiple_rows      6[["5","12","9","4"]]
print(lst)
lista1 = fl.sort_by_col(my_list=lst, ref_col=2, fill_chr="2.5", type = "number", update=True)
print(lista1)
print(lst)


# fun.print_fancy_list(lista1)
# print()
# fun.print_fancy_list(lst)


# print(lst)
# lista1 = fl.sort_by_col(my_list=lst, ref_col=2, fill_chr=11, type = "number", update=False)
# print(lista1)

# fun.print_fancy_list(lista1)
# print()
# fun.print_fancy_list(lst)import HotListFuns as fl

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
lst = [["t",2],["-4",3],["-5.5","6.0",5]]

# lst = ["-10.5","-40",["50"],[250],["H"],"10"] # mix_items                           8



# number_list = fl.str2num(my_list=lst, update=False, force_fill_chr=False)
# print(number_list)

# def number(n):
#    try:
#       numb = int(n)
#       return numb
#       return "integer"
#    except:
#       try:
#          numb = float(n)
#          return numb
#          return "float"
#       except:
#          return 0
#          return "string"

# result = number("-5") + 1
# print(result)
# mensaje = fl.ins_space(4)+"Hello!"+fl.ins_space(4)
# fl.send_msg(mensaje, 32, 0, True, 4, 2)
# print()
# fl.send_msg(mensaje, 1, 234, True, 4, 2)
# fl.send_msg(mensaje, 1, 15, True, 4, 2)
print(lst)
result = fl.str2num(my_list=lst, fill_chr=99, update=False)
print(result)
print(lst)
result = fl.str2num(my_list=lst, update=False)
print(result)

# print(lst)
# lista1 = fl.sort_by_col(my_list=lst, ref_col=1, fill_chr=7, update=True)
# print(lista1)

# fun.print_fancy_list(lista1)
# print()
# fun.print_fancy_list(lst)
# print(lst)

# fl.str2num(lst, update=True)
# print(lst)
# fl.sort_by_col(lst, ref_col=1,update=True)
# print(lst)
# fun.print_fancy_list(lst)



# lst = [[9,8,7,7],[4,0,1],[5,6,5],[1,108,99,99]]  
# fl.sort_by_col(lst, ref_col=1,update=True)
# print(lst)
# print()

# fl.str2num(lst, update=True)
# print(lst)
# print()

# fl.sort_by_col(lst, ref_col= 1, type="number", update=True)
# print(lst)

# list_t = ["miguel", "4","angel", "2","aguilar", "cuesta","----"]
# list_t = fl.sort_by_col(list_t)
# fun.print_fancy_list(list_t)

# exam = [1,2,3,"k",6]
# print(sorted(exam))