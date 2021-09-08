# Q42 탑승구

# 답안 예시
# 루트 0에 연결해서 서로소 집합 연산을 한다는 아이디어를 해결하지 못해서 중간까지 풀고 답을 봄

def find_parent(parent, x):
	if parent[x] != x:
		# 그래프와 노드를 넣고 확인
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

g = int(input()) # 탑승구의 개수
p = int(input()) # 비행기의 개수

# 부모 테이블 초기화
parent = [0] * (g+1)
# 부모 테이블 상, 부모를 자기자신으로 초기화
for i in range(1, g+1):
  parent[i] = i

result = 0
for _ in range(p):
  # 비행기 탑승구의 루트확인
  data = find_parent(parent, int(input()))
  if data == 0: #현재 루트가 0이면 종료
    break
  union_parent(parent, data, data -1) # 그렇지 않다면 왼쪽의 집합과 합치기
  result += 1

print(result)