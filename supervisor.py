from agents import MathAgent, TextAgent, TimeAgent

class Supervisor:
    """
    여러 에이전트를 관리하는 '조정자(관리자)' 역할.

    하는 일 :
    1. 사용할 에이전트들을 등록해 두고
    2. 사용자의 입력을 보고
    3. 어떤 에이전트가 처리할지 골라서 맡긴 뒤
    4. 그 결과를 돌려준다.

    사용자는 Supervisor에게만 말하고,
    어떤 에이전트가 실제 처리했는지는 몰라도 된다.
    (-> 이게 바로 멀티에이전트 구조의 핵심 아이디어)
    """

    def __init__(self):
        """
        Supervisor가 시작될 때,
        사용할 에이전트들을 미리 생성해서 목록에 넣어둔다.
        """

        # 나중에 에이전트를 추가하고 싶으면 여기 리스트에만 새 에이전트를 넣으면 된다.
        self.agents = [
            MathAgent(),
            TextAgent(),
            TimeAgent(),
        ]

    def route(self, message : str) -> str:
        """
        들어온 메시지를 보고,
        각 에이전트에게 "너 이거 처리할 수 있어?"라고 물어본 뒤,
        처리할 수 있는 에이전트를 찾으면 그 에이전트에게 일을 맡긴다.

        처리 과정 :
        1. self.agents를 순서대로 돌면서
        2. agent.can_handle(message)가 True인 애를 찾고
        3. 찾으면 agent.handle(message)를 호출해서 결과를 반환
        4. 아무도 못 하면 기본 안내 메시지 반환
        """

        # 등록된 에이전트들을 순서대로 확인
        for agent in self.agents:
            if agent.can_handle(message): # 이 에이전트가 처리할 수 있다고 했으니, 실제 처리 맡김
                return agent.handle(message)
            
        
        # 여기까지  왔다는 건, 어느 에이전트도 처리 불가라는 뜻
        # 사용자에게 사용할 수 있는 명령어를 안내해준다.
        return (
            "[Supervisor] 이해할 수 없는 명령입니다. \n"
            "사용 가능 예시 : \n"
            " math 3 5      -> 덧셈\n"
            " text hello    -> 대문자로 변환\n"
            " time          -> 현재 시간"
        )
