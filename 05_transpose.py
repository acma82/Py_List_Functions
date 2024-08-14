import list_functions as lf

msg = f'''
            Inputs                     Outputs                                       Cases
   list_1 = "hello"                    []                                              1
   list_1 = []                         []                                              2
   list_1 = [5]                        [[5]]                                           3
   list_1 = [[1]]                      [1]                                             4
   list_1 = [1,2,3,4,5,6]              [[1],[2],[3],[4],[5],[6]]                       5
   list_1 = [[1,2],[3,4],[5,6]]        [[1,3,5],[2,4,6]           ]                    6
   list_1 = [[1],[4],[5,6]]            [[1,4,5],[fill_value,fill_value,6]]
                                       [[1,4,5]] -> autofill = False
                                       [[1,4,5]] -> autofill = False, type=\'string\'
   list_1 = [10,[50],[250],["H"],100]  [[10],[[50]],[[250]],[["H"]],[100]]             7

   list_1 = [[1,2,3,4,5,6]]            [1, 2, 3, 4, 5, 6]                              8 
   list_1 = [1, 2, 3, 4, 5, 6]         [[1], [2], [3], [4], [5], [6]]
   list_1 = [[1],[2],[3],[4],[5],[6]]  [[1,2,3,4,5,6]]
   '''
print(msg)
a = 6+2j
print(a)
# lst = "hello"        lst = []        lst = [5]        lst = [[1]]
# lst = [1,2,3,4,5,6]  ls[1, 2, 3, 4, 5, 6]t = [[1,2],[3,4],[5,6]]        lst = [[1],[4],[5,6]]
lst = [[1],[4,"t"],[5,6,"dos"]]
print("original:", lst)
#trans_lst = lf.transpose(my_list=lst, autofill=True, fill_value=0.5, type=lf.Fill_Type.NUMBER, update=False)
#trans_lst = lf.transpose(my_list=lst, autofill=True, fill_value="1", type="string", update=False)
trans_lst = lf.transpose(my_list=lst, autofill=True, fill_value=a, type="number", update=False)
print("New     :",trans_lst)




'''
----------------------------------------------------------------------------
   import list_functions as lf
   lf.transpose(my_list, autofill, fill_value, type, update)
   lf.transpose(list, bool, any, type, bool)

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
         the spot that need to be filled leaving the other elements intact
         in the list.
Options                          
lst = [1,2,3,4,5,6]
lst = [[1,2],[3,4],[5,6],[7,8]]
lst = [[1,2,3,4,5,6]]
lst = [[1],[4],[5,6]]
lst = [5,[50,40],45]
lst = [[5],6,40,[45]]

----------------------------------------------------------------------------
   '''
