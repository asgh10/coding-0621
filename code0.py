'''
x = ['f','a','r','t']
print (x[2])
print (x[1])
print (x[0])
print (x[3])
'''

#파이썬의 연결 리스트
#리스트처럼 붙어서 저장하지 않고
#데이터->다음데이터->다음데이터
#구조: 데이터 : 다음 데이터(노드) 주소z 

class Node:
    def __init__(self,data): #생성자 함수 Node 객체가 만들어 질때 자동실행 됨
        self.data = data    #노드가 저장 할 실제 데이터
        self.next = None    #다음 노드를 가리키는 변수
        #처음에는 다음노드가 없으므로 Node


#객체 생성
node1 = Node(10)
node2 = Node(20)

print("node1 데이터:", node1.data)
print("node2 데이터:", node2.data)

#연결
node1.next = node2
print("node1이 가르키는 다음 노드 데이터:", node1.next.data)
#즉:
#node1 -> node2 -> data 값 출력
