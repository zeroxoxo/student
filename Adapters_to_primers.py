def complement1(asd):
    qwe = ''
    rty = ('A','G','T','C')
    for i in asd:
        qwe+=rty[rty.index(i)-2]
    return(qwe)

seq = open('seq.txt', 'r').read().replace('\n','').upper()
ast = 'GGGGCCAACTTTCTTGTACAAAGTGG'
afn = complement1('GGGGACAACTTTGTATAATAAAGTTGGC')[::-1]
seq1 = ast + seq + afn
ans = seq1[0:20+len(ast)]+' '+complement1(seq1[::-1][0:20+len(afn)])
print(ans, len(ans)) 
print(seq1)
