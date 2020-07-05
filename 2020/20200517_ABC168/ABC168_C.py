import math

MINUTES_L = 6       # 長針が1分間で動く角度
MINUTES_S = 0.5     # 短針が1分間で動く角度
HOURS_S = 30        # 短針が1時間で動く角度

A, B, H, m = map(int, input().split())

angle_L = MINUTES_L * m
angle_S = HOURS_S * H + MINUTES_S * m

# 長針が示す座標を求める
radian = angle_L * math.pi / 180
y_L = math.sin(radian) * B
x_L = math.cos(radian) * B

# 短針が示す座標を求める
radian = angle_S * math.pi / 180
y_S = math.sin(radian) * A
x_S = math.cos(radian) * A

# 2点間の距離
ans = math.sqrt((x_L - x_S) * (x_L - x_S) + (y_L - y_S) * (y_L - y_S))

print(ans)
