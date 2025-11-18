# Without #
def to_str(lst):
    result = []
    current = lst

    while current is not None and current != []:
        if isinstance(current, list) and len(current) > 0:
            result.append(str(current[0]))
            current = current[1] if len(current) > 1 else None
        else:
            break

    result.append('None')
    return ' -> '.join(result)

# def to_str(lst):
#     result = ""
#     stack = [lst]
#     while stack:
#         item = stack.pop()
#         if isinstance(item, list):
#             stack.extend(item[::-1])
#         else:
#             result += str(item) + " -> "
#     return result + "None"



# With #
def to_str(lst):
    if lst is None or lst == []:
        return 'None'

    if isinstance(lst, list) and len(lst) > 0:
        current = lst[0]
        rest = lst[1] if len(lst) > 1 else None
        return f'{current} -> {to_str(rest)}'

    return 'None'
# def to_str(nested_list):
#     def helper(lst):
#         result = ""
#         for item in lst:
#             if isinstance(item, list):
#                 result += helper(item) + " -> "
#             else:
#                 result += str(item) + " -> "
#         return result.rstrip(" -> ")
#     return helper(nested_list) + " -> None"


print(to_str([1, [2, [3, [7, [91, 65], [4, 5]]]]]))
