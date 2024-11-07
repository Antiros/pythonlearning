calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_str = string.upper()
    lower_str = string.lower()
    return (length, upper_str, lower_str)

def is_contains(string, list_to_search):
    count_calls()
    return any(s.lower() == string.lower() for s in list_to_search)
print(string_info('Galaxy'))
print(string_info('Andromeda'))
print(is_contains('Milkyway', ['way', 'mIlky', 'miLKYwaY']))
print(is_contains('supernova', ['hypernova', 'nova']))
print(calls)
