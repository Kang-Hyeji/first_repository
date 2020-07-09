# 1주일 내용 10문제로 끝내기

# 1. 파이썬 조건문을 활용하여 장발장은 빵을 못먹게 하기
# - 실행 예시 : "장발장 차례 입니다, 빵을 드릴 수 없습니다."
# - 실행 예시 : "홍길동 차례 입니다, 빵을 하나 드리겠습니다."

people = ['홍길동', '성진', '심청이', '장발장', '심봉사']

print('============문제 1번============')
for i in people :
    print(f'{i} 차례 입니다, ', end='')
    if i =='장발장':
        print('빵을 드릴 수 없습니다.')
    else : 
        print('빵을 하나 드리겠습니다.')


# --------------------------------------------------------

# 2. 1번 문제의 구현된 부분을 함수로 바꾸기
# - 조건 : 입력값(사람 한 명씩) 을 받아서 빵을 먹으면 안되는 사람이면 0을, 먹어도 되면 1을 반환하기
# - 실행 예시 : "홍길동은 빵을 먹을 수 있는 사람 입니다."
# - 실행 예시 : "장발장은 빵을 먹을 수 없는 사람 입니다."
# 반복문을 활용하여 5 명 전원 다 출력 할 것
print('============문제 2번============')

def bread(name):
    print(f'{name}은 빵을 ', end='')
    if name == '장발장' :
        print('먹을 수 없는 사람입니다.')
        return 0
    else :
        print('먹을 수 있는 사람입니다.')
        return 1

for i in people :
    check = bread(i)


# --------------------------------------------------------

# 3. 지역변수와 전역변수 이해하기

# 아래의 코드는 num_stamp 라는 전역변수를 함수 내에서 global 명령을 통해 수정가능하게 억지로 만든상태이다.
# 하지만, 함수의 기능과 본질을 생각하면 아래의 예시는 굉장히 바람직하지 못하다!
# global 명령은 안쓰는 것이 좋다!
# 그렇다면, global 명령을 사용하지 않고 아래의 로직을 함수의 입력값과 반환값을 활용하여 수정해보기!
print('============문제 3번============')

num_stamp = 0  # 쿠폰 스탬프가 찍힌 횟수 (전역변수)


def stamp(num):
    """쿠폰 스탬프가 찍힌 횟수를 증가시키고, 화면에 출력한다."""         # num_stamp는 전역변수다
    num = num + 1  # 오류가 발생하지 않는다 (global 안쓰면 오류 발생함)
    print(num)

    return num


num_stamp=stamp(num_stamp)  # 화면에 1이 출력된다
num_stamp=stamp(num_stamp)  # 화면에 2가 출력된다


# --------------------------------------------------------

# 4. 클래스 이용하기
# 요구사항
# - 교통수단 클래스 만들기 (속성 : 이름, 가격, 출발시간, 도착시간 / 기능 : 출발시간, 도착시간 보기)
# - 비행기 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 수하물 가능여부
# 기능 : 출발시간, 도착시간 보기, 수하물 맡기기(수하물이 가능하면 "수하물을 맡겼습니다!"출력, 불가능하면 "이 비행기는 수하물을 못맡깁니다!" 출력)
# - 기차 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 좌석등급
# 기능 : 출발시간, 도착시간 보기, 좌석등급 보기

# 클래스를 상속을 활용해서 효율적으로 만들어 볼것! (메소드 오버라이딩)
# 두 개 이상의 인스턴스를 비행기, 기차 각각 만들어 볼것
print('============문제 4번============')

class transport:
    def __init__(self, name, charge, start, arrive):
        self.name = name
        self.charge = charge
        self.start = start
        self.arrive = arrive

    def start_time(self):
        return self.start
    def arrive_time(self):
        return self.arrive

class airplane(transport):
    def __init__(self, name, charge, start, arrive, baggage):
        super().__init__(name, charge, start, arrive)
        self.baggage=baggage

    def baggage_possible(self):
        if self.baggage == 'yes':
            print('수하물을 맡겼습니다!')
        elif self.baggage == 'no' :
            print('이 비행기는 수하물을 못맡깁니다!')

class train(transport):
    def __init__(self, name, charge, start, arrive, grade):
        super().__init__(name, charge, start, arrive)
        self.grade=grade
    def train_class(self):
        return self.grade


air001=airplane('air001','55000','08:50','10:20','no')
air002=airplane('air002','125000','12:30','22:10','yes')

tra100=train('tra100','25000','16:30','18:20','B')
tra200=train('tra200','45000','07:30','09:00','A')

print(f'{air001.name}의 출발 시간 : {air001.start_time()}')
print(f'{air001.name}의 도착 시간 : {air001.arrive_time()}')
air001.baggage_possible()

print(f'{air002.name}의 출발 시간 : {air002.start_time()}')
print(f'{air002.name}의 도착 시간 : {air002.arrive_time()}')
air002.baggage_possible()

print(f'{tra100.name}의 출발 시간 : {tra100.start_time()}')
print(f'{tra100.name}의 도착 시간 : {tra100.arrive_time()}')
print(f'좌석등급 : {tra100.train_class()}')

print(f'{tra200.name}의 출발 시간 : {tra200.start_time()}')
print(f'{tra200.name}의 도착 시간 : {tra200.arrive_time()}')
print(f'좌석등급 : {tra200.train_class()}')


# --------------------------------------------------------

# 5. 문자열 이용하기


# 파이썬 io 하는거 2 문제
