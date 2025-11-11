from datetime import datetime

class BaseAgent:
    def __init__(self, name : str): # 에이전트 이름(디버깅 구분용)
        self.name = name

    def can_handle(self, message : str) -> bool:
        """
        이 에이전트가 '이 요청을 처리할 수 있는지'를 판단하는 함수.
        - Supervisor가 여러 에이전트에서 순서대로 물어볼 때 사용됨.
        - 각 에이전트마다 로직이 다르기 때문에 여기서는 틀만 만들고, 실제 내용은 자식 클래스에서 구현.
        """

        raise NotImplementedError # 자식이 반드시 구현하도록 강제
    
    def handle(self, message : str) -> str:
        """
        실제로 요청을 처리하는 함수.
        - 예 : 수학 에이전트면 계산 수행, 텍스트 에이전트면 문자열 처리.
        """

        raise NotImplementedError # 자식이 반드시 구현하도록 강제
    
# 숫자 계산 담당 에이전트
class MathAgent(BaseAgent): # 부모(BaseAgent)의 생성자 호출해서 이름 세팅
    def __init__(self):
        super().__init__("MathAgent")

    def can_handle(self, message : str) -> bool:
        """
        이 에이전트가 맡은 요청인지 판단.
        - 규칙 : 사용자가 입력한 문장이 'math'로 시작하면 내가 처리하겠다.
        - 예 : 'math 3 5'
        """
        return message.startswith("math")
    
    def handle(self, message : str) -> str:
        """
        실제 계산 처리.
        입력 형식 : "math 3 5"
        1) 입력을 쪼개서 숫자 2개를 꺼낸 뒤
        2) 더해서 결과를 문자열로 반환.
        """

        parts = message.split() # 공백 기준으로 쪼갬

        # 'math 3 5'처럼 총 3개의 덩어리가 아니면 사용법 안내
        if len(parts) != 3:
            return "[MathAgent] 사용법 : math 3 5"
        
        # 두 번째, 세 번째 값을 정수로 변환 시도
        try:
            a = int(parts[1])
            b = int(parts[2])
        except ValueError: # 숫자가 아니라면 에러 메시지
            return "[MathAgent] 숫자를 입력해주세요. 예 : math 3 5"
        
        result = a + b # 결과를 보기 좋게 포맷해서 반환
        return f"[MathAgent] {a} + {b} = {result}"
        

# 텍스트 가공 담당 에이전트
class TextAgent(BaseAgent):
    def __init__(self):
        super().__init__("TextAgent")

    def can_handle(self, message : str) -> bool:
        """
        규칙 : 'text'로 시작하는 입력은 내가 맡는다.
        - 예 : 'text hello world'
        """
        return message.startswith("text")
    
    def handle(self, message : str) -> str:
        """
        'text' 뒤에 오는 문장을 전부 대문자로 바꿔서 반환.
        - 예 : 'text hello world' -> 'HELLO WORLD'
        """

        # "text" 다음부터 끝까지 잘라서 실제 내용만 가져옴
        content = message[len("text "):]

        if not content: # 내용이 비어있으면 사용법 안내
            return "[TextAgent] 사용법 : text 아무_문장"
        return f"[TextAgent] {content.upper()}" # 대문자로 변환해서 반환
            
        
class TimeAgent(BaseAgent):
    def __init__(self):
        super().__init__("TimeAgent")

    def can_handle(self, message : str) -> bool:
        """
        규칙 : 사용자가 'time'이라고만 입력하면 내가 처리.
        - 공백 없이 'time' 딱 한 단어.
        """

        return message.strip() == "time"
    
    def handle(self, message : str) -> str:
        """
        현재 시간을 'YYYY-MM-DD HH:MM:SS' 형식으로 반환.
        """

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[TimeAgent] 지금 시간은 {now} 입니다."