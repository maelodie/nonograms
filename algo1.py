M = 5
def case_possible(j : int, l: int, s):
    if l = 0:
        return True
    elif l >= 1:
        if j < s[l] - 1:
            return False
        elif j == s[l] - 1:
            if j != M-1:
                return True
        else:
            return case_possible(j+1, l-1, s)

