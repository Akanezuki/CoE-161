def count_bad_channels(blocklength, erasure_prob):

    gv_depth = math.log2(blocklength)
    curr_p = erasure_prob
    curr_d = 0
    gl_count = 0

    def polar_recur(bec_prob, curr_bec_prob, curr_depth, given_depth, count):
        #print("count: ", count)
        if curr_depth == given_depth:
            #print("reached end depth: ")
            if curr_bec_prob > bec_prob:
                count += 1
                #print("successful count: ", count)
                return count
            else:
                #print("fail")
                return count
        else:
            #print("Splitting")
            curr_depth += 1
            #print("curr depth: ", curr_depth)
            w1_curr_bec_prob = curr_bec_prob**2
            w2_curr_bec_prob = 1 - ((1-curr_bec_prob)**2)
            return(polar_recur(bec_prob, w1_curr_bec_prob, curr_depth, given_depth, count) + polar_recur(bec_prob, w2_curr_bec_prob, curr_depth, given_depth, count))

    ans = polar_recur(erasure_prob, curr_p, curr_d, gv_depth, gl_count)
    print(ans)

    return ans