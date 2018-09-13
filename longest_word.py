# coding: utf-8
# Search for the largest word within a phrase

def longest_word(phrase):
    size_max = 0
    start_pos = 0
    end_pos = len(phrase) - 1
    aux = 0
    
    for i in range(len(phrase)):
        if phrase[i] == ' ':
            aux = 0
        else:
            aux += 1
            if aux >= size_max:
                end_pos = i
                start_pos = i - aux + 1
                size_max = aux
    
    word = ''
    for i in range(start_pos, end_pos + 1):
        word += phrase[i]
    
    return word


print "Enter a phrase: "
phrase = raw_input()
print "The longest word in this sentence is:", longest_word(phrase)