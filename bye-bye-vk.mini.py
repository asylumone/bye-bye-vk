#!/usr/bin/env python3
#Bye-Bye, VK!
#With love, by t.me/undefined_value
import base64
import gzip
code = bytes("""H4sIAFTAZFsC/+VaeZPiuJL/n0/hfhMVUI+asg0YQ8fr2TX3YTAGm6uno8KHbIxPfHDNzndfyTZXFV3V/a54G0tENUjKTKXyl8pM
Sf3LJzwKfFw2HBw4W8w7hCvXKWZ+qR3Ar/DvCZv2P2V+mRnhCrPcLWzLByx8tgEeOSrQDAeoL1vJikDGsD3XDzFZCkC5dGrpR8M7
/wahJwXBqRkaNshM+8yo+8J2a9gXKDgEQe4vf/lLplMKukzNXi5bAcPkiWWhQK+H20V1fmgNdEWXoh6l7D2T0Fu1QYsM9UAttphh
kWutxbq+bLk2LZobQ7CEWsMsFgNuIppmbyIuq+w0b9Q5kMdJPrO05o3Vwm3iEmeJgS2Y9M4UTUnD6aKu0rgwr4vF3r5VKfp7SsRr
Sj/obOayYDGrWr7EeNxQnuiFw5qdDUjRMgiTlTXW4HjKEnoC3mz4VTZfyXhOQwz6u+ly7G+tmW8e5bCosEy5Yy0ov0pNpxxJVQA9
1hp4a2rs8+YQ7y/HwOpsFYbgV7XOiNMaB4razsLSbLZoifyEF9nBXj8MpqbTFFv96jzTKdPrormebHyCDDienhr5dc3fk0divuo3
j01BZ70SNSwGriVPxOmwv/I1xpoItZ2usqUiP+L50nhHDIZ8gVddVuxbg9F62SQHDL2reL0x3+bdTFNrRj5N00pnlnfMtjCsqWJ7
UdIOlTyOb+W1VqSpEtERO8Wq60dRBZ+JupjvrRRGzdeGNaIvy5Ioz12lVF9P6CAgRu0BIdn1aaPXKivORq04fmas9o8uWT0UNmvX
wV1WJ8bmmBl6U3ZmrJ2S6S0mRDvPsqHVCZZmSQkEdzKKSDF07aFQXNA9QOKuPl118b4gSdOmQ3apvhjJoiFTFtmpKe6skCnQHpXH
lzufJPcl0psoVXGdN5aEVyxx6gb4odtRvN2WVXb8SAaFo6xsXB0YrW2Dt8pT2a37XnesCvV2ryD5lfHeKuxL7MxecM3GkiIUR1vy
60ybMzidtw/acj1o7jmqYYtHkaH2nj3tTkrzbpNtH41QWXY67X17tHYpfD3DvZG1Zeozf8Mw7rJPT+Zro87LMhfa+bE1rNHrutCU
JHIOokg81gaZrdcRW7sDS6z5slasCBo/WBalVUUgFgY9d+bA1CpL3TT7u4bWWwAwHNSBOxOmMrTjYsSJgrUOD0p/NaM3m/W8yIYr
stLpt71+g+QWjqgdq7ycmeLsQZ3znfy6wR+X3coaFJkjqdkTtWH1TC6IqmVAuSDolLUoauNHjbNn+KEmCWRDrdm1tlwzwzrltGtS
pbvJD0y6W+xStL0vNcm8W7e8oqpGGT2wKlXb35QF6jC0dLZta1VKbxb4jjI48ovhsctOlrW5SJT4+n7dLoDawZkO67PDgtps8V2T
X5drZi9PNkbMJGC5kGPJrmNbjlLZF3VfGx7Kh3nGFKWmMOmRvriqtyqzhVE1+HAynrRKtF60IrtvLNTaejAp9JfOOhoZYKjT4kDp
WgoftoR24zDXZ9o4XDUcu+OABUPgVU7ZLtdu0ey0wbYsGz7IzKmCvhWr5bxaH4BNuaDyh4NJNOaLYYeMOmavjNv5XmW45Ahq7Gug
iyt8ezgeNXjRPjYHk1Ft2yBGijWdrFm1ZZZWE7XXyY+GxMYWyhtOEMoCucr0fXLh5H13Xj7OPbJozxVZ7Ww7Bbj197y6K4r8cN6q
6rRBBypVp7rqUdLkFU1JFdmc+k3L749bTqWfp9StsuyC5WAvTzvHVlQfFPJu16k3W94+YxnNAblt6u1pRBvLuTirrncV7rioFtjw
UJasPk4a4+2G5TWKFQ28IxoF7QiI45KravxxsekVN812hTY8wSsfg+HM6DYXR2LllLpEQ8b9ZdBkl5lObS3uya08ZMkZGdZxayP7
LcrtRrvlYD0GHrUXwmp1arVa+wGv02rFHpeOfYoflptyHrf7Wn0SGpUDxymR507HzJEqVzota1DvDWo2HzmjxdzIrCnS0ierVsUh
Wngg+IS52ASCbuf1eac5gyYQ6jrj4kNZ6Dc7IVPzy43W5HAoVGlCHdj8Yat1iN2erDZHAevg01ph69QZ0q+THZreDdoi2WkzmXV+
tLG3ixkICX5+bJS4PUcUWqoSADna1+kFy3St3m5qGvth0d0ultSQVhlqMh9RETFcl5TpoleqDdU1kacoZhdorjmsG2xQmvFW3wim
R47qWplqU1iQhWnVBvMGsW6V+2MpT1Q3s2VXYWtqkGeG22Ndqpt1g5k3942dtViqeb8uFW21kffxoi7zzJSX3YILjPzYgX67VsLB
uizpMjcriPxIH5cz9cWSnG1HMOeCnS61B+WiLdKqbGgNdTUPWt0Dr/jHCm4rKrMZ95yDQ8z2AtPF1cBWW/LEHAxkZhhMys6gOakO
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""".replace("\n", ""), "utf-8")
exec(gzip.decompress(base64.decodestring(code)).decode("utf-8"))
