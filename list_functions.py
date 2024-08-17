# Note: Use Python 3.12 or above
import enum
import csv
import os

class Layout(enum.StrEnum):
   HORIZONTAL = "horizontal"
   VERTICAL =   "vertical"


class Fill_Type(enum.StrEnum):
   STRING = "string"
   NUMBER = "number"


class Length_Col(enum.StrEnum):
   MAX = "max"
   MIN = "min"



#-------------------------------------------------------------------------------------------------------------
# Convert From Dict to List Type                                                                             -
#-------------------------------------------------------------------------------------------------------------
def dict_to_list(data:dict, key_title="key", value_title="value"):
   '''
   ----------------------------------------------------------------------------
   This function converts a dictionary to a list.
   ----------------------------------------------------------------------------
   '''
   my_key_list = []; my_data_list = []

   my_key_list  = list(data.keys())
   my_data_list = list(data.values())
   
   complete_list = [];  tempo_list = []
   if (key_title == "key") and (value_title == "value"):
      if (len(my_key_list)) > 1:   complete_list.append(["Keys","Values"])
      else:                        complete_list.append(["Key","Value"])
   
   elif (key_title == None or value_title == None or \
         key_title.lower() == "none" or value_title.lower() == "none"):
      pass

   else:
      complete_list.append([key_title,value_title])

   for d in range(len(data)):
      tempo_list.append(my_key_list[d])
      tempo_list.append(my_data_list[d])
      complete_list.append(tempo_list)
      tempo_list = []
   
   return complete_list


#-------------------------------------------------------------------------------------------------------------
# Convert From Set or Frozenset to List Type                                                                 -
#-------------------------------------------------------------------------------------------------------------
# set and frozenset values are printed in aleatory order all the time
def set_to_list(data:set|frozenset, header="set",layout:Layout=Layout.VERTICAL):
   '''
   ----------------------------------------------------------------------------
   This function converts a set or a frozenset to a list.
   ----------------------------------------------------------------------------
   '''
   tempo_list = []
   #----------------------------------------------------------------------------------
   def set_to_list_get_header():
      if header == "set" or header == "frozenset":
         if len(data) > 1:
            tempo_list.append([header+" Values"])
         else:
            tempo_list.append([header+" Value"])

      elif (header == None or header.lower() == "none"):
         pass

      else:
         tempo_list.append([header])
   

   #----------------------------------------------------------------------------------
   def set_to_list_layout_Vertical(option="horizontal"):
      set_to_list_get_header()

      cnt = 0; l = len(data)
      while l > 0:
         dato = list(data)[cnt]
         if (option == "vertical"):  tempo_list.append([dato])
         else:                       tempo_list.append(dato)
         cnt += 1
         l   -= 1


   #---------------------------------------------------------------------------------- 
   if (layout.lower() == "vertical" or layout == Layout.VERTICAL):
      set_to_list_layout_Vertical("vertical")

   elif (layout.lower == "horizontal" or layout == Layout.HORIZONTAL):
      set_to_list_layout_Vertical()

   else: pass
   
   return tempo_list


#-------------------------------------------------------------------------------------------------------------
# Convert From Range to List Type                                                                            -
#-------------------------------------------------------------------------------------------------------------
def range_to_list(data:range, header = None, layout:Layout=Layout.HORIZONTAL):
   '''
   ----------------------------------------------------------------------------
   This function converts a range to a list.
   ----------------------------------------------------------------------------
   '''
   tempo_list = []

   def range_to_list_get_header(option="horizontal"):
      if header == None or header.lower() == "none": pass

      else:
         if (option == "vertical"):            
            tempo_list.append([header])
         else:
            tempo_list.append("Range")
      
   #for n in data:
   if (layout.lower() == "vertical" or layout == Layout.VERTICAL):
      range_to_list_get_header("vertical")
      for n in data:
         tempo_list.append([n])      
      
   elif (layout.lower() == "horizontal" or layout == Layout.HORIZONTAL):
      range_to_list_get_header()
      for n in data:
         tempo_list.append(n)      
        
   else: pass

   return tempo_list



#-------------------------------------------------------------------------------------------------------------
# Convert From Tuple to List Type                                                                            -
#-------------------------------------------------------------------------------------------------------------
def tuple_to_list(data:tuple):
   '''
   ----------------------------------------------------------------------------
   This function converts a tuple to a list.
   ----------------------------------------------------------------------------
   '''
   tempo_list = []
   #-----------------------------------------------------------------------------------------------
   if (len(data) == 0):
      return tempo_list                

   #-----------------------------------------------------------------------------------------------
   elif (len(data) == 1):          
                                 # string              ("")         -> Case 0   String
                                 # "empty_tuple"       ("",)        -> Case 1   Empty
      tempo_list.append(data[0]) # "one_item_no_row"   ("Apple",)   -> Case 2   Tuple
      return tempo_list          # "one_item_one_row"  (("Apple",)) -> Case 3   Tuple inside Tuple

   #-----------------------------------------------------------------------------------------------
   #elif len(data) > 1:
   else:
      type_type = []; lengths = []
      l = len(data); tuple_tuple = 0; tuple_other = 0

      for n in range(len(data)):
         if (isinstance(data[n], tuple)):
            tuple_tuple = 1            
            type_type.append("tuple")
            lengths.append(len(data[n]))
         
         else:
            tuple_other = 1
            type_type.append("other")
            lengths.append(1)
      
      # This is only for tuples inside the tuple ->
      # tupleData = (("hello","hello"),("hell",),("hi","bye","good"),([1,2],))        -> Case 4
      if (tuple_tuple == 1 and tuple_other == 0):
         tempo = []
         for col in data:
            for i in col:
               tempo.append(i)
            tempo_list.append(tempo)
            tempo = []

      # This is only for other types inside a tuple 
      # tupleData = ("hello","hell","hi",[1,2])                                       -> Case 5
      elif (tuple_tuple == 0 and tuple_other == 1):
         for n in data:
            tempo_list.append(n)     # for rows (Horizontal)
            #tempo_list.append([n])  # for cols (Vertical)
         
       

      # This is for combination tuple (tuple =1 and other = 1)                        -> Case 6
      # tupleData = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
      elif (tuple_tuple == 1 and tuple_other == 1):
         for n in range(l):
            if (lengths[n]) > 1:
               tempo = []
               for i in range(lengths[n]):
                  tempo.append(data[n][i])
               tempo_list.append(tempo)

            else:
               if (type_type[n] == "other"):
                  tempo_list.append([data[n]])
               else:
                  tempo_list.append([data[n][0]])
      else:
         tempo_list = []

   return tempo_list



#-------------------------------------------------------------------------------------------------------------
# Conversion Any Data Type To To A List Type                                                                 -
#-------------------------------------------------------------------------------------------------------------
def data_to_list(dato):
   '''
   ----------------------------------------------------------------------------
   This function converts a any type of variable to a list type.
   ----------------------------------------------------------------------------
   '''
   data_list = []
   
   # list, bool, int, float, complex and string type
   def bifs_to_list(data):
      tempo_list = []
      tempo_list.append(data)
      return tempo_list

   if (isinstance(dato, list)):      return dato      
   elif (isinstance(dato, bool)):    data_list = bifs_to_list(dato)
   elif (isinstance(dato, int)):     data_list = bifs_to_list(dato)
   elif (isinstance(dato, float)):   data_list = bifs_to_list(dato)
   elif (isinstance(dato, str)):     data_list = bifs_to_list(dato)
   elif (isinstance(dato, complex)): data_list = bifs_to_list(dato)  
      
   # range type
   elif (isinstance(dato, range)):     data_list = range_to_list(dato)

   # dictionary type
   elif (isinstance(dato, dict)):      data_list = dict_to_list(dato)
   
   # set type
   elif (isinstance(dato, set)):       data_list = set_to_list(dato)

   # frozenset type
   elif (isinstance(dato, frozenset)): data_list = set_to_list(dato)
   
   # tuple
   elif (isinstance(dato, tuple)):     data_list = tuple_to_list(dato)
   
   else: pass
 
   return data_list


#-------------------------------------------------------------------------------------------------------------
# Manipulation Of A List Type                                                                                -
# Get List Type                                                                                              -
#-------------------------------------------------------------------------------------------------------------
def get_list_type(my_list):
   if not isinstance(my_list, list):
      return "incorrect_variable_type"                # [Not a List] Case 0
  #-----------------------------------------------------------------------------------------------

   if (len(my_list) == 0):
      return "empty_list"                             # []    Case 1

  #-----------------------------------------------------------------------------------------------

   if (len(my_list) == 1):
      if isinstance(my_list[0], list):
         if len(my_list[0]) > 1:
            return "multiple_items_one_row"           # [[1,2,3]]   Case 5
         else:
            return "one_item_one_row"                 # [[1]]  Case 4
      else:
         return "one_item_no_row"                     # [1]   Case 2

  #-----------------------------------------------------------------------------------------------
   if (len(my_list) > 1):
      items = 0; rows = 0
      for n in my_list:
         if not isinstance(n, list):
            items = 1
         else:
            rows = 1

      if (items ==  1 and rows == 0):
         return "multiple_items_no_row"               #  [1,2,3]  Case 3
      elif (items == 0 and rows == 1):
         return  "multiple_items_multiple_rows"       # [[1],[4],[7]]              Case 6
                                                      # [[1,2,3],[4,5,6],[7,8,9]]  Case 6
                                                      # [[1],[1,2,3],[5,4,7,8]]    Case 6
                                                      # any combination of this is Case 6
                                                      # [[1,2,3],[[2],3,4],[5,[6,7]]] Case 6
      else:
         return "mix_items"                           # [5,6,[1,2,3],[1,0,3]]      Case 7
                                                      # [[1,2],[1,2,[1]],[1,2,3]]  Case 7
                                                      # any combination of this is Case 7

#-------------------------------------------------------------------------------------------------------------
# Item List Rotation                                                                                         -
#-------------------------------------------------------------------------------------------------------------
# Right Shift                                                                                                -
#-------------------------------------------------------------------------------------------------------------
def right_shift(my_list:list=[], shift:int=0, update:bool=False)->list:
   '''
----------------------------------------------------------------------------
   import list_functions as lf
   lf.right_shift(list, int, bool)

   This function shift the elements in a list to the right.

   
   update is used to save the actual list with the shift elements.
   update is set to False is we wish to keep the original list and save
   the new list into another variable.
      
Options                          
lst = [1,2,3,4,5,6]           lst = [[1,2],[3,4],[5,6]]
lst = [[1],[4],[5,6]]         lst = [10,[50],[250],["H"],100]
lst = [[1,2,3,4,5,6]]
   
Example:
   print("original:  ", list_1, end="")
   print("   right_shift 2, update=False")
   newlist = lf.right_shift(list_1, 1, False)
   print("new list:  ",newlist)
   print("original:  ", list_1)

   print("\n----------------------------------------------------------------\n")

   print("original:  ", list_1,end="")
   print("   right_shift 2, update=True")
   newlist = lf.right_shift(my_list=list_1, shift= 1, update= 1)
   print("new list:  ",newlist)
   print("original:  ", list_1)
----------------------------------------------------------------------------
   '''
   list_type = get_list_type(my_list)

   # list_type = incorrect_variable_type: [Not a list type variable]
   if list_type == "incorrect_variable_type":
      return my_list
   # list_type = empty_list: []
   elif list_type == "empty_list":
      return my_list
   
   # list_type = one_item_no_row: ["one"]
   elif list_type == "one_item_no_row":
      return my_list
   
   # list_type = one_item_one_row: [["one"]]
   elif list_type == "one_item_one_row":
      return my_list

   # list_type == "multiple_items_no_row"          [1,2,3,4]
   # list_type == "multiple_items_multiple_rows"   [[7,6],[5,4],[1,2,3]] or [[2],[3],[5]]
   # list_type == "mix_items"                      [10,[50],[250],["H"],100]
   elif list_type == "multiple_items_no_row" or list_type == "mix_items"\
      or list_type == "multiple_items_multiple_rows":
      
      result = []; result = my_list; tempo = []

      length = len(result)-1
      for rot in range(shift):
         tempo.append(result[length])
         for n in range(length):
            tempo.append(result[n])
         result = tempo
         tempo = []

      if update == True:
         my_list.clear()
         [my_list.append(n) for n in result]
         return my_list
      else:
         return result
      
   # list_type = multiple_items_one_row: [[1,2,3,4]]
   elif list_type == "multiple_items_one_row":
      tempo = []; result = []; result = my_list[0]; length = len(result)-1

      for rot in range(shift):
         tempo.append(result[length])
         for n in range(length):
            tempo.append(result[n])
         result = tempo
         tempo = []

      if update == True:
         my_list.clear()         
         [tempo.append(n) for n in result]
         my_list.append(tempo)
         return my_list
      
      else:
         return [result]
   
   # A different case will just return the same list
   else:
      return my_list  
#-------------------------------------------------------------------------------------------------------------
# Left Shift                                                                                                 -
#-------------------------------------------------------------------------------------------------------------
def left_shift(my_list:list=[], shift=0, update:bool=False)->list:
   '''
----------------------------------------------------------------------------
   import list_functions as lf
   lf.left_shift(list, int, bool)

   This function shift the elements in a list to the left.

   update is used to save the actual list with the shift elements.
   update is set to False is we wish to keep the original list and save
   the new list into another variable.
      
Options                          
lst = [1,2,3,4,5,6]           lst = [[1,2],[3,4],[5,6]]
lst = [[1],[4],[5,6]]         lst = [10,[50],[250],["H"],100]
lst = [[1,2,3,4,5,6]]
   
Example:
   print("original:", list_1, end="")
   print("   left_shift 2, update=False")
   newlist = lf.left_shift(list_1, 2, False)
   print("new list:",newlist)
   print("original:", list_1)

   print("\n---------------------------------------------------------------------------------\n")

   print("original:", list_1,end="")
   print("   left_shift 2, update=True")
   newlist = lf.left_shift(my_list=list_1, shift= 2, update= 1)
   print("new list:",newlist)
   print("original:", list_1)
----------------------------------------------------------------------------
   '''   
   list_type = get_list_type(my_list)

   # list_type = incorrect_variable_type: [Not a list type variable]
   if list_type == "incorrect_variable_type":
      return my_list

   # list_type = empty_list: []
   elif list_type == "empty_list":
      return my_list
   
   # list_type = one_item_no_row: ["one"]
   elif list_type == "one_item_no_row":
      return my_list
   
   # list_type = one_item_one_row: [["one"]]
   elif list_type == "one_item_one_row":
      return my_list

   # list_type == "multiple_items_no_row"          [1,2,3,4]
   # list_type == "multiple_items_multiple_rows"   [[7,6],[5,4],[1,2,3]] or [[2],[3],[5]]
   # list_type == "mix_items"                      [10,[50],[250],["H"],100]
   elif list_type == "multiple_items_no_row" or list_type == "mix_items"\
      or list_type == "multiple_items_multiple_rows":
      
      result = []; result = my_list; tempo = []; length = len(result)-2
      for rot in range(shift):
         tempo.append(result[1])
         for n in range(length):
            idx = n + 2
            tempo.append(result[idx])
         tempo.append(result[0])
         result = tempo
         tempo = []
      if update == 1:
         my_list.clear()
         [my_list.append(n) for n in result]
         return my_list
      else:
         return result

   # list_type = multiple_items_one_row: [[1,2,3,4]]
   elif list_type == "multiple_items_one_row":
      tempo = []; result = []; result = my_list[0]; length = len(result)-2
      for rot in range(shift):
         tempo.append(result[1])
         for n in range(length):
            idx = n + 2
            tempo.append(result[idx])
         tempo.append(result[0])
         result = tempo
         tempo = []

      if update == 1:
         my_list.clear()            
         [tempo.append(n) for n in result]
         my_list.append(tempo)
         return my_list
      else:
         return [result]

   # A different case will just return the same list
   else:
      return my_list  

#-------------------------------------------------------------------------------------------------------------
# Swap                                                                                                       -
#-------------------------------------------------------------------------------------------------------------
def swap(my_list:list=[], pos1=0, pos2=0, update:bool=False)->list:
   '''
----------------------------------------------------------------------------
   import list_functions as lf
   lf.swap(list, int, int, bool)

   This function swap two elements in a list.

   update is used to save the actual list with the swap elements.
   update is set to False is we wish to keep the original list and save
   the new list into another variable.

   pos1 -> position 1 to be swap with position 2
   pos2 -> position 2 to be swap with position 1

   Note: If one of the position provided is out of range, the function
         will return the list as original and it will print a message
         out of range.
      
Options                          
lst = [1,2,3,4,5,6]           lst = [[1,2],[3,4],[5,6]]
lst = [[1],[4],[5,6]]         lst = [10,[50],[250],["H"],100]
lst = [[1,2,3,4,5,6]]
   
Example:
   lst = [[1,2],[3,4],[5,6],[7,8]]
   print("original: ", lst,end="")
   print("   update=False, pos1=0, pos2=2")
   newlist = lf.swap(my_list=lst, update= False, pos1= 0, pos2=2)
   print("new list: ",newlist)
   print("original: ", lst)

   print("\n----------------------------------------------------------------\n")

   print("original: ", lst,end="")
   print("   update=true, pos1=3, pos2=0")
   newlist = lf.swap(my_list=lst, update=True, pos1=3, pos2=0)
   print("new list: ",newlist)
   print("original: ", lst)
----------------------------------------------------------------------------
   '''
   list_type = get_list_type(my_list)

   # list_type = incorrect_variable_type: [Not a list type variable]
   if list_type == "incorrect_variable_type":
      return my_list

   # list_type = empty_list: []
   elif list_type == "empty_list":
      return my_list
   
   # list_type = one_item_no_row: ["one"]
   elif list_type == "one_item_no_row":
      return my_list
   
   # list_type = one_item_one_row: [["one"]]
   elif list_type == "one_item_one_row":
      return my_list

   # list_type == "multiple_items_no_row"          [1,2,3,4]
   # list_type == "multiple_items_multiple_rows"   [[7,6],[5,4],[1,2,3]] or [[2],[3],[5]]
   # list_type == "mix_items"                      [10,[50],[250],["H"],100]
   elif list_type == "multiple_items_no_row" or list_type == "mix_items"\
      or list_type == "multiple_items_multiple_rows":
      result = []; length = len(my_list) - 1

      if (length < pos1):
         print(f" pos1 = {pos1} is out of range...! ")
         return my_list
      if (length < pos2):
         print(f" pos2 = {pos2} is out of range...! ")
         return my_list
      
      for n in range(len(my_list)):
         if n == pos1:
            result.append(my_list[pos2])
         elif n == pos2:
            result.append(my_list[pos1])
         else:
            result.append(my_list[n])
      
      if update == 1:
         my_list.clear()
         [my_list.append(n) for n in result]         
         return my_list
      else:
         return result
         
   # list_type = multiple_items_one_row: [[1,2,3,4]]
   elif list_type == "multiple_items_one_row":
      result = []; length = len(my_list[0]) - 1
      if (length < pos1):
         print(f" pos1 = {pos1} is out of range...! ")
         return my_list
      if (length < pos2):
         print(f" pos2 = {pos2} is out of range...! ")
         return my_list
      
      for n in range(len(my_list[0])):
         if n == pos1:
            result.append(my_list[0][pos2])
         elif n == pos2:
            result.append(my_list[0][pos1])
         else:
            result.append(my_list[0][n])

      if update == 1:
         my_list.clear()
         [my_list.append(n) for n in result]         
         return [my_list]
      else:
         return result

   else:
      return [my_list]
   

#-------------------------------------------------------------------------------------------------------------
# Complete Data List to Make it Rectangular (Rows and Cols)                                                  -
#-------------------------------------------------------------------------------------------------------------
def autofill_data(my_list:list, fill_value="----", update:bool=False)->list:
   '''
----------------------------------------------------------------------------
   import list_functions as lf
   lf.autofill_data(list, str/int/float, update)

   This function will fill all the empty columns from the list.
   fill_value is the chr to be used to fill those columns. It can be str,
   int, float, or bool. By default it's a str type (----).
   
         
example:
   lst = [[9,8,7],[4],[5,6]]
   print("Original:",lst)
   result = lf.autofill_data(lst, fill_value=9.8, update=False)
   print("mylist=lst, fill_value=9.8, update=False")
   print("Result  :",result)
   print("Original:",lst)

   print("\n----------------------------------------------------------------\n")

   print("Original:",lst)
   result = lf.autofill_data(my_list=lst, fill_value=99, update=True)
   print("mylist=lst, fill_value=99, type= \"string\", update=True")
   print("Result  :",result)
   print("Original:",lst)
----------------------------------------------------------------------------
   '''
   list_type = get_list_type(my_list)
   if list_type == "multiple_items_multiple_rows":
      n_rows, n_cols = dimensions(my_list)
      tempo = []; matrix_update = []

      for row in range(n_rows):
         for col in range(n_cols):
            try:
               tempo.append(my_list[row][col])
            except:
               tempo.append(fill_value)
               

         matrix_update.append(tempo)
         tempo = []
         
      if update == True:
         my_list.clear()
         [my_list.append(n) for n in matrix_update]
      return matrix_update 
   
   else:
      return my_list


#-------------------------------------------------------------------------------------------------------------
# Transpose List (Converting the rows into cols and cols into rows)                                          -
#-------------------------------------------------------------------------------------------------------------
def transpose(my_list:list, autofill=True, fill_value="----", type:Fill_Type=Fill_Type.STRING, update:bool=False)->list:
   '''
----------------------------------------------------------------------------
   import list_functions as lf
   lf.transpose(my_list, autofill, fill_value, type, update)
   lf.transpose(list, bool, any, str, bool)

   This function get the transpose list.

   update is used to replace original list with the transpose list.
   update is set to False to keep the original list and save
   the new list into another variable.

   Note: When the list is not square or rectangular, the autofill will be
         used. If the autofill is set to False, some data will be lost.
         If the autofill is set to True, the fill_value will be used
         to fill those spot needed. The fill_value can be replace as 
         needed, by default is set to four dash. 

         Also, autofill only make all the elements in the list to string 
         when we use type=string, however for number option it only affect
         the spot that need to be filled leaving the other elements intact.
Options                          
lst = [1,2,3,4,5,6]
lst = [[1,2],[3,4],[5,6],[7,8]]
lst = [[1,2,3,4,5,6]]
lst = [[1],[4],[5,6]]
lst = [5,[50,40],45]
lst = [[5],6,40,[45]]
lst = [[1],[4,"t"],[5,6,"dos"]]

print("original:", lst)
trans_lst = lf.transpose(my_list=lst, autofill=True, fill_value=0.5, type=lf.Fill_Type.NUMBER, update=False)
print("New     :",trans_lst)

----------------------------------------------------------------------------
   '''
   transpose_list = []
   list_type = get_list_type(my_list)


   if list_type == "incorrect_variable_type":  # [Not a List]  Done...! Case 0
      pass #return "incorrect variable type"
  
   elif list_type == "empty_list":             # []  Done...! Case 1
      pass #return "empty list"
  
   elif list_type == "multiple_items_one_row": # input: [[10,20,30]] output: [10,20,30] Done...! Case 5
      for row in my_list:
         for col in row:
            transpose_list.append(col)
      #return transpose_list

   elif list_type == "one_item_one_row":       # input: [[10]] output: [10] Done...! Case 4
      transpose_list.append(my_list[0][0])
      #return transpose_list
  
   elif list_type == "one_item_no_row":        # input :[10]  output: [[10]] Done...! Case 2
      transpose_list = [[my_list[0]]]
      #return transpose_list

   elif list_type == "multiple_items_no_row":  # input: [10,20,30] output: [[10],[20],[30]] Done...! Case 3
      for col in range(len(my_list)):               
         transpose_list.append([my_list[col]])
      #return transpose_list
  
   elif list_type == "mix_items": 
      for n in my_list:
         transpose_list.append([n])
         #return transpose_list                # input: [5,[50],45] or [5,[50,40],45] or [[5],6,40,[45]] Case 9

   else:   # input: [[1],[2],[3]] output: [[1,2,3]] Done...! Case 6
           # input: [[1,2,3],[4,5,6],[7,8,9]] output: [[1,4,7],[2,5,8],[3,6,9]] Done...!  Case 7
           # input: [[1,2,3],[4,5,6,6],[7,8,9,9]] output: [[1,4,7],[2,5,8],[3,6,9]] Done...! Case 8
           # input: [[1,2,3],[4,5],[7,8,9]] output: Error_data_dimension Done...! Case 9
           # note: the element 0 needs to be greater than the rest.

      #--------------------------------------------------------------
      if (autofill == True):
         fill_list = autofill_data(my_list=my_list, fill_value=fill_value,type=type)
      else:
         fill_list = my_list         
      #--------------------------------------------------------------      
           
      lengths = []
      for l in fill_list:           # finding the smallest
         lengths.append(len(l))    
    
      smaller = min(lengths)
    
      for item in fill_list:
         if len(item) != smaller:
            break

      for i in range(smaller): 
         row =[]
         for item in fill_list:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
         transpose_list.append(row)

   if update == False:
      pass
   else:
      my_list.clear()
      for n in transpose_list:
         my_list.append(n)

   return transpose_list



#-------------------------------------------------------------------------------------------------------------
# Dimension of the List (Rows and Cols)                                                                      -
#-------------------------------------------------------------------------------------------------------------
def dimensions(my_list:list=[], option:Length_Col=Length_Col.MAX)->tuple[int]:
   '''
----------------------------------------------------------------------------
   import fancylist as fl
   n_rows, n_cols = dimensions(data_list)

   This function return the number of rows and cols in a list.
   It will take the longest number for the columns as the case 7 or 8.
      
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
   rows, cols = fl.dimensions(lst,""max)
   print("rows: ", rows, "     cols: ", cols)
   
   rows, cols = lf.dimensions(my_list=lst, option=lf.Length_Col.MIN)
   print("rows: ", rows, "     cols: ", cols)
----------------------------------------------------------------------------
   '''
   n_rows = 0; n_cols = 0
   list_type = get_list_type(my_list)

   if list_type == "incorrect_variable_type" or list_type == "empty_list":
      return n_rows, n_cols
   
   elif list_type == "one_item_no_row": # Done  ["dato"]
      n_cols = 1; n_rows = 1

   elif list_type == "one_item_one_row": # Done [["dato"]]
      n_cols = 1; n_rows = 1

   elif list_type == "multiple_items_no_row": # Done ["Hello","bye","good"]
      n_rows = 1
      n_cols = sum(1 for num in my_list)

   elif list_type == "multiple_items_one_row": # Done [["Hello","bye","good"]]
      n_rows = 1
      for n in my_list[0]:
         n_cols += 1  
   
   # Done [["Hello"],["bye"],["good"]] or [["Hello","mio"],["bye"],["good","hh"]]
   elif list_type == "multiple_items_multiple_rows":
      n_rows = len(my_list); n_cols = 0; lengths = []
      
      for r in my_list:
         lengths.append(len(r))
      
      if option.lower() == "max":
         n_cols = max(lengths)
      
      elif option.lower() == "min":
         n_cols = min(lengths)

      else:
         n_cols = 0

   else:
      n_cols = 0; n_rows = 0
  
   return n_rows, n_cols


#-------------------------------------------------------------------------------------------------------------
# Convert a Mix Type Elemnt List to a String List                                                            -
#-------------------------------------------------------------------------------------------------------------
def num_to_str(my_list:list=[], fill_value="----", update:bool=False)->list:
   tempo = []; str_list = []
   list_type = get_list_type(my_list)

   if list_type == "incorrect_variable_type":
      error = " "+list_type+" "
      print(error)
      return None
   
   elif list_type == "empty_list":
      return my_list

   elif list_type == "one_item_no_row": # Done  ["dato"]
      str_list.append(str(my_list[0]))
      if update == True:
         my_list.clear()
         my_list.append(str_list[0])

   elif list_type == "one_item_one_row": # Done [["dato"]]
      str_list.append([str(my_list[0][0])])
      if update == True:
         my_list.clear()
         my_list.append([str_list[0][0]])

   elif list_type == "multiple_items_no_row": # Done ["Hello","bye","good"]
      [str_list.append(str(n)) for n in my_list]
      if update == True:
         my_list.clear()
         [my_list.append(n) for n in str_list]

   elif list_type == "multiple_items_one_row": # Done [["Hello","bye","good"]]
      tempo = []
      [tempo.append(str(my_list[0][n])) for n in range(len(my_list[0]))]
      str_list.append(tempo)
      if update == True:
         my_list.clear()
         [my_list.append(n) for n in str_list]
   
   # Done [["Hello"],["bye"],["good"]] or [["Hello","mio"],["bye"],["good","hh"]]
   elif list_type == "multiple_items_multiple_rows":
      n_rows = len(my_list)
      n_cols = 0
      # getting the longest number of columns in the list
      for n in my_list:
         if len(n) > n_cols:
            n_cols = len(n)
      
      # filling the empty spots
      for row in range(n_rows):
         for col in range(n_cols):
            try:
               tempo.append(str(my_list[row][col]))
            except:
               tempo.append(str(fill_value))
         str_list.append(tempo)
         tempo = []

      if update == True:
         my_list.clear()
         [my_list.append(n) for n in str_list]
      else: pass
      
   else:   # list_type == "mix_items"
      for n in my_list:
         str_list.append(str(n))
      
      if update == True:
         my_list.clear()
         [my_list.append(n) for n in str_list]
  
   return str_list

   


#-------------------------------------------------------------------------------------------------------------
# Convert a List to Digit Where Possible                                                                     -
#-------------------------------------------------------------------------------------------------------------
def str_to_num(my_list:list=[], fill_value=0, update:bool=False)->list:
   def get_number(x):
      try: 
         numb = int(x)
         return numb          # return "integer"
      except:
         try:
            numb = float(x)
            return numb       # return "float"
         except:
            try:
               numb = complex(x)
               return numb
            except:
               return "no_number_type"

   def conver2number(n):
      numb = get_number(n)
      if numb != "no_number_type":
         return numb
      elif isinstance(fill_value, int) or isinstance(fill_value, float) or isinstance(fill_value, complex):
         numb = get_number(fill_value)
         return numb
      else:
         return 0
               
   # num_to_str is already using the send_msg function         
   #string_list = num_to_str(my_list=my_list, fill_value=fill_value, update=False)
   tempo = []; num_list = []
   list_type = get_list_type(my_list)
   
   if list_type == "incorrect_variable_type":
      return [] #None
   
   if list_type == "empty_list":
      return my_list
   
   elif list_type == "one_item_no_row": # Done  ["dato"]
      num_list.append(conver2number(my_list[0]))
      if update == True:
         my_list.clear()
         my_list.append(num_list[0])

   elif list_type == "one_item_one_row": # Done [["dato"]]
      num_list.append([conver2number(my_list[0][0])])
      if update == True:
         my_list.clear()
         my_list.append([num_list[0][0]])

   elif list_type == "multiple_items_no_row": # Done ["Hello","bye","good"]
      [num_list.append(conver2number(n)) for n in my_list]
      if update == True:
         my_list.clear()
         [my_list.append(n) for n in num_list]

   elif list_type == "multiple_items_one_row": # Done [["Hello","bye","good"]]
      tempo = []
      [tempo.append(conver2number(my_list[0][n])) for n in range(len(my_list[0]))]
      num_list.append(tempo)
      if update == True:
         my_list.clear()
         [my_list.append(n) for n in num_list]

   # Done [["Hello"],["bye"],["good"]] or [["Hello","mio"],["bye"],["good","hh"]]
   elif list_type == "multiple_items_multiple_rows":
      n_rows = len(my_list)
      n_cols = 0
      # getting the longest number of columns in the list
      for n in my_list:
         if len(n) > n_cols:
            n_cols = len(n)
      
      # filling the empty spots
      for row in range(n_rows):
         for col in range(n_cols):
            try:
               tempo.append(conver2number(my_list[row][col]))
            except:
               tempo.append(conver2number(fill_value))
         num_list.append(tempo)
         tempo = []

      if update == True:
         my_list.clear()
         [my_list.append(n) for n in num_list]
      else: pass

   else:
      for n in my_list:
         num_list.append(conver2number(n))
      
      if update == True:
         my_list.clear()
         [my_list.append(n) for n in num_list]

   return num_list


#-------------------------------------------------------------------------------------------------------------
# Replace a Same Elements on a List                                                                          -
#-------------------------------------------------------------------------------------------------------------
def replace(my_list:list=[], ref_value="---", new_value="----", update:bool=False)->list:
   list_type = get_list_type(my_list)
   replace_list = []
   if list_type == "incorrect_variable_type":
      error = " "+list_type+" "
      print(error)
      return None
   
   elif list_type == "empty_list":
      return my_list

   elif list_type == "one_item_no_row": # Done  ["dato"]
      if (ref_value == my_list[0]):
         replace_list.append(new_value)
      
      if update == True:
         my_list.clear()
         my_list.append(replace_list[0])

   elif list_type == "one_item_one_row": # Done [["dato"]]
      if (ref_value == my_list[0][0]):
         replace_list.append([new_value])

      if update == True:
         my_list.clear()
         my_list.append([replace_list[0][0]])

   elif list_type == "multiple_items_no_row": # Done ["Hello","bye","good"]
      for n in my_list:
         if (n == ref_value):
            replace_list.append(new_value)
         else:
            replace_list.append(n)

      if update == True:
         my_list.clear()
         [my_list.append(n) for n in replace_list]

   
      # Done [["Hello","bye","good"]]
      # Done [["Hello"],["bye"],["good"]] or [["Hello","mio"],["bye"],["good","hh"]]
   elif list_type == "multiple_items_one_row" or list_type == "multiple_items_multiple_rows":
      tempo_list = []
      for row in my_list:
         for col in row:
            if (col == ref_value):
               tempo_list.append(new_value)
            else:
               tempo_list.append(col)

         replace_list.append(tempo_list)
         tempo_list = []

      if update == True:
         my_list.clear()
         tempo_list = []
         for row in replace_list:
            for col in row:
               tempo_list.append(col)
            
            my_list.append(tempo_list)
            tempo_list = []
      
   else:
      for n in my_list:
         if (n == ref_value):
            replace_list.append(new_value)
         else:
            replace_list.append(n)

      if update == True:
         my_list.clear()
         [my_list.append(n) for n in replace_list]
   
   return replace_list
#-------------------------------------------------------------------------------------------------------------
# Sort a List by Specific Reference Column                                                                   -
#-------------------------------------------------------------------------------------------------------------
# def sort_by_col(my_list:list=[], ref_col=0, fill_value="----", type="string", update=False)->list:
# my_list:list[]   this discribe the type of input in the function
# ->list           this show the return type of the function
def sort_by_col(my_list:list=[], ref_col=0, fill_value="----", type:Fill_Type=Fill_Type.STRING, update:bool=False)->list:
   
   list_type = get_list_type(my_list)

   if list_type == "incorrect_variable_type":
      print()
      print(msg=" Only For List Type Variable ",indent=4)
      print()
      return my_list
   
   elif list_type == "empty_list":
      return my_list

   elif list_type == "one_item_no_row": # Done  ["dato"]
      return my_list
   
   elif list_type == "one_item_one_row": # Done [["dato"]]
      return my_list
   
   elif list_type == "multiple_items_no_row": # Done ["Hello","bye","good"]
      
      tempo_list = []      
      if type == "string":   [tempo_list.append(str(n)) for n in my_list]
      elif type == "number": tempo_list = str_to_num(my_list=my_list, fill_value=fill_value, update=False)
      else:                  [tempo_list.append(str(n)) for n in my_list]

      sorted_list = sorted(tempo_list)

      if update == True:
         my_list.clear()
         [my_list.append(n) for n in sorted_list]

      return sorted_list

   elif list_type == "multiple_items_one_row": # Done [["Hello","bye","good"]]
      tempo_list = []; tempo = []
      if type == "string":
         [tempo.append(str(n)) for n in my_list[0]]
         tempo_list.append(tempo)

      elif type == "number":
         tempo_list = str_to_num(my_list=my_list, fill_value=fill_value, update=False)

      else:
         [tempo.append(str(n)) for n in my_list[0]]
         tempo_list.append(tempo)
      

      sorted_list = sorted(tempo_list[0])

      if update == True:
         my_list.clear()
         tempo_list = []
         [tempo_list.append(n) for n in sorted_list]
         my_list.append(tempo_list)
   
      return [sorted_list]

      # Done [["Hello"],["bye"],["good"]] or [["Hello","mio"],["bye"],["good","hh"]]
   elif list_type == "multiple_items_multiple_rows":
      complete_list = autofill_data(my_list=my_list, fill_value=fill_value, type=type, update=False)
      n_rows, n_cols = dimensions(complete_list, "max")

      if ref_col >= n_cols:
         print()
         print(" ref_col out of range...! ")
         print()
         return my_list 

      else:
         if type == "string":
            new_list = num_to_str(my_list=my_list, update=False)
            sorted_list = [new_list[0]] + sorted(complete_list[1:], key=lambda x: x[ref_col])
            #sorted_list = [my_list[0]] + sorted(complete_list[1:], key=lambda x: str(x[ref_col]))
         elif type == "number":
            sorted_list = [my_list[0]] + sorted(complete_list[1:], key=lambda x: (x[ref_col]))
         else:
            sorted_list = [my_list[0]] + sorted(complete_list[1:], key=lambda x: str(x[ref_col]))

         if update == True:
            my_list.clear()
            [my_list.append(n) for n in sorted_list]     
      
         return sorted_list

   else:
      print()
      print(msg=" Not supported between instances of int and list ")
      print()
      return my_list
   

#-------------------------------------------------------------------------------------------------------------
# Write CSV File                                                                                             -
#-------------------------------------------------------------------------------------------------------------
def write_csv_file(my_list=["None"], file_path="fancylist")->str:
   current_path = os.getcwd()
   ext = ""
   for l in file_path[-4:]:
      ext += l

   if ext == ".csv":
      file_name = file_path
   else:
      file_name = file_path + ".csv"

   #with open(file_path + ".csv", "w", newline="") as file:
   with open(file_name, "w", newline="") as file:
      writer = csv.writer(file)

      for row in range(len(my_list)):
         writer.writerow([col for col in my_list[row]])

   if ("/" in file_name): file = file_name
   else:                  file = current_path+"/"+file_name

   return file


#-------------------------------------------------------------------------------------------------------------
# Read CSV File                                                                                              -
#-------------------------------------------------------------------------------------------------------------
def read_csv_file(file_path="fancylist")->list:
   rows = []; ext = ""
   for l in file_path[-4:]:
      ext += l

   if ext == ".csv": file_name = file_path
   else:             file_name = file_path + ".csv"

   #with open(file_path + ".csv", "r", newline="") as file:
   with open(file_name, "r", newline="") as file:
      reader = csv.reader(file)
      #header = next(reader)
      for row in reader:
         rows.append(row)
   return rows
