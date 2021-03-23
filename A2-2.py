class Node:
    def __init__(self, symbol=None):
        self.left = None
        self.right = None
        self.data = symbol

    def __del__(self):
        if self.left is not None:
            del self.left
        if self.right is not None:
            del self.right
        del self.data
    
    def insert(self, bitstring, symbol):
        if bitstring == '':
            self.data = symbol
        elif bitstring[0] == '0':
            if self.left is None:
                self.left = Node()
            
            self.left.insert(bitstring[1:], symbol)
        elif bitstring[0] == '1':
            if self.right is None:
                self.right = Node()
            
            self.right.insert(bitstring[1:], symbol)

class Decoder:
    def __init__(self, symbol_map):
        self.root = Node()
        for (bit_string, symbol) in symbol_map.items():
            self.root.insert(bit_string, symbol)
    
    def __del__(self):
        del self.root

#-----------------------------------END--OF--HEADER----------------------------------#

def prefix_free_decode(decoder, bit_string):
    bs_index = 0
    tlist = []
    slist = []
    for x in range(len(bit_string)):
        tlist.append(bit_string[x])
    
    def data_pop_r(Node, bitlist, string_list):
        if Node.data != None:
            string_list.append(Node.data)
            return Node.data
        
        b = bitlist.pop(0)

        if b == '0':
            data_pop_r(Node.left, bitlist, string_list)
        if b == '1':
            data_pop_r(Node.right, bitlist, string_list)

    while len(tlist) != 0:
        data_pop_r(decoder.root, tlist, slist)

    ans = ''.join(slist)

    return ans

x = prefix_free_decode(Decoder({'10010':'p','10011':'t','0100':'d', '1110':'i', '000':'n', '10100':'y', '0101':'c', '10101':'u', '0110':'s', '10110':'h', '0111':'r', '110':' ', '001':'e', '10111':'v', '1111':'a', '1000':'g'}), '111100001001100011011100101111010010011101101110000100011000011100101001')
print(x)
y = prefix_free_decode(Decoder({'00':'e','01':'h','10':'y', '11':' '}), '0100101101001011010010')
print(y)





























