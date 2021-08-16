text1 = " процент"
text2 = " процента"
text3 = " процентов"
cou = 0
for cou in range(0, 100):
    cou += 1
    if 5 <= cou <= 20:
        print(str(cou) + text3)
    elif cou % 10 == 1:
        print(str(cou) + text1)
    elif cou % 10 == (5, 9):
        print(str(cou) + text3)
    else:
        print(str(cou) + text2)