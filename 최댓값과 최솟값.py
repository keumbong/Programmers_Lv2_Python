def solution(s):
    my_list = s.split(' ')
    my_list = list(map(int, my_list))
    max_num, min_num = max(my_list), min(my_list)

    return str(min_num) +' ' + str(max_num)