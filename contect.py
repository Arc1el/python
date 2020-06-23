menu = 0
contact = []
while True :
    print("================")
    print("1.친구 리스트 출력")
    print("2.친구추가")
    print("3.친구삭제")
    print("4.이름변경")
    print("9.종료")
    menu = int(input("메뉴를 선택하세요 : "))
    if menu == 1 :
        print(contact)
    elif menu == 2 :
        name = input("이름을 입력하세요 : ")
        contact.append(name)
    elif menu == 3 :
        delName = input("삭제하고 싶은 이름을 입력하세요 : ")
        if delName in contact:
            contact.remove(delName)
        else :
            print("이름이 발견되지 않음")
    elif menu == 4 :
        oldName = input("변경하고싶은 이름을 입력하세요 : ")
        if oldName in contact :
            index = contact.index(oldName)
            newName = input("새로운 이름을 입력하세요 : ")
            contact[index] = newName
        else :
            print("이름이 발견되지 않음")
    elif menu == 9 :
        print("종료합니다.")
        break;
