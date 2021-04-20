class User():
    def say_hello(self):
        print("안녕하세요, 저는 {0}입니다.".format(self.name))

    def login(self, my_email, my_password):
        # 로그인 메소드
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

user1 = User()
user2 = User()

user1.name = "Hoon"
user1.email = "ehdgns4038@naver.com"
user1.password = "1234"

user2.name = "Naver"
user2.email = "naver.com"
user2.password = "6789"

#인스턴스 메소드 사용법
# User.say_hello(user1)
# user1.say_hello()

#인스턴스 메소드 특징
# user1.login("ehdgns4038@naver.com", "1234") # 정답! user1이 첫번째 파라미터로 들어간다!
# user1.login(user1, "ehdgns4038@naver.com", "1234") #틀린것이다!!!

