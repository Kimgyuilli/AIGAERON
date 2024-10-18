def GetMaxDay(year, month):
    #한 달의 마지막 날 반환
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 14:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 31

print("달력 출력 프로그램")
while(True):
    year = int(input("찾을 년도 입력: (끝내려면 -1 입력)"))
    if year == -1: break
    month = int(input("찾을 월 입력: "))
    print(year, "년 ", month, "월")
    days = ['일', '월', '화', '수', '목', '금', '토']
    
    #연도 뒤 두 자리 끊어서 저장(계산을 위해)
    ye = year // 100
    ar = year % 100

    #1, 2월은 전 년도 13월, 14월로 처리
    if month < 3:
        month += 12
        ar -= 1
        #세기가 바뀔 때 년도 처리
        if ar < 0:
            ar = 99
            ye -= 1

    #첫 날 요일 계산(Zeller 공식)
    FirstDay = (ar + (ar // 4) + (ye // 4) - 2 * ye + ((26 * (month + 1)) // 10) + 1 - 1) % 7

    #해당 달의 마지막 날 계산
    DaysInMonth = GetMaxDay(int(year), month)
        
    print(" ".join(days))
    print("--------------------")
        
    CurDay = FirstDay
    #첫 주 공백처리
    print("   " * FirstDay, end="")
    #1일부터 출력
    for day in range(1, DaysInMonth + 1):
        print(f"{day:2d} ", end="")
        CurDay += 1
        if CurDay % 7 == 0:
            print()  # 주가 끝나면 줄바꿈
    print("\n")
