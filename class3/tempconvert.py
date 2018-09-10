list_c = [0.0, 37.0, 100.0, 30.0, 15.0]
list_f = []
for temp_c in list_c:
    list_f = list_f + [(temp_c   * 9 / 5) + 32]
print(list_f)
