def comp(asd):
    qwe = ''
    rty = ('A','G','T','C')
    for i in asd:
        qwe+=rty[rty.index(i)-2]
    return(qwe)


an_mes = ('AGAGTTTGGAACACC','TTCCTTCTC','TTGCATTGAAAGCGC')
an_dac = ('AGAGTTTGGAACACC','ATCCATTTC','TTGCATTGAAAGCGC')

rbs = 'TTCACACAGGAAACC'
linker = 'ggcagc'.upper()
gene = 'AAAAAAAAAAAAAAAAAAAAA'
#gene = open('gfp', 'r').read().replace('\n', '').upper()

x = comp(an_mes[2])[::-1]+comp(an_mes[1])[::-1]+comp(an_mes[0])[::-1]+rbs+an_mes[0][0:-3]+'ATG'+an_mes[1]+linker+gene

def rna(x):
  y = ''
  for i in x:
    if i == 'T':
      y+='U'
    else:
      y+=i
  return(y)


print('Toehold switch: ', rna(x))
print('Trigger RNA: ', rna(an_mes[0]+an_mes[1]+an_mes[2]))
