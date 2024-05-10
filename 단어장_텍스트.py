start = 0

while start == 0 :
    import os
    qs = str(input("처음 시작하나요 ?(Y/N) : "))

    if qs == "Y" or qs == "y" :
        try :
            with open('단어장.txt','r') as f :
                list_text = f.read()

            print("")
            print("존재하는 파일이 있습니다")
            print("")

            qq = str(input("기존의 파일을 그대로 사용하시겠습니까?(Y/N) : "))

            if qq == "Y" or qq == "y" :
                os.system("cls")
                start = 1
                n = 0
            
            elif qq == "N" or qq == "n" :
                first_word = str(input("첫 단어를 입력해주세요 : "))
                first_mean = str(input("해당 단어의 의미를 입력해주세요 : "))

                with open('단어장.txt','w') as f :
                    f.write(first_word + " : " + first_mean + "\n")
                    f.close()
                    os.system("cls")
                    start = 1            
                    n = 0
            
            else :
                print("")
                print("올바른 명령을 입력해주세요.")
                print("")        

        except :
            first_word = str(input("첫 단어를 입력해주세요 : "))
            first_mean = str(input("해당 단어의 의미를 입력해주세요 : "))

            with open('단어장.txt','w') as f :
                f.write(first_word + " : " + first_mean + "\n")
                f.close()
                os.system("cls")
                start = 1            
                n = 0

    elif qs == "N" or qs == "n" :
        try :
            with open('단어장.txt','r') as f :
                list_text = f.read()
                f.close
                os.system("cls")
                start = 1
                n = 0
        except :
            print("")
            print("메타파일이 없는 관계로 새로 생성하겠습니다.")
            print("")

            first_word = str(input("첫 단어를 입력해주세요 : "))
            first_mean = str(input("해당 단어의 의미를 입력해주세요 : "))

            with open('단어장.txt','w') as f :
                f.write(first_word + " : " + first_mean + "\n")
                f.close()
                os.system("cls")
                start = 1            
                n = 0

    else :
        print("")
        print("올바른 명령을 입력해주세요.")
        print("")        
    
while n == 0 :
    import os
    qs1 = int(input("1:단어추가\n2:수정,삭제\n3:퀴즈\n4:단어목록표\n0:종료\n입력 : "))

    if qs1 == 1 : 
        n = 1
        os.system("cls")
        z = 0
        while z == 0 : 
            with open('단어장.txt','a') as f :
                add_word = str(input("단어입력(이전화면 : 0) : "))

                if add_word == "0" :
                    z = 1
                    os.system("cls")
                    n = 0
                                
                else :
                    with open('단어장.txt','r') as f :
                        list_text = f.readlines()
                        index = -1

                        for i in range(0, len(list_text)) :
                            find_txt = str(list_text[i])
                            for j in range(0, len(find_txt)) :
                                if find_txt[j] == ":" :
                                    xy = j
                                    find_word = find_txt[0:xy-1]
                                    break

                            if find_word == add_word :
                                print("")
                                print("추가하실 단어가 이미 존재합니다.")
                                print("")
                                index = i

                            else :
                                if i == len(list_text) -1 :
                                    if index == -1 :
                                        f.close

                                        with open('단어장.txt','a') as f1 :
                                            add_mean = str(input("단어뜻 : "))                
                                            f1.write(add_word + " : " + add_mean + "\n")
                                            f1.close()
            
    if qs1 == 2 :
        n = 1
        os.system("cls")
        with open('단어장.txt','r') as f :
            list_text = f.readlines()
            select_word = str(input("수정할 단어(아무 글자 입력 시 이전화면) : "))
            index = -1

            for i in range(0, len(list_text)) :
                find_txt = str(list_text[i])
                for j in range(0, len(find_txt)) :
                    if find_txt[j] == ":" :
                        xy = j
                        replace_word = find_txt[0:xy-1]
                        replace_mean = find_txt[xy+2:len(find_txt)-1]
                        break

                if replace_word == select_word :   
                    print("")
                    print("선택하신 단어를 찾았습니다!")
                    print("")
                    index = i
                    qs2 = int(input("1:단어 수정\n2:뜻 수정\n0:돌아가기\n입력 : "))                            
                    break
                
                else :
                    if i == len(list_text) -1 :
                        if index == -1 :
                            f.close
                            os.system("cls")
                            print("")
                            print("선택하신 단어가 없습니다.")
                            qs2 = 0                
        if qs2 == 1 :
            print("")
            edit_word = str(input("새로 입력할 단어(미 변경 시 : 0) : "))

            if edit_word == "0" :
                list_text[index] = replace_word + " : " + replace_mean + "\n"
            else :
                list_text[index] = edit_word + " : " + replace_mean + "\n"

            for l in range(0, len(list_text)) :
                if l == 0 :
                    with open('단어장.txt','w') as f1 :
                        f1.write(list_text[l])
                        f1.close
                else :
                    with open('단어장.txt', 'a') as f1 :
                        f1.write(list_text[l])
                        f1.close  

            print("")
            print("수정되었습니다.")
            print("")
            n = 0

        if qs2 == 2 :
            print("")
            print("기존 뜻 : " + replace_mean)
            print("")
            edit_mean = str(input("바꿀 뜻(미 변경시 : 0) : "))

            if edit_mean == "0" :
                list_text[index] = replace_word + " : " + replace_mean  + "\n"
            else :
                list_text[index] = replace_word + " : " + edit_mean  + "\n"
            
            for l in range(0, len(list_text)) :
                if l == 0 :
                    with open('단어장.txt','w') as f1 :
                        f1.write(list_text[l])
                        f1.close
                else :
                    with open('단어장.txt', 'a') as f1 :
                        f1.write(list_text[l])
                        f1.close   

            print("")
            print("수정되었습니다.")
            print("")
            n = 0

        if qs2 == 0 :
            if index != -1 :
                os.system("cls")
                n = 0
            else :
                print("")
                n = 0

    if qs1 == 0 :
        n = 1

    if qs1 == 3 :
        n = 1
        os.system("cls")
        with open('단어장.txt','r') as f :
            list_text = f.readlines()

            if len(list_text) < 4 :
                print("")
                print("퀴즈를 낼 수 있을만큼 단어목록이 존재 하지 않습니다")
                print("")
                n = 0

            else :
                m = 0
                while m == 0 :
                    import random
                    os.system("cls")
                    quiz = ["","","",""]
                    quiz[0] = str(random.choice(list_text))
                    
                    while quiz[1] == "" or quiz[0] == quiz[1] :
                        quiz[1] = str(random.choice(list_text))

                    while quiz[2] == "" or quiz[2] == quiz[0] or quiz[2] == quiz[1] :   
                        quiz[2] = str(random.choice(list_text))
                    
                    while quiz[3] == "" or quiz[3] == quiz[0] or quiz[3] == quiz[1] or quiz[3] == quiz[2] :
                        quiz[3] = str(random.choice(list_text))


                    quiz_word = ["","","",""]
                    quiz_mean = ["","","",""]

                    for q in range(0, 4) :
                        quiz_text = quiz[q]
                        for w in range(0, len(quiz_text)) :
                            if quiz_text[w] == ":" :
                                xy1 = w
                                quiz_word[q] = quiz_text[0:xy1-1]
                                quiz_mean[q] = quiz_text[xy1+2:len(quiz_text)-1]
                                break
                        
                    quiz_number = int(random.choice([0,1,2,3]))

                    print("단어 " + quiz_word[quiz_number] + "의 뜻은 무엇일까요?")
                    print("")
                    print("(1) " + quiz_mean[0] + "  (2) " + quiz_mean[1] + "  (3) " + quiz_mean[2] + "  (4) " + quiz_mean[3])
                    print("")
                        
                    answer = int(input(">>>>>>답 선택(이전화면 : 0) : "))

                    if answer == 1 or answer == 2 or answer == 3 or answer == 4 :
                        if answer - 1 == quiz_number :
                            print("")
                            print("짝짝! 정답입니다.")
                            print("")
                            os.system("pause")

                        else :
                            print("")
                            print("아이고 틀렸습니다.")
                            print("")
                            os.system("pause")

                    elif answer == 0 :
                        m = 1
                        os.system("cls")
                        n = 0
                    else :
                        print("")
                        print("올바른 값을 입력해주세요.")
                        print("")

    if qs1 == 4 :
        os.system("cls")
        with open('단어장.txt','r') as f :
            list_text = f.read()
            print(list_text)