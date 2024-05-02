def to_str(lst):
    result = ""
    stack = [lst]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            result += str(item) + " -> "
    return result + "None"

# def to_str(lst):
#     result = ""
#     for item in lst:
#         if isinstance(item, list):
#             result += to_str(item) + "-> "
#         else:
#             result += str(item) + " -> "
#     return result[:-3]



print(to_str([1, [2, [3, [7, [8]], [4, [5]]]]]))
