# -*- coding: utf-8 -*-
import sys

class HuffNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def is_leaf(self):
        return not(self.left or self.right)
    
def create_frequencies(data):
    '''
    Function to create frequencies for character data
    '''
    frequency_dict = {}
    for char in data:
        if char not in frequency_dict.keys():
            frequency_dict[char] = 1
        else:
            frequency_dict[char] += 1
    frequencies = []
    for char, freq in frequency_dict.items():
        frequencies.append(HuffNode(char, freq))
    
    return frequencies

def sort_frequencies(frequencies):
    sorted_freq =  sorted(frequencies, key=lambda x: x.freq, reverse=True)
    return sorted_freq

def build_huff_tree(text):
    frequencies = create_frequencies(text)
    frequencies = sort_frequencies(frequencies)
    
    while len(frequencies) > 1:
        left = frequencies.pop()
        right = frequencies.pop()
        
        freq_sum = left.freq + right.freq
        
        parent = HuffNode(None, freq_sum)
        parent.left = left
        parent.right = right
        
        frequencies.append(parent)
        
        frequencies = sort_frequencies(frequencies)
        
    return frequencies[0]

def trim_huff_tree(tree, huff_code):
    huff_dict = {}
    if not tree:
        return huff_dict
    if tree.is_leaf():
        huff_dict[tree.char] = huff_code
    huff_dict.update(trim_huff_tree(tree.left, huff_code + '0'))
    huff_dict.update(trim_huff_tree(tree.right, huff_code + '1'))
    return huff_dict

def decode_next(data, index, tree):
    assert(tree)
    assert(len(data) > 0)
    if tree.is_leaf():
        return tree.char, index
    if data[index] == '0':
        return decode_next(data, index + 1, tree.left)
    else:
        return decode_next(data, index + 1, tree.right)
    

def huffman_encoding(text):
    assert len(text) > 0, "text should not be empty"
    huff_tree = build_huff_tree( text )
    huff_map = trim_huff_tree( huff_tree, '' )
    data = ''
    for char in text:
        data += huff_map[char]
    return data, huff_tree



def huffman_decoding(data, tree):
    assert data, 'Encoding is not available'
    assert(tree)
    text, next_index = decode_next( data, 0, tree )
    while next_index < len(data):
        next_char, next_index = decode_next( data, next_index, tree )
        text += next_char
    return text

def test_encoding(text):
    print ("Original Text:\t\t {}".format( text ))
    print ("Size:\t\t\t {}".format( sys.getsizeof(text) ))
    
    encoded_data, tree = huffman_encoding(text)
    print ("Huffman Encoding:\t {}".format(encoded_data))
    print ("Size:\t\t\t {}".format( sys.getsizeof( int(encoded_data, base=2) ) )) if encoded_data else 0
    
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("Decoded Text:\t\t {}".format(decoded_data))
    print ("Size:\t\t\t {}".format( sys.getsizeof(decoded_data) ))
    
    return decoded_data == text


#Test Cases

print( test_encoding("The bird is the word") )
#Original Text:      The bird is the word
#Size:               69
#Huffman Encoding:   1110100100010111000110101101100111111110111100010001011001110000101101
#Size:               36
#Decoded Text:       The bird is the word
#Size:               69
#True

print( test_encoding("Adam") )
#Original Text:     Adam
#Size:              53
#Huffman Encoding:  01001110
#Size:              28
#Decoded Text:      Adam
#Size:              53
#True

print( test_encoding("The quick brown fox jumps over the lazy dog.") )
#Original Text:     The quick brown fox jumps over the lazy dog
#Size:              93
#Huffman Encoding:  100101000101011110011110111100110000010000011100011101100010001001101111011000010111111101110101110100101000010111110010101010101011011111010110001010111110100110111110110110001111110000001110011110010
#Size:              52
#Decoded Text:      The quick brown fox jumps over the lazy dog
#Size:              93
#True

print( test_encoding("ABBBBABBABABBBAABABABAABABA") )
#Original Text:     ABBBBABBABABBBAABABABAABABA
#Size:              76
#Huffman Encoding:  011110110101110010101001010
#Size:              28
#Decoded Text:      ABBBBABBABABBBAABABABAABABA
#Size:              76
#True

print( test_encoding("ABA"))
#Original Text:           ABA
#Size:                    52
#Huffman Encoding:        101
#Size:                    28
#Decoded Text:            ABA
#Size:                    52
#True

#print( test_encoding("AAA"))
#The string contains same characters which means the entropy in the data is zero and hence, it defeats the purpose of encoding.
#AssertionError: Encoding is not available. 

#print( test_encoding("") )
# AssertionError text should not be empty