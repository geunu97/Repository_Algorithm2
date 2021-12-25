#LV2 행렬 테두리 회전하기

#사각형 테두리만 한칸씩 이동하는 문제 & 최솟값 찾기

def rotate(x1, y1, x2, y2, graph):

    s = graph[x1][y1]  #맨 왼쪽 맨 위에 값
    list_new = []
	
    #핵심1) 왼쪽 열을 위로 한칸씩 올리기
    for x in range(x1, x2):
        graph[x][y1] = graph[x + 1][y1]
        list_new.append(graph[x][y1])
        
    #핵심2) 아래 행을 왼쪽으로 한칸씩 이동하기
    for y in range(y1, y2):
        graph[x2][y] = graph[x2][y + 1]
        list_new.append(graph[x2][y])
        
    #핵심3) 오른쪽 열을 아래로 한칸씩 내리기
    for x in range(x2, x1, -1):
        graph[x][y2] = graph[x-1][y2]
        list_new.append(graph[x][y2])

    #핵심4) 위에 행을 오른쪽으로 한칸씩 밀기(x1,y1+1에서 시작해야 함)
    for y in range(y2, y1 + 1, -1):
        graph[x1][y] = graph[x1][y - 1]
        list_new.append(graph[x1][y])
        
    graph[x1][y1+1] = s
    list_new.append(s)
    
    return min(list_new)
        
    
def solution(rows, columns, queries):
    answer = []
    
    graph = [[1] * columns for _ in range(rows)]   #행 열

    for i in range(rows):
        for j in range(columns):
            graph[i][j] = ((i) * columns + j + 1)  #값 넣기

    for x1, y1, x2, y2 in queries:
        answer.append(rotate(x1-1, y1-1, x2-1, y2-1, graph)) # -1씩 해주고 넣기

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
#print(solution(100,97,[[1,1,100,97]]))

#https://ssinee.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%96%89%EB%A0%AC-%ED%85%8C%EB%91%90%EB%A6%AC-%ED%9A%8C%EC%A0%84%ED%95%98%EA%B8%B0-python3-level2
#정리해서 노트에 써놓기