"""
20163309 해양컴퓨터공학과 김현민
전산언어 기말프로젝트과제 - 냉장고 재고관리시스템

데이터파일(fridgeData.txt)파일을 사용하여 냉장고의 상태를 저장, 불러오고
냉장고에 데이터를 추가하고 데이터파일을 갱신하며 냉장고의 재고를 관리할수있는 시스템
냉장고정보는 ":" 를, 일반 제품데이터는 ","를 구분자로사용하여 데이터를 사용
fridgeData.txt는 프로그램과 동일 디렉토리에 위치해야하며 파일이 없는경우 초기설정을통해 생성가능

fridgeData.txt 의 구성 ==================================
(첫번째줄)냉장고이름:냉장고의 최대용량:냉장고의 현재재고량
(두번째줄이후)제품이름,유통기한(유통기한의형식은 YYYYMMDD의 형태)

아쉬웠던 점
1. 데이터파일을 튜플이나 리스트의 형태로 저장하였으면 sort하는데 더 쉽게 진행되었을것 같았으나
실력미달로 인해 문자열에 구분자를 사용해 저장하게되어 이를 유통기한순으로 정렬하는데 sorted함수를 사용하지못해 따로 구현해야 했다.

2. 강의 후반부에 클래스를 사용하는 내용이 있었으나 이미 프로그래밍이 어느정도 진행되어졌기 때문에 클래스를 미사용하였다.
사용하게되었으면 냉장고 여러대를 관리하게 프로그래밍 할 수 있었을것 같다.
"""


def selectInit():  # 초기설정 결정함수
    answer = input("초기설정을 진행하시겠습니까? (y/n) !주의 y이외 입력시 기존의 데이터가 삭제됩니다! : ")
    if answer == "y":
        return True
    else:
        return False


def initFridge():  # 냉장고 초기설정함수
    fName = input("냉장고 이름을 설정해주세요 : ")
    fMax = input("냉장고에 들어갈수있는 최대물건 갯수를 설정해주세요 : ")
    datafile = open("fridgeData.txt", "w")  # w 모드로 열었기때문에 파일 초기화될 수 있음
    datafile.write(fName)  # 결론적으로 냉장고이름:냉장고 최대용량:현재용량(초기화이므로 0)으로 저장
    datafile.write(":")
    datafile.write(fMax)
    datafile.write(":0" + "\n")
    datafile.close()


def printMenu():  # 메뉴출력함수
    print("========================================")
    print("|          냉장고 관리 프로그램            |")
    print("========================================")
    print("| 1. 냉장고 남은용량 보기                  |")
    print("| 2. 냉장고에 제품추가                    |")
    print("| 3. 냉장고 제품보기                      |")
    print("| 4. 냉장고 유통기한 임박순 출력            |")
    print("| 5. 냉장고 제품찾기                      |")
    print("| 6. 냉장고 제품삭제                      |")
    print("| 이외의 아무입력시 프로그램이 종료됩니다     |")
    print("========================================")
    return int(input("| 메뉴를 입력하세요 : "))


def storeItem():  # 데이터파일에 식품을 저장하는 함수
    global fridgeNow
    str1 = input("식품 이름을 입력해주세요 ex)우유 : ")
    str2 = input("유통기한을 입력해주세요 ex)20200710 : ")
    storeData = str1 + "," + str2 + "\n"
    datafile = open("fridgeData.txt", "a")
    datafile.write(storeData)
    fridgeNow += 1
    datafile.close()
    answer = input("제품을 더 입력하시겠습니까? (y/n) : ")
    if answer == "y":
        return True
    else:
        return False


def updateInfo(name, max, now):  # 식품을 저장하거나 변동점이있을때 파일의 맨첫줄의 냉장고 상태 업데이트하는 함수
    infoData = []
    with open('fridgeData.txt', 'r') as datafile:
        infoData = datafile.readlines()
    with open('fridgeData.txt', 'w') as datafile:
        datafile.write(name + ":" + str(max) + ":" + str(now) + "\n")  # 첫째줄에 냉장고상태를 새로 작성
        datafile.writelines(infoData[:0] + infoData[1:])  # 기존의 냉장고상태를 제외한채 파일을 작성
    datafile.close()


def printFridge():  # 냉장고의 현재상태 출력
    print("현재 " + fridgeName + "에 ", fridgeNow, "개의 제품이 들어있습니다. \n남은용량은", fridgeMax - fridgeNow, "개 입니다.")


def printItem():  # 냉장고의 식품들을 오래전에 넣은 순서대로 출력(파일에 기록된대로)
    datafile = open("fridgeData.txt", "r")
    iList = []
    for i in range(fridgeNow + 1):
        iList.append(datafile.readline().rstrip('\n'))
    datafile.close()
    del iList[0]

    print("|  제품이름\t|      유통기한     |")
    for i in range(len(iList)):
        item = iList[i].split(',')
        year = item[1][0:4]
        month = item[1][4:6]
        day = item[1][7:9]
        print("|  %5s\t|  %s년 %s월 %s일  |" % (item[0], year, month, day))


def sortItem():
    tempList = []  # 데이터를 가져와 임시 복사
    datafile = open("fridgeData.txt", "r")
    for i in range(fridgeNow + 1):
        tempList.append(datafile.readline().rstrip('\n'))
    datafile.close()
    del tempList[0]

    sList = []  # 가져온 데이터를 활용하여 :로 구분지은 필드의 두번째만 담게될 배열
    for i in range(len(tempList)):
        sList.append(tempList[i].split(',')[1])
    sList.sort()  # sort 함으로써 유통기한만 정렬되어 담겨지게됨

    print("|  제품이름\t|      유통기한     |")
    for i in range(1, len(sList)):
        for j in range(len(tempList)):
            fIndex = tempList[j].find(sList[i]) - 1
            if fIndex >= 0:
                item = tempList[j][0:fIndex]
                year = tempList[j][fIndex + 1:][0:4]
                month = tempList[j][fIndex + 1:][4:6]
                day = tempList[j][fIndex + 1:][7:9]
                print("|  %5s\t|  %s년 %s월 %s일  |" % (item, year, month, day))


def findItem(text):  # 상품명을 매개변수로 전달받아 찾는함수
    fList = []  # 데이터를 가져와 임시 복사
    datafile = open("fridgeData.txt", "r")
    for i in range(fridgeNow + 1):
        fList.append(datafile.readline().rstrip('\n'))
    datafile.close()
    del fList[0]

    print("|  제품이름\t|      유통기한     |")
    for i in range(6):
        fIndex = fList[i].find(text)  # text를 찾음. 성공한경우 0이상의 값을 리턴(인덱스)
        if fIndex >= 0:  # 찾은경우
            item = fList[i].split(',')
            year = item[1][0:4]
            month = item[1][4:6]
            day = item[1][7:9]
            print("|  %5s\t|  %s년 %s월 %s일  |" % (item[0], year, month, day))


def delItem(text):  # 제품명을 매개변수로 전달받아 해당 인덱스의 배열을 삭제하는 함수
    global fridgeNow
    fList = []  # 데이터를 가져와 임시 복사
    datafile = open("fridgeData.txt", "r")
    for i in range(fridgeNow + 1):
        fList.append(datafile.readline().rstrip('\n'))
    datafile.close()
    del fList[0]

    for i in range(6):
        if fList[i].find(text) >= 0:  # 찾은경우
            fridgeNow -= 1
            with open('fridgeData.txt', 'r') as datafile:
                infoData = datafile.readlines()
            with open('fridgeData.txt', 'w') as datafile:  # 냉장고상태 업데이트랑 같은원리. 해당줄을 빼고 파일을 작성
                datafile.writelines(infoData[:i + 1] + infoData[i + 2:])
            datafile.close()


# 여기서부터 main
fridgeName = ""  # 냉장고이름
fridgeMax = 0  # 냉장고 최대용량
global fridgeNow  # 전역변수 fridgeNow. 현재 냉장고에 들어간 물품 상태를 기록
fridgeNow = 0

if selectInit():  # selectInit이 참인경우. 초기화를 한다고 응답한경우
    initFridge()  # 초기화
    datafile = open("fridgeData.txt", "r")  # 데이터파일에서 냉장고 정보를 가져옴
    fridgeInfo = datafile.readline().rstrip('\n')
    datafile.close()
    tempArr = fridgeInfo.split(':', maxsplit=2)
    fridgeName = tempArr[0]
    fridgeMax = int(tempArr[1])
    fridgeNow = int(tempArr[2])
else:  # 초기화를 하지 않는다고 응답한경우 곧바로 데이터파일에서 냉장고 정보를 가져옴
    datafile = open("fridgeData.txt", "r")
    fridgeInfo = datafile.readline().rstrip('\n')
    datafile.close()
    tempArr = fridgeInfo.split(':', maxsplit=2)
    fridgeName = tempArr[0]
    fridgeMax = int(tempArr[1])
    fridgeNow = int(tempArr[2])
    print("기존의 냉장고가 선택되었습니다. 냉장고이름은 " + fridgeName + ", 냉장고의 남은용량은 ", fridgeMax - fridgeNow, " 입니다.")

while 1:  # 메뉴를 선택하여 프로그램 동작시작
    select = printMenu()
    if select == 1:  # 냉장고 상태보기
        printFridge()
    elif select == 2:  # 제품 추가
        if fridgeMax == fridgeNow:  # 냉장고가 가득 찬경우
            print("| 냉장고가 가득찼습니다.")
            break;
        while storeItem():  # 더이상 추가를 원하지 않을때까지 무한반복
            updateInfo(fridgeName, fridgeMax, fridgeNow)  # 냉장고 상태를 업데이트 (데이터파일의 첫줄을 갱신)
    elif select == 3:  # 냉장고의 제품들을 입력한 순서대로 출력 (데이터파일에 적혀있는순서)
        printItem()
    elif select == 4:  # 냉장고의 제품들을 유통기한 임박순서대로 출력 (데이터파일을 :구분자로 읽어 2번째 필드를 비교)
        sortItem()
    elif select == 5:  # 등록했던 제품을 입력하면 해당 제품의 제품명과 유통기한 표시
        findtext = input("| 찾고자하는 상품을 입력하세요 : ")
        findItem(findtext)
    elif select == 6:  # 등록했던 제품을 찾아 삭제
        findtext = input("| 삭제하고자 하는 상품을 입력하세요 : ")
        delItem(findtext)
    else:  # 프로그램 종료 (1-6 제외 아무입력)
        print("프로그램을 종료합니다. 감사합니다.")
        break;
