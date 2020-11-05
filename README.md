# SNP selection from GCTA results

## Object

Let's selecting top K high effect SNP from GCTA mlma or mlma.loco results. The LD report from plink can be used for pruning optionally.

## Code
this code were implemented by **python 3**
### Procedure summary
1.  All SNP are sorted by their effects (beta).
2. first SNP is saved at results.
3. (option) If you input LD report, all SNP LD-related with first SNPs are removed from SNP list. 
4.  Process 2. and 3. will be repeated for K. 
### Simple to use code
```
python snp_selection_from_gcta.py --gcta [1] --k [2] --out [3] --ld [4]
```
[1]: gcta results file (mlma or mlma.loco)

[2]: #N of selected SNPs (default: 1000)

[3]: output name (default: same name with gcta file)

[4]: (option) plink LD report
 
## Example
```
python snp_selection_from_gcta.py --gcta example/GCTA.loco.mlma --k 1000 --out test_results.txt --ld example/plink.ld
```
