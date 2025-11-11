from mcp.server.fastmcp import FastMCP      # MCP 서버를 쉽게 만들 수 있도록 도와주는 FastMCP를 가져온다.
from supervisor import Supervisor           # 우리 쪽 멀티에이전트 시스템(Supervisor)를 가져온다.

mcp = FastMCP("multi-agent-demo")           # MCP 서버 인스턴스를 만든다
sv = Supervisor()                           # Supervisor 인스턴스 생성

@mcp.tool()                                 # MCP "툴(TOOL)" 정의
def route_message(message : str) -> str:
    """
    멀티 에이전트에게 사용자의 메시지를 전달하고,
    그 처리 결과를 문자열로 돌려주는 MCP Tool 함수.

    매개변수(parameter)
    -----------
    message : str
        MCP 클라이언트(예 : Chatgpt, Claude Desktop, IDE 등)에게 넘겨주는 텍스트 명령.
        예)
        - "math 3 5"
        - "text hello world"
        - "time"

        반환값(return)
        ----------
        str
            Supervisor가 적절한 에이전트를 선택해 처리한 뒤 돌려주는 응답 문자열
    """
    return sv.route(message)

if __name__ == "__main__":
    mcp.run()