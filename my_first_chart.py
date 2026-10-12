import matplotlib.pyplot as plt

# 한글 폰트 설정 (맥은 AppleGothic, 윈도우는 Malgun Gothic 사용)
plt.rcParams["font.family"] = "Malgun Gothic"  # 윈도우인 경우 "Malgun Gothic"으로 변경
plt.rcParams["axes.unicode_minus"] = False

prices = [75000, 79500, 70000, 75000, 71900]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)

for i, p in enumerate(prices):
  ax.annotate(
      f"{p:,}",
      (i, p),
      textcoords="offset points",
      xytext=(0, 8),
      ha="center",
  )

ax.set_title("내 첫 그래프")
fig.savefig("my_first_chart.png")