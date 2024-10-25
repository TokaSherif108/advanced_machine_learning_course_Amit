def fun(s):
    lst = s.split(" ")
    new_lst = lst[::-1]
    new_str = ""
    for i in new_lst:
        new_str += i + " "
    #new_str = new_str[:-1]
    print (new_str)
s = "Hello World"
fun(s)
