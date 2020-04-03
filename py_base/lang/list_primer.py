
int_array_list = [1, 2, 3]
str_array_list = [str(x) for x in int_array_list]
string_content = ",".join(str_array_list)
print(int_array_list, ", ", string_content)