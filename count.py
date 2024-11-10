input_string="python program"
char_count={}
for char in input_string:
    if char!=' ':
        if char in char_count:
            char_count[char]+=1
            print("if",char_count[char])
        else:
            char_count[char]=1
            print("else",char_count)
print("Alphanumeric character count:",char_count)
