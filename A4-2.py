import random, math

def exact_entropy(dist):
    return sum([-p*math.log2(p) for p in dist.values() if p > 0])

def estimated_entropy(samples, dist):
    return sum([-samples.count(x)/len(samples) * math.log2(dist[x]) for x in set(samples) if dist[x] > 0])

def jointly_typical(x, y, joint_dist, epsilon):
    if len(x) != len(y):
        raise ValueError('x and y must have equal lengths.')
    elif epsilon <= 0:
        raise ValueError('epsilon must be strictly positive.')
    else:
        row_length = [len(joint_dist[i]) for i in range(len(joint_dist))]
        if any([row_length[i] != row_length[0] for i in range(1, len(row_length))]):
            raise ValueError('All rows of joint_dist must have equal lengths.')
    
    xy = [(x[i], y[i]) for i in range(len(x))]
    x_symbols = range(len(joint_dist))
    y_symbols = range(len(joint_dist[0]))

    x_prob = {x: sum([joint_dist[x][y] for y in y_symbols]) for x in x_symbols}
    y_prob = {y: sum([joint_dist[x][y] for x in x_symbols]) for y in y_symbols}
    xy_prob = {(x,y): joint_dist[x][y] for x in x_symbols for y in y_symbols}

    Hx = exact_entropy(x_prob)
    Hy = exact_entropy(y_prob)
    Hxy = exact_entropy(xy_prob)

    #if max([abs(Hx - estimated_entropy(x, x_prob)), abs(Hy - estimated_entropy(y, y_prob)), abs(Hxy - estimated_entropy(xy, xy_prob))]) < epsilon:
        #print(max([abs(Hx - estimated_entropy(x, x_prob)), abs(Hy - estimated_entropy(y, y_prob)), abs(Hxy - estimated_entropy(xy, xy_prob))]))

    return max([abs(Hx - estimated_entropy(x, x_prob)), abs(Hy - estimated_entropy(y, y_prob)), abs(Hxy - estimated_entropy(xy, xy_prob))]) < epsilon

#------------------------------------------ end of header ------------------------------------------------------------------------------------#
    	
def typical_set_codec(channel, x_dist, frame_len, block_len, num_frames, epsilon):

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
    print(num_frames)
    print(success)
    estimated_error_probability = fail/num_frames

    print(estimated_error_probability)
    return(estimated_error_probability)

#---------------------------------------------- MAIN ------------------------------------------------------------#


p = 0.01
#channel = [[0.99, 0.005, 0.005],[0.005, 0.99, 0.005],[0.005, 0.005, 0.99]]
#channel = [[1-p, 0, p],[0, 1-p, p]]
channel = [[0.95, 0, 0.05], [0, 0.95, 0.05]]
#channel[x][y]

frame_len = 10
x_dist = [1/2, 1/2]
block_len = 1000
num_frames = 1000
epsilon = 0.05

typical_set_codec(channel, x_dist, frame_len, block_len, num_frames, epsilon)