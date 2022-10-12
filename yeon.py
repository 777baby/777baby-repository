import random
Dkbb={'가위':'보','바위':'가위','보':'바위'}    #딕셔너리 가위는 보에 이김
rkbb=['가위','바위','보']

vcount=0 #이긴횟수
rcount=0 #진 횟수

for i in range(2): # 2회 게임
    Mkbb=' '

    while Mkbb not in rkbb:   #가위 바위 보 이외의 입력시 다시 입력 받은
        Mkbb=input('가위,바위,보 입력: ')
    Ckbb=random.choice(rkbb)                    #컴퓨터가 결정
    print('나:',Mkbb,'   PC:',Ckbb)
    if Mkbb == Ckbb:
        print('비겼습니다.')
    elif Ckbb == Dkbb[Mkbb]:
        print('우와 승리.')
        vcount+=1
    else:
        print('에구 졌다.')
        rcount+=1
    print()
print(' %d승 %d패'%(vcount,rcount))