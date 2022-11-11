a=int(input("Serum sodium enter value between 136-145 :"))
b=int(input("Serum creatinine enter value between 62-115 :"))
c=int(input("Urine sodium enter value between 100-260:"))
d=int(input("Urine creatinine enter value between 1768-32709:"))
f=c*b*100
e=a*d
g=f/e
g=round(g,1)
if a < 135:
    print("the value entered for serum sodium is very low should be between 136-145")
if a >=146:
    print("the value entered for serum sodium is very high should be between 135-145")
if b <= 61:
    print("the value entered for Serum creatinine is very low should be between 62-115")
if b >=116:
    print("the value entered for Serum creatinine is very high should be between 62-115")
if c <= 99:
    print("the value entered for Urine sodium is very low should be between 100-260")
if c >=261:
    print("the value entered for Urine sodium is very high should be between 100-260")
if d < 1767:
    print("the value entered for Urine creatinine is very low should be between 1768-32709")
if d >=32710:
    print("the value entered for Urine creatinine is very high should be between 1768-32709")

if 0 <= g <= 1:
    print("%s%%"%g,"FENa")
    print("Pre-Renal")
    print("e.g. Hypovolemia, heart failure, renal artery stenosis, sepsis (anything causing decreased effective renal perfusion). Remember, contrast-induced nephropathy will often look pre-renal.")

if 1 <= g <= 3:
    print("%s%%"%g,"FENa")
    print("INTRINSIC")
    print("e.g. ATN, AIN, glomerulonephritides")
if 4 <= g <= 100:
    print("%s%%"%g,"FENa")
    print("Post-Renal/Obstructive")
    print("e.g. BPH, bladder stone, bilateral ureter obstruction")
    