import list_functions as lf

#-------------------------------------------------------------------------------------
# Bool, Integer, Float, Complex, and String                                          -
#-------------------------------------------------------------------------------------
print("\033[48;5;99m                                                           \033[0m")
print("  BOOL")
b = False; result = lf.data_to_list(b)
print(result)
print()


print("\033[48;5;99m                                                           \033[0m")
print("  INTEGER")
b = 55; result = lf.data_to_list(b)
print(result)
print()


print("\033[48;5;99m                                                           \033[0m")
print("  FLOAT")
b = 45.98; result = lf.data_to_list(float)
print(result)
print()


print("\033[48;5;99m                                                           \033[0m")
print("  COMPLEX")
b = 5+6j; result = lf.data_to_list(b)
print(result)
print()


print("\033[48;5;99m                                                           \033[0m")
print("  STRING")
b = "Chicho...!"; result = lf.data_to_list(b)
print(result)
print()



#-------------------------------------------------------------------------------------
# dictionary to list                                                                 -
#-------------------------------------------------------------------------------------
print("\033[48;5;99m                                                           \033[0m")
print("  DICTIONARY")
dict_1 = {"Name":"Miguel Angel","Last":"Aguilar Cuesta","Country":"Mexico","Age":"42"}
list_dict = lf.dict_to_list(data=dict_1,key_title=None, value_title="My Values")
for dato in list_dict:
      print(dato)
print()
#-------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------
# set to list                                                                        -
#-------------------------------------------------------------------------------------
print("\033[48;5;99m                                                           \033[0m")
print("  SET  ")
set_1 = {1,3,5,7,9}
list_set = lf.set_to_list(data=set_1, header="None", layout=lf.Layout.VERTICAL)
# list_set = lf.set_to_list(data=set_1, header="None", layout="vertical")
# list_set = lf.set_to_list(set_1, "None", "horizontal")
print(list_set)
print()


#-------------------------------------------------------------------------------------
# frozenset to list                                                                  -
#-------------------------------------------------------------------------------------
print("\033[48;5;99m                                                           \033[0m")
print("  FROZENSET  ")
print("\n  dictionary to frozenset")
example_dictionary = {"key1":"value1", "key2":"value2", "key3":"value3"}
frozen_set_d = frozenset(example_dictionary)
print(frozen_set_d)

print("\n  list to frozenset")
example_list = [1,2,3,4,5]
frozen_set_l = frozenset(example_list)
print(frozen_set_l)

print("\n  tuple to frozenset")
example_tuple = (1,2,3,4,5)
frozen_set_t = frozenset(example_tuple)
print(frozen_set_t)

print("\n  set to frozenset")
example_set = {1,2,3,4,5}
frozen_set_s = frozenset(example_set)
print(frozen_set_s)

print("\n  frozenset to list")
d = lf.set_to_list(frozen_set_d)
l = lf.set_to_list(frozen_set_l)
t = lf.set_to_list(frozen_set_t)
s = lf.set_to_list(frozen_set_s)

print("dict: ",d)
print("list: ",l)
print("tuple:",t)
print()


#-------------------------------------------------------------------------------------
# range to list                                                                      -
#-------------------------------------------------------------------------------------
print("\033[48;5;99m                                                           \033[0m")
print("  RANGE")
r = range(0,15,3)
print(r)
l = lf.range_to_list(data=r, header=None, layout=lf.Layout.VERTICAL)
print(l)
l = lf.range_to_list(r,"Range Title","horizontal")
print(l)
print()
l = lf.data_to_list(r)# by default->(data=r, header=None, layout=lf.Layout.HORIZONTAL)
print(l)


#-------------------------------------------------------------------------------------
# tuple to list                                                                      -
#-------------------------------------------------------------------------------------
print("\033[48;5;99m                                                           \033[0m")
print("  TUPLE")
tupleData1 = (("Apple"));    print("case 0:",tupleData1)       # this is a string                     Case 0
tupleData2 = ("",);          print("case 1:",tupleData2)       # this is a tuple                      Case 1
tupleData3 = ("Apple",);     print("case 2:",tupleData3)       # this is a simple tuple               Case 2
tupleData4 = (("Apple",));   print("case 3:",tupleData4)       # this is a tuple inside tuple         Case 3
print()
tupleData5 = (("hello",),("hell",),("hi",),([1,2],)) # this is a simple tuple w/ tuples     Case 4
tupleData6 = (("hello","hello"),("hell",),("hi","bye","good"),([1,2],)) #                   Case 4
print("Case 4:",tupleData5); print("Case 4:",tupleData6)
print()
tupleData7 = ("hello","hell","hi",[1,2])             # this is a simple tuple w/ string     Case 5
tupleData8 = (("hello"),("hell"),("hi"),([1,2]))     # this is a simple tuples w/ string    Case 5
print("Case 5:",tupleData7); print("Case 5:",tupleData8)
print()
# this is a tuple w/ combination other type of variables Case 6
tupleData9 = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
print("Case 6:",tupleData9)
print()

listData1 = lf.tuple_to_list(tupleData1);   print("Case 0:",listData1)
listData2 = lf.tuple_to_list(tupleData2);   print("Case 1:",listData2)
listData3 = lf.tuple_to_list(tupleData3);   print("Case 2:",listData3)
listData4 = lf.tuple_to_list(tupleData4);   print("Case 3:",listData4)
listData5 = lf.tuple_to_list(tupleData5);   print("Case 4:",listData5)
listData6 = lf.tuple_to_list(tupleData6);   print("Case 4:",listData6)
listData7 = lf.tuple_to_list(tupleData7);   print("Case 5:",listData7)
listData8 = lf.tuple_to_list(tupleData8);   print("Case 5:",listData8)
listData9 = lf.tuple_to_list(tupleData9);   print("Case 6:",listData9)
print()
