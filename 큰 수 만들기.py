def solution(number, k):
    st = []
    for num in number:
        while st and st[-1] < num and k > 0:
            st.pop()
            k -= 1
        st.append(num)

    while k > 0:
        st.pop()
        k-=1

    answer = ''.join(st)
    return answer