"""
================= PYTHON FORMAT SPECIFIERS =================

General syntax inside f-strings:
    f"{value:[flags][width][.precision][type]}"

------------------------------------------------------------
TYPE SPECIFIERS
------------------------------------------------------------
s   → String
d   → Integer (decimal)
b   → Binary                (e.g., 255 → 11111111)
o   → Octal                 (e.g., 255 → 377)
x   → Hexadecimal lowercase (e.g., 255 → ff)
X   → Hexadecimal uppercase (e.g., 255 → FF)
f   → Fixed-point decimal   (e.g., 3.14159 → 3.14)
F   → Same as f but INF/NAN in caps
e   → Scientific notation   (e.g., 1234 → 1.234e+03)
E   → Scientific notation   (uppercase)
g   → General (auto uses f or e)
G   → General (uppercase)
%   → Percentage            (e.g., 0.85 → 85%)

------------------------------------------------------------
WIDTH & PRECISION
------------------------------------------------------------
{value:5d}       → width = 5 (right aligned)
{value:.2f}      → 2 decimal places
{value:08.2f}    → pad with zeros → '00012.34'

------------------------------------------------------------
FLAGS
------------------------------------------------------------
<   → Left align
>   → Right align (default)
^   → Center align
0   → Pad with zeros
,   → Use comma as thousands separator (1,000,000)
_   → Use underscore as thousands separator (1_000_000)
+   → Always show sign (+/-)
-   → Show negative sign only
(space) → Leading space for positive numbers

------------------------------------------------------------
EXAMPLES
------------------------------------------------------------
num = 12345.6789
print(f"{num:.2f}")      # 12345.68
print(f"{num:,.2f}")     # 12,345.68
print(f"{num:010.2f}")   # 00012345.68
print(f"{num:^12.2f}")   # ' 12345.68  '
print(f"{255:x}")        # ff
print(f"{255:b}")        # 11111111
print(f"{0.85:%}")       # 85.000000%
print(f"{0.85:.0%}")     # 85%

============================================================
"""
