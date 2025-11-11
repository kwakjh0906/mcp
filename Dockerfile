# 1) Python 3.11 버전이 들어있는 기본 이미지 사용
FROM python:3.11-slim

# 2) 컨테이너 안의 작업 디렉토리 설정
WORKDIR /app

# 3) requirements.txt 복사 및 필요한 패키지 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 4) 내 코드 파일들을 모두 복사
COPY . /app

# 5) 컨테이너가 실행될 때 실행할 명령 (여기서는 console.py)
CMD ["python", "console.py"]

