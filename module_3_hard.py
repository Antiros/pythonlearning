data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

total_sum = 0

def sub_sum(other):
    global total_sum
    for item in other:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(key, int):
                    total_sum += key
                elif isinstance(key, str):
                    total_sum += len(key)
                else:
                    sub_sum(key)
                if isinstance(value, int):
                    total_sum += value
                elif isinstance(value, str):
                    total_sum += len(value)
                else:
                    sub_sum(value)
        else:
            calculate_structure_sum(item)

def calculate_structure_sum(data):
    global total_sum
    if isinstance(data, int):
        total_sum += data
    elif isinstance(data, str):
        total_sum += len(data)
    else:
        sub_sum(data)
    return total_sum
result = calculate_structure_sum(data_structure)
print(result)