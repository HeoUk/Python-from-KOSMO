print('[리스트 생성 첫번째 : 빈 리스트]')#동적으로 요소 추가시 주로 사용
def pprint(obj):
    print('객체:{},타입:{}'.format(obj,type(obj)))
    if not isinstance(obj,float) and not isinstance(obj,int):
        print('객체의 요소 수:',len(obj))
#방법1-[]
a=[]
pprint(a)
#방법2-list():list클래스의 생성자
a=list()
pprint(a)
print('[리스트 생성 두번째 : 같은 타입의 객체(요소) 저장]')
b=[1,2,3,4,5]#변수 하나에 여러개 데이타 설정:패킹
pprint(b)
print('[리스트 생성 세번째 : 다른 타입의 객체(요소) 저장]')
c=['가길동',20,3.14,True]
pprint(c)
print('[리스트 언팩킹]')
#리스트의 각 요소를 여러 변수에 나눠 담는 것:언패킹(구조분해)
#단, 변수의 개수가 요소의 개수와 일치해야 한다
c1,c2,c3,c4 = c
pprint(c1)
pprint(c2)#TypeError: object of type 'int' has no len()
pprint(c3)#TypeError: object of type 'float' has no len()
pprint(c4)#TypeError: object of type 'bool' has no len()
print('[리스트 생성 네번째 : 문자열로 리스트 만들기]')
s='PYTHON'
list_from_str = list(s)
pprint(list_from_str)
list_from_str = s.split()#문자열 전체를 하나의 요소로 갖는 리스트 반환
pprint(list_from_str)
print('[리스트 생성 다섯번째 :list(range객체)]')
list_from_range=list(range(5))
pprint(list_from_range)
print('[빈 리스트에 값 할당하기]')
#빈 리스트에 값을 할당할때는 [인덱스]=값 으로 할당하는게 아니라 append()함수를 이용해서 할당한다
#a[0]='가길동'#IndexError: list assignment index out of range
a.append('가길동')
a.append(20)
a.append('송파구')
pprint(a)
print('[리스트객체[인덱스]=값 : 해당 인덱스의 값 수정]')
#a[3] = '코스모'#IndexError: list assignment index out of range
a[1]=40
a[len(a)-1]='금천구'
pprint(a)
print('[리스트객체[인덱스] : 해당 인덱스의 값 읽기]')
print('a[0]:{},a[{}]:{}'.format(a[0],len(a)-1,a[len(a)-1]))
print('[리스트의 요소수 구하기:len()]')
print('총 요소수:',len(list(range(100,1000,2))))
print('[리스트 슬라이싱]')
#c=['가길동', 20, 3.14, True]
print(c[1:1])#[] 빈 리스트
print(c[1:3])#[20, 3.14]
print(c[1:-3])#1부터 -4(-3-1)까지 []
#[:끝인덱스] -  처음부터 끝인덱스-1까지
print(c[:4])
#[시작인덱스:] -  시작인덱스부터 끝까지
print(c[-len(c):])
#[:] -  모든 요소 슬라이싱
print(c[:])
print('[for문을 이용해서 리스트의 인덱스 및 요소 가져오기]')
f=['가','나','다','라']
for element in f:#요소만 출력
    print(element)
for index in range(len(f)):##요소와 인덱스 출력
    print('인덱스:{},요소:{}'.format(index,f[index]))
#for 인덱스, 값 in enumerate(순서가 있는 객체):  #인덱스와 값을 동시에 꺼내올 수 있다
for index,element in enumerate(f):#요소와 인덱스 출력
    print('인덱스:{},요소:{}'.format(index,element))




