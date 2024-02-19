def to_str(list1):
    res = ""  # Создаем пустую строку
    while True:  # Цикл повторяться до тех пор, пока не пройдет по всему списку
        for el in list1:  # Проходим по элементам(el) списка(list1)
            if isinstance(el, list):  # Проверка на тип элемента, если элемент является списком, то присваеваем list1 текущий элемент
                list1 = el
                break
            else:  # Если же элемент не является списком добавляем его к списку res с "->"
                res += f"{el} -> "
        else:
            break  # Если нет элементов, значит, мы прошли весь список
    return res[:-4] + " -> None"  # Удаляем последние "->" и добавляем "-> None"


print(to_str([1, [2, [3, [4, [5]]]]]))