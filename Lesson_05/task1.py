name = input("Enter your name: ").lower()
surname = input("Enter your surname: ").lower()
birthday = input("Enter your year of birth: ").lower()
domain = '@kobzar.ua'

print(f'1st variant:  {name}.{surname}{domain}')
print(f'2nd variant:  {name[0]}{surname}{domain}')
print(f'3nd variant:  {name[0]}{surname[0]}{birthday}{domain}')