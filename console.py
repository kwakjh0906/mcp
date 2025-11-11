from supervisor import Supervisor

def main():
    """
    콘솔 프로그램의 시작점.
    1. Supervisor를 생성하고
    2. 사용자의 입력을 계속 받으면서
    3. Supervisor에게 처리를 맡기고
    4. 결과를 출력한다.
    """

    # 1) Supervisor 인스턴스 생성
    sv = Supervisor()

    # 2) 초기 안내 메시지 출력
    print("=== Multi-Agent Practice Console ===")
    print("사용 가능한 예시 명령어 : ")
    print(" math 3 5        -> 덧셈 (예 : math 2 4)")
    print(" text hello      -> 대문자로 변환 (예 : text hello world)")
    print(" time            -> 현재 시간 출력")
    print(" exit / quit     -> 프로그램 종료")
    print("====================================")

    # 3) 사용자의 입력을 계속 받는 반복문
    while True:
        # 사용자 입력 받기
        message = input("\nYou > ").strip()

        # 아무 것도 안 쳤으면 다시 입력 받기
        if message == "":
            continue

        # 종료 명령 처리
        if message.lower() in ("exit", "quit"):
            print("프로그램을 종료합니다.")
            break

        # 4) Supervisor에게 이 메시지를 어떻게 처리할 지 맡김
        response = sv.route(message)

        # 5) 결과 출력
        print(response)

# 이 파일을 '직접 실행'했을 때만 main() 함수를 실행하도록 하는 파이썬 관용구.
# 다른 파일에서 import 할 때는 main()이 실행되지 않도록 하기 위함
if __name__ == "__main__":
    main()

