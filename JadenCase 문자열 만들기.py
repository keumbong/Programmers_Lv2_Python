def solution(s):
    answer = s.split(' ')
    my_list = []

    for word in answer:
        my_list.append(word.capitalize())
    return ' '.join(my_list)