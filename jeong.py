def find_string(inputs):
    Ostr=''
    Olst=[]
    for i in inputs:
        if i.isdigit(): #숫자가들어오면
            if len(Ostr)>0:
                Olst.append(Ostr) #문자 모음을 리스트로
                Ostr=''
        else: #문자가 들어오면
            Ostr += i #문자를 모음
    if len(Ostr)>0: #마지막 문자 모음이 있는지확인하여
        Olst.append(Ostr) #문자 모음을 리스트로
    return(Olst)

inputs='cat32dog16cow5'

string_List = find_string(inputs)
print(string_List)