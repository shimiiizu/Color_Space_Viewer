import pandas as pd
import matplotlib.pyplot as plt

# データフレームを読み込む
df = pd.read_csv('./csv/RGBCMYK.csv')

# RGB値を0-1の範囲に正規化（色として使用）
colors = df[['R', 'G', 'B']].values / 255.0

# パーセント変換
C_percent = (df['C'] / 255.0) * 100
M_percent = (df['M'] / 255.0) * 100
Y_percent = (df['Y'] / 255.0) * 100
K_percent = (df['K'] / 255.0) * 100
MC_percent = M_percent + C_percent
MK_percent = M_percent + K_percent

# 2行3列のサブプロット
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 1行目: Y vs M, Y vs C, Y vs K
axes[0, 0].scatter(Y_percent, M_percent, c=colors, s=100, edgecolors='black')
axes[0, 0].set_xlabel('Y (Yellow) [%]', fontsize=12)
axes[0, 0].set_ylabel('M (Magenta) [%]', fontsize=12)
axes[0, 0].set_title('Y vs M', fontsize=14)
axes[0, 0].set_xlim(0, 100)
axes[0, 0].set_ylim(0, 100)
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].scatter(Y_percent, C_percent, c=colors, s=100, edgecolors='black')
axes[0, 1].set_xlabel('Y (Yellow) [%]', fontsize=12)
axes[0, 1].set_ylabel('C (Cyan) [%]', fontsize=12)
axes[0, 1].set_title('Y vs C', fontsize=14)
axes[0, 1].set_xlim(0, 100)
axes[0, 1].set_ylim(0, 100)
axes[0, 1].grid(True, alpha=0.3)

axes[0, 2].scatter(Y_percent, K_percent, c=colors, s=100, edgecolors='black')
axes[0, 2].set_xlabel('Y (Yellow) [%]', fontsize=12)
axes[0, 2].set_ylabel('K (Black) [%]', fontsize=12)
axes[0, 2].set_title('Y vs K', fontsize=14)
axes[0, 2].set_xlim(0, 100)
axes[0, 2].set_ylim(0, 100)
axes[0, 2].grid(True, alpha=0.3)

# 2行目: Y vs M+C, Y vs M+K（左2つのみ使用）
axes[1, 0].scatter(Y_percent, MC_percent, c=colors, s=100, edgecolors='black')
axes[1, 0].set_xlabel('Y (Yellow) [%]', fontsize=12)
axes[1, 0].set_ylabel('M+C [%]', fontsize=12)
axes[1, 0].set_title('Y vs M+C', fontsize=14)
axes[1, 0].set_xlim(0, 100)
axes[1, 0].set_ylim(0, 200)
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].scatter(Y_percent, MK_percent, c=colors, s=100, edgecolors='black')
axes[1, 1].set_xlabel('Y (Yellow) [%]', fontsize=12)
axes[1, 1].set_ylabel('M+K [%]', fontsize=12)
axes[1, 1].set_title('Y vs M+K', fontsize=14)
axes[1, 1].set_xlim(0, 100)
axes[1, 1].set_ylim(0, 200)
axes[1, 1].grid(True, alpha=0.3)

# 右下のプロットを非表示
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()