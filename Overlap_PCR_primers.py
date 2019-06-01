a='TAAACGTCGAACAGTCATGAAAGTCTTAGTACCAGACATACCATTTTACTGTGAATATTATTTGAAGCTG'
b='ATTTCTTCAAACATTTAAAAATAAAGACTTATTGTAGACAGAGGTACGCCCTTTTAATGGTTGCGATAAA'

# Довольно эффективная реализация алгоритма нахождения комплемента
def complement1(asd):
    qwe = ''
    rty = ('A','G','T','C')
    for i in asd:
        qwe+=rty[rty.index(i)-2]
    return(qwe)

# Ответ
print(complement1(b[0:20])[::-1]+complement1(a[:-21:-1])+' '+a[:-21:-1][::-1]+b[0:20])
