import re

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
    blist = []
    def char_extract(Node, set_elem, bit_list):
        if Node.data.intersection(set_elem) == set_elem and len(Node.data) != 1:
            if Node.left.data.intersection(set_elem) == set_elem:
                bit_list.append('0')
                char_extract(Node.left, set_elem, bit_list)
            if Node.right.data.intersection(set_elem) ==set_elem:
                bit_list.append('1')
                char_extract(Node.right, set_elem, bit_list)
        else:
            return

    samplist = list(samples)
    while len(samplist) != 0:
        x = samplist.pop(0)
        sx = set(x)
        char_extract(encoder.root, sx, blist)
        
    ans = ''.join(blist)
    return ans

#============================================================#

def encoder_report(encoder, grimms_title, titles, lines):
    title_idx = titles.index(grimms_title)
    line_start = lines.index(grimms_title)
    line_end = lines.index(titles[title_idx + 1])

    orig_text = '\n'.join(lines[line_start:line_end])
    bitstring = huffman_encode(encoder, orig_text)

    return len(orig_text), len(bitstring)

if __name__ == '__main__':
    
    regex = re.compile("^( ){5}[A-Z',\\-\\[\\] ]+$")
    titles = []

    file_contents = open('grimms-fairy-tales.txt').read().replace('\r','')
    lines = file_contents.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        if regex.match(line):
            titles.append(line[5:])
    titles.append('*****')
    
    encoder = HuffmanEncoder(list(file_contents))

    for grimms_title in titles[:-1]:
        print(grimms_title, encoder_report(encoder, grimms_title, titles, lines))
