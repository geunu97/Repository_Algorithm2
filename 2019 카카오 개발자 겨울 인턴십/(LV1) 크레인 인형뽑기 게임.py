#LV1 크레인 인형뽑기 게임

def solution(board, moves):
    stack = []
    count = 0
    len_value = len(board)
    
    for i in moves:
        for j in range(len_value):
            if board[j][i-1] == 0:
                continue
            else:
                if len(stack) >= 1:
                    if stack[-1] == board[j][i-1]:
                        stack.pop()
                        count += 2
                    else:
                        stack.append(board[j][i-1])
                else:
                    stack.append(board[j][i-1])
                
                board[j][i-1] = 0    #방문처리
                break
                
                #print(stack)                  #프로그래머스 출력 따로     
    return count