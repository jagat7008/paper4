def word_length(text):
    words=text.split()
    word_dict={}
    for word in words:
        word_dict[word]=len(word)
    return word_dict
s='i am jagatjit behera'
input_s=(word_length(s))
print(input_s)    