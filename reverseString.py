while True:
    string = input("문자열 하나를 입력하세요 종료(q) : ")
    if(string == 'q'):
        print('프로그램을 종료합니다.')
        break;
    
    strLen = len(string)

    for i in range(0, strLen):
        print(string[-i-1])
        i += 1
