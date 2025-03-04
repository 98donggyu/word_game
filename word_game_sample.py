## 파일 처리 및 리스트 자료 구조 저장
    # data/word.txt 파일 로딩하여 읽기 (word file)

## 필요한 내장, 외장 모듈 불러오기
    # 필요한 내장모듈 import
    # 미디어 파일 처리를 위한 pygame 모듈 설치 및 import하기

import random # 단어 무작위 선택
import time #게임시작 부터 종료까지 총 걸린 시간 측정을 위해
from pygame  import mixer
mixer.init()

path = "data\word.txt"
# file = open(path,"r")
words = []

# 파일 읽기 예외 처리
try: 
    file = open(path, "r", encoding='UTF8')
except IOError as err:
    print("I/O error:{0}".format(err))
else:
    read_words = file.readlines()
    for word in read_words:
        # 각단어의 공백 및 뉴라인 캐릭터 제거
        word = word.rstrip("\n")
        # 각 단어를 words리스트에 저장 (리스트네임: words)
        words.append(word)
finally:
    file.close()

# with open(path,"r",encoding='UTF8') as file:
#     read_words = file.readlines()
# 제시어 출력           
print(words)
    
input("게임 시작을 원하시면 Enter키를 눌러주세요!")
#게임출력
start = time.time()

# 문제 출력 & 입력
n = 1
cor_cnt = 0
while n <= 5 :  #단어 입력 횟수를 총 5번 반복 
    random.shuffle(words)  #words리스트에서 임의 단어 한개 추출
    q = random.choice(words) 
    print("문제 # {}".format(n)) 
    print(q) #제시어 화면 출력
    x = input() #사용자 입력
    print() #입력한 단어 출력

# 정답 확인 (제시된 단어와 입력한 단어가 일치하는지 판단 --> 맞춘 개수 카운트하기
    if str(q).strip() == str(x).strip():
        print("정답!") #맞췄을때, 틀렸을때 효과음 내기와 문자 출력 가산점
        mixer.music.load('assets/good.wav')  # 맞을 때의 소리 파일
        # print("good!") #소리출력여부 확인
        mixer.music.play()
        cor_cnt += 1
    else:
        print("오답!!!")
        mixer.music.load('assets/bad.wav')  # 틀렸을 때의 소리 파일
        mixer.music.play()
        #print("beep!")

    n += 1
end = time.time() 

# 3. 게임 종료 결과 메세지
game_time = end - start # 걸린 시간 변수
game_time = format(game_time, ".3f")

print('-------------게임 종료!-------------') # 게임 종료 메세지


# 합격, 불합격 메세지, 3개 이상 맞추면 합격, 2개 이하로 맞추면 불합격 출력
if cor_cnt >= 3:        
    print('합격!')
else:
    print('불합격!')

# 게임시간, 정답개수 안내 메세지
print("게임 시간 : {} / 정답 개수 : {}".format(game_time, cor_cnt))



