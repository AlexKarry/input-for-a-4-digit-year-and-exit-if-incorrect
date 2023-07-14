=======

user_type = input('please enter a 4-digit year: ')               # str, 2349

if not user_type.isdigit() or len(user_type) != 4:               # bool, True
    print('sorry, must be 4 digits')
else:
    print(f'input validated: {user_type}')
exit()

=======

# valid_input = False                                            # bool, False
#
# while not valid_input:                                         # bool, True
#     user_type = input('Please enter a 4-digit year: ')         # str, 2349
#
#     if not user_type.isdigit() or len(user_type) != 4:         # bool, True
#         print('Sorry, must be 4 digits')
#     else:
#         print(f'Input validated: {user_type}')
#         valid_input = True
