from re import fullmatch as re_fullmatch


print(True) if re_fullmatch('((0[1-9])|([12]\d)|(3[0-1]))/((0[1-9])|(1[0-2]))/([12]\d{3})', '29/12/3000') else print(False)
