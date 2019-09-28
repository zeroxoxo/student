# Brainfuck compiler (from codewars exercise) c = brainfuck code (str), ipt = input ascii characters (str)
def brainfuck(c, ipt):
    memory = 1000
    out, p, i, br, in_id, m = '', 0, 0, 0, 0, [0 for n in range(memory)]
    while i < len(c):
        if c[i] == '>':
            p += 1
        elif c[i] == '<':
            p -= 1
        elif c[i] == '+':
            if m[p] == 255:
                m[p] = 0
            else:
                m[p] += 1
        elif c[i] == '-':
            if m[p] == 0:
                m[p] = 255
            else:
                m[p] -= 1  
        elif c[i] == '.':
            out += chr(m[p])
            
        elif c[i] == ',':
            m[p] = ord(ipt[in_id])
            in_id += 1
        elif c[i] == '[':
            if m[p] == 0:
                br = 1
                while c[i] != ']' or br > 0:
                    i += 1
                    if c[i] == '[':
                        br += 1
                    elif c[i] == ']':
                        br -= 1
                i +=1
        elif c[i] == ']':
            if m[p] != 0:
                br = 1
                while c[i] != '[' or br > 0:
                    i -= 1
                    if c[i] == ']':
                        br += 1
                    elif c[i] == '[':
                        br -= 1
                i -= 1
        i += 1
    return out
