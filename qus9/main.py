def add_indexes(s):
    output_str=""
    for i,c in enumerate(s):
        output_str += c + str(i+1)
    return output_str
s="abcde"
output_str=add_indexes(s)
print(output_str)