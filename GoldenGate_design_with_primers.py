def complement1(asd):
    qwe = ''
    rty = ('A','G','T','C')
    for i in asd:
        qwe+=rty[rty.index(i)-2]
    return(qwe)

qqq = '''ccaggcatcaaataaaacgaaaggctcagtcgaaagactgggcctttcgttttatctgttgtttgtcggtgaacgctctctactagagtcacactggctcaccttcgggtgggcctttctgcgtttata'''.upper()
f = 'GTAGGTCTCAGTAA'
r = complement1('GTAGGTCTCTAAGG')[::-1]
qqq1 = f+qqq+r
print(qqq1, len(qqq1))
ans = qqq1[0:34]+' '+complement1(qqq1[::-1][0:34])
print(ans, len(ans))
