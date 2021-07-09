'''
  [할당(대입)연산자]
   = : 변수 = 값(변수)
      오른쪽에 있는 값을 왼쪽의 변수에
      할당(대입)한다.
  [축약표현]
  +=,-=,*=,%=..등등
  변수1 += 값(변수2) => 변수1 = 변수1+값 혹은
  변수1 = 변수1+변수2
'''
#대입 연산자(=)로 초기화
#대입 연산자의 오른쪽식이 항상 먼저 실행된후
#그 결과값을 왼쪽의 변수에 대입
#num1만 선언시 [x]
#num1#NameError: name 'num1' is not defined
num1=100
num2 = num1
#200 = num2#[x]왼쪽에는 항상 변수가 와야 한다.
#2]축약표현
#※산술연산자에만 적용
num1+=100#num1 = num1 + 100
print('num1:{},num2:{}'.format(num1,num2))
num1%=num2#num1= num1 % num2
print('num1:{},num2:{}'.format(num1,num2))
num2 *= 2+10#num2 = num2 * (2+10)
print('num1:{},num2:{}'.format(num1,num2))



