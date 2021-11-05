def solution(new_id):
    list_check = ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/']
                  
    #1,2단계
    new_id_list = []
    for i in new_id:
        if i in list_check:
            continue
        else:
            if chr(65) <= i <= chr(90):
                i = i.lower()
                new_id_list.append(i)
            else:
                new_id_list.append(i)
            
    #3단계
    new_id_list2 = []
    de = 0
    for i in new_id_list:
        if i == '.':
            de += 1
            if de == 1: 
                new_id_list2.append('.')
        else:
            de = 0
            new_id_list2.append(i)
        
    #4단계
    if new_id_list2[len(new_id_list2)-1] == '.':
        del new_id_list2[len(new_id_list2)-1]
        
    if len(new_id_list2) != 0:
        if new_id_list2[0] == '.' :
            del new_id_list2[0]
        
    #5단계
    if len(new_id_list2) == 0:
        new_id_list2.append('a')
        
    #6단계
    new_id_list3 = []
    if len(new_id_list2) >= 16:
        for i in range(15):
            new_id_list3.append(new_id_list2[i])
    else:
        new_id_list3 = new_id_list2

        
    if new_id_list3[len(new_id_list3)-1] == '.':
        del new_id_list3[len(new_id_list3)-1]
      
    #7단계
    if len(new_id_list3) <= 2:
        add_value = new_id_list3[len(new_id_list3)-1]
        for _ in range(3):
            if len(new_id_list3) == 3:
                break
            else:
                new_id_list3.append(add_value)
    
                
        
    answer = "".join(new_id_list3)
    return answer