def solution(my_string,overwrite_string,s):
    my_string=list(my_string)
    for i in range(len(overwrite_string)):
        my_string[i+s]=overwrite_string[i]
    return ''.join(my_string)