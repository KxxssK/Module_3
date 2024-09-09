calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string ):
    len_str = len(string )
    verh_reg = string .upper()
    nig_reg = string .lower()
    inf_str = ([len_str, verh_reg, nig_reg])
    count_calls()
    return inf_str

def is_contains (string, list_to_search):
    otv = 0
    for i in list_to_search:
        if i.lower() == string.lower():
            otv = True
        else:
            otv = False
    count_calls()
    return otv

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)

