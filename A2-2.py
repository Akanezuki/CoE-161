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
    # your code..
    # more code..

    return ans
}
























