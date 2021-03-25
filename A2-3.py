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

    while len(samples) != 0:
        x = samples.pop(0)
        sx = set(x)
        char_extract(encoder.root, sx, blist)
        
    ans = ''.join(blist)
    return ans
