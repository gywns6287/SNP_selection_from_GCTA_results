#2020.11.05

import argparse

##parser
parser = argparse.ArgumentParser()
parser.add_argument('--gcta', help='Input gcta mlma or mlma.loco results')
parser.add_argument("--ld", help = "Input Plink LD results, if you don't need pruning, just skip this", default = None)
parser.add_argument("--k", help='Input #N of selecting marker', default = 1000, type = int)
parser.add_argument('--out',default = None)
args = parser.parse_args()
if not args.out:
    args.out = args.gcta.split('.')[0] + 'results.txt'

##open GCTA results##
GCTA = open(args.gcta,'r')
next(GCTA)
SNP = GCTA.read().splitlines()
print('Total {0} SNPs in GCTA results'.format(len(SNP)))
SNP.sort(key = lambda k: abs(float((k.split()[6]))),reverse = True)
SNP = [i.split()[1] for i in SNP]

#without LD punning
if not args.ld:
    with open(args.out,'w') as out:
        out.write('\n'.join(SNP[:args.k])+'\n')
    if len(SNP[:args.k]) != args.k:
        print('Warning: K is larger than Total markers, then program extrat whole marker.')
    print('Total {0} marker are extracted at {1}'.format(len(SNP[:args.k]),args.out))
    quit()

##make LD dictonary
from collections import defaultdict
print('make LD dictonary from {0}'.format(args.ld))

LD = open(args.ld,'r')
next(LD)
LD_dic = defaultdict(list)

for line in LD:
    line_ = line.split()
    LD_dic[line_[2]].append(line_[5])

sum_len = 0
for v in LD_dic.values(): sum_len += len(v)

print('Total {0} marker have LD-SNP\n'
      'Total {1} SNP make LD-relationship each other'
      .format(len(LD_dic),round(sum_len/len(LD_dic),3)))


##LD prunning
out = open(args.out,'w')
k = 0
for _ in range(args.k):
    k += 1
    candi = SNP.pop(0)
    for ld_snp in LD_dic[candi]:
        if ld_snp in SNP:
            SNP.remove(ld_snp)
    out.write(candi+'\n')

    if not SNP:
        print('Warning: K is larger than prunned markers, you should decreas K or LD threshold.')
        break
print('Total {0} marker are extracted at {1}'.format(k,args.out))
