from decimal import Decimal, ROUND_DOWN

tmp_a, B = map(str, input().split())
A = int(tmp_a)

print(int(A * Decimal(B).quantize(Decimal('0.01'), rounding=ROUND_DOWN)))
