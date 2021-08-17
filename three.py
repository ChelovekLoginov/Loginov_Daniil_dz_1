text1 = " процент"
text2 = " процента"
text3 = " процентов"
for cou in range(0, 101):
    if 5 <= cou <= 20:
        print(str(cou) + text3)
    elif cou % 10 == 1:
        print(str(cou) + text1)
    elif 5 <= cou % 10 <= 9:
        print(str(cou) + text3)
    elif cou % 10 == 0:
        print(str(cou) + text3)
    else:
        print(str(cou) + text2)
