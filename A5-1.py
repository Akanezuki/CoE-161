def count_bad_channels(blocklength, erasure_prob):

    given_depth = math.log2(blocklength)
    curr_ep = erasure_prob
    curr_d = 0
    initial_count = 0

    def polar_recur(erasure_prob, curr_erasure_prob, curr_depth, given_depth, count):

        if curr_depth == given_depth:
            if curr_erasure_prob > erasure_prob:
                count += 1
                return count
            else:
                return count
        else:
            curr_depth += 1
            w1_curr_erasure_prob = curr_erasure_prob**2
            w2_curr_erasure_prob = 1 - ((1-curr_erasure_prob)**2)
            return(polar_recur(erasure_prob, w1_curr_erasure_prob, curr_depth, given_depth, count) + polar_recur(erasure_prob, w2_curr_erasure_prob, curr_depth, given_depth, count))

    ans = polar_recur(erasure_prob, curr_ep, curr_d, given_depth, initial_count)
    return ans