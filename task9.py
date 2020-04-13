def repeat(original_list):
    new_list = ""
    for x in list(set(original_list)):
        new_list += str(x) + " " + str(original_list.count(x)) + ";"
    return new_list


_list = [28, 1, 0, 1, 0, 3, 4, 0, 0, 3]
print(repeat(_list))