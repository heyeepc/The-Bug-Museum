date = []
date_min = []
date_max = []

while True:

    date_1 = input("输入一个数字")

    if date_1 == " ":

        break

    for i in date_1:

        date.append(i)


b = sum(date) / len(date)

for i in date:

    if i < b:
        date_min.append(i)

for i in date:

    if i > b:
        date_max.append(i)

print(f"平均值{b}")
print(f"小于平均值{date_min}")
print(f"大于平均值{date_max}")









