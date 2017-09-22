#!/bin/python

def cc(str):
    list1 = [0] * 26
    for i in range(0,len(str)):
        if (str[i] >= 'a' and str[i] <= 'z' ):
        list[ord(str[i]) - ord('a') ] += 1
    print(list)
    
if __name__ == "__main__":
    str = "this is test for scripts."
    str = str.lower()
    cc(str)