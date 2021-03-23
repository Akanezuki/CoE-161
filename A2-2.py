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





























