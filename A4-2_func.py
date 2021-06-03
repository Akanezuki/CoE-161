def typical_set_codec(channel, x_dist, frame_len, block_len, num_frames, epsilon):

    print("frame_len: ", frame_len)
    print("block_len: ", block_len)
    print("num_frames: ", num_frames)
    print("epsilon: ", epsilon)
    print("x_dist: ", x_dist)
    print("channel: ", channel)

    #-----generating xy joint distribution-----#

    x_rows, y_cols = (len(x_dist), len(channel[0]))
    xy_dist = [[channel[i][j]*x_dist[i] for j in range(y_cols)] for i in range(x_rows)]

    #-----generating alphabet-----#

    symbols = [i for i in range(len(x_dist))]
    output_symbols = [i for i in range(len(channel[0]))]

    #---------generating codebook-----------#

    codebook = {}
    for i in range(2**frame_len):
        sym_block_str = ''
        for j in range(block_len):
            sym_block_str += str(random.choices(symbols, x_dist).pop())
        sym_block_int = [int(i) for i in sym_block_str]
        codebook[i] = sym_block_int

    #-----selecting codeword for transmission-----#

    input_frames = [random.randrange(2**frame_len) for i in range(num_frames)]
    input_blocks = [codebook[input_frames[i]] for i in range(num_frames)]

    #----- sending transmission through channel -----#

    output_sequence = []
    for sym in input_blocks:
        yn = []
        for i in sym:
            yn.append(random.choices(output_symbols, channel[i]).pop())
        output_sequence.append(yn)
        yn = []

    #----- checking joint typicallity of Xn and Yn -----#
    
    success = 0
    for output_element in output_sequence:
        checker = 0
        for codeword in codebook.values():
            if jointly_typical(codeword, output_element, xy_dist, epsilon):
                checker += 1
        if checker == 1:
            success += 1

    fail = num_frames - success
    estimated_error_probability = fail/num_frames
    print("eep: ", estimated_error_probability, '\n')
    return(estimated_error_probability)
