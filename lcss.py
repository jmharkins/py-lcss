#import numpy as np

def lcss(s, t):
    len_s = len(s)
    len_t = len(t)
    pref_matrix = [[] for i in range(0,len_s)]
    maxlen = 0
    maxstr = []
    for i in range(0, len_s):
        s_i = s[i]
        for j in range (0, len_t):
            t_j = t[j]
            if s_i == t_j:
                if (i == 0) or (j == 0):
                    pref_matrix[i].append(1)
                else:
                    pref_matrix[i].append(pref_matrix[i-1][j-1] + 1)
                if pref_matrix[i][j] > maxlen:
                    maxlen = pref_matrix[i][j]
                    substr = s[(i+1)-maxlen:(i+1)]
                    maxstr = [substr]
                elif pref_matrix[i][j] == maxlen:
                    substr = s[(i+1)-maxlen:(i+1)]
                    if substr not in maxstr:
                        maxstr.append(substr)
            else:
                pref_matrix[i].append(0)
    return maxstr
