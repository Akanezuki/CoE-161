class Node:
    def __init__(self, data, weight):
        self.left = None
        self.right = None
        self.data = data
        self.weight = weight

class HuffmanEncoder:
    def __init__(self, samples):
        alphabet = set(samples)
        alphabet_size = len(alphabet)

        nodes = [Node({symb}, samples.count(symb)) for symb in alphabet]

        for it in range(1, len(alphabet)):
            a,b = sorted(range(len(nodes)), key = lambda idx : nodes[idx].weight)[:2]
            
            supernode = Node(nodes[a].data.union(nodes[b].data), nodes[a].weight + nodes[b].weight)
            supernode.left = nodes[a]
            supernode.right = nodes[b]
            
            nodes = [nodes[idx] for idx in range(len(nodes)) if idx not in (a,b)]
            nodes.append(supernode)

        self.root = nodes[0]
    
    def encode(self, samples):
        return huffman_encode(self, samples)

#============================================================#

def huffman_encode(encoder, samples):
    # Your code goes here
    # More code..
    
    return ans

