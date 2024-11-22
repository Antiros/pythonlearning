# # def sum_of_digits(number):
# #     str_number = str(number)
# #     if len(str_number) <= 1:
# #         return int(str_number)
# #     first = int(str_number[0])
# #     return first + sum_of_digits(int(str_number[1:]))
# # result = sum_of_digits(1)
# # print(result)
#
# def is_palindrome(s):
#     s = s.replace(' ', '').lower()
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])
# result = is_palindrome("A man a plan a canal Panama")
# print(result)

def list_digits(number):
    str_number = str(number)
    if len(str_number) <= 1:
        return [int(str_number)]
    first = str_number[0]
    return [first] + list_digits(int(str_number[1:]))
result = list_digits(132326541515)
print(result)