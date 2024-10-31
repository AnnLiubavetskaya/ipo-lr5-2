simvol = 0
first_str = input("Введите первую вашу строку: ")
first_replace = first_str.replace(' ', '')
len_first_str = len(first_replace)
second_str = input("Введите вторую вашу строку: ")
for i in second_str :
    if i in first_replace:
        simvol += 1
if simvol == len_first_str :
    print("Ваши строки являются анаграммами ")
else:
    print("Ваши строки не являются анаграммами")