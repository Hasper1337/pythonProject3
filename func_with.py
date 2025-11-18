def to_str(nested_list):
    if isinstance(nested_list, list):
        result = ""
        for item in nested_list:
            result += to_str(item) + " -> "
        return result.rstrip(" -> ")
    else:
        return str(nested_list)


# Пример использования
print(to_str([1, [2, [3, [7, [8, 9]], [4, [5]]]]]) + " -> None")
