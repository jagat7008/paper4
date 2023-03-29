import re
input_str='msys@technology@bangalore'
output_str=re.sub(r'[^\w\s]',' ',input_str)
output_str=re.sub(' +',' ',output_str)
print(output_str)