def visualize(persentage):
    print(f"{persentage}%: {'*' * (persentage // 10)}")

percentages = [33, 50, 22, 70, 12, 90]
for persentage in percentages:
    visualize(persentage)

