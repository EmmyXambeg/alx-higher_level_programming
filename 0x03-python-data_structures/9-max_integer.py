#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    else:
        ''' this else can be removed since return
        ends the function for the if statement :)
        '''
        x = my_list[0]
        for i in my_list:
            if i > x:
                x = i
        return x
