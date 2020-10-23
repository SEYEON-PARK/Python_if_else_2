time=float((input("근무시간을 입력하시오. : ")))
hourMoney=int(input("시간당 임금을 입력하시오. : "))

if time>=40:
    total=time*hourMoney*1.5
else:
    total=time*hourMoney
print("총임금은 ", total)
