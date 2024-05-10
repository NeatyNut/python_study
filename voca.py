import os
import random
lo = str(input("불러오거나 새로만들 메모장 이름 입력\n"
                "기존 'voca' 메모장을 이용해도 됩니다\n"
                ">>> "))
f = open(lo + ".txt", "a")
f.close()
try :
    while True :
        n = int(input("단어장 설정 목록\n"
        "1. 단어 추가\n"
        "2. 퀴즈\n"
        "3. 단어 목록 보기\n"
        "5. 뒤로가기/종료\n"
        ">>> "))
        os.system("cls")
        if n == 1 :
            f = open(lo + ".txt", "a")
            while True :
                print("종료:5")
                st1 = str(input("단어 : "))
                if st1 == "5" :
                    break
                st2 = str(input("뜻 : "))
                if st2 == "5" :
                    break
                print()
                f.write(st1 + ":" + st2 + "\n")
            f.close()
        if n == 2 :
            li = []
            f = open(lo + ".txt", "r")
            for i in f.readlines() :
                li.append(i.split(":"))
            if len(li) < 4 :
                print("퀴즈를 풀기위한 단어가 적습니다")
                os.system("pause")
                os.system("cls")
                f.close()
            else :
                while True :
                    li1 = dict(li)
                    g1 = list(li1.keys())
                    g2 = list(li1.values())
                    n = random.choice(g1)
                    print(n + "의 뜻은 ??\n")
                    li2 = set({})
                    while len(li2) != 4 :
                        m = random.choice(g2)
                        li2.add(m)
                        li2.add(li1[n])
                    li3 = list(li2)
                    random.shuffle(li3)
                    for i in range(4) :
                        print("({}) {}".format(i + 1, li3[i]))
                    an = int(input("(종료:5)정답은?>>> "))
                    if an == 5 :
                        f.close()
                        break
                    if li1[n] == li3[an - 1] :
                        print("\n정답 입니다^^\n")
                        os.system("pause")
                        os.system("cls")
                        f.close()
                    else :
                        print("\n틀렸어~~\n")
                        fff = li1[n]
                        print("정답은? {}".format(fff))
                        os.system("pause")
                        os.system("cls")
                        f.close()
        if n == 3 :
            f = open(lo + ".txt", "r")
            ii = f.read()
            if ii != "" :
                print(ii)
                os.system("pause")
                os.system("cls")
                f.close()
            else :
                print("단어가 존재 하지않습니다")
                os.system("pause")
                os.system("cls")
                f.close()
        if n == 5 :
            f.close()
            break
        else :
            print("단어장 설정에 들어왔습니다")
except :
    print("오류 발생 다시 로드하세요\n")
    

