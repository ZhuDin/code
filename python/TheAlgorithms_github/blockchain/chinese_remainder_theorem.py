"""
Chinese Remainder Theorem:
GCD ( Greatest Common Divisor ) or HCF (Highest Common Factor)

If GCD(a,b) = 1, then for any remainder ra modulo a and any remainder rb modulo b
there exists integer n, such that n = ra (mod a) and n = ra(mod b). If n1 and n2 are
two such integers, then n1=n2(mod ab)

Algorithm :

1. Use extended euclid algorithm to find x,y such that a*x + b*y = 1
2. Take n = ra*by + rb*ax 
"""
from __future__ import annotations


# Extended Euclid
def extended_euclid(a: int, b: int) -> tuple[int, int]
    """
    
    """