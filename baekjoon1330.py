#두 정수 A와 B가 주어졌을 때, A와 B를 비쇼하는 프로그램을 작성하시오.
a=int(input('첫 번째  수를 입력하세요'))
b=int(input('두 번째 수를 입력하세요'))

if a>b:
    print('>')
elif a<b:
    print('<')
elif a==b:
    print('==')
    