def solution(num_list):
    a=num_list[::2]
    b=num_list[1::2]
    return max(sum(a),sum(b))