# AWS SAA-C03 30일 한국어 커리큘럼 생성 시스템

AWS Solutions Architect Associate (SAA-C03) 자격증 범위의 인프라 지식을 밑바닥부터 체계적으로 학습하기 위한 30일 커리큘럼 자동 생성 시스템입니다.

## 프로젝트 개요

이 시스템은 AWS 콘솔 실습과 AWS CDK 코드 구현을 통해 실무 중심의 학습 경험을 제공합니다. "Learn by Doing" 철학을 바탕으로, 각 일차는 다음 두 가지 파트로 구성됩니다:

- **Part 1 (Console Lab)**: AWS 콘솔에서의 수동 실습을 통한 Mental Model 구축
- **Part 2 (CDK Lab)**: AWS CDK를 통한 Infrastructure as Code 구현 및 자동화

## 주요 특징

- 30일 완성 구조화된 커리큘럼
- 약점 영역 우선 학습 (Week 1-2: Networking, Database, Storage, Governance)
- 통합 시나리오 중심 학습 (Week 3-4)
- SSM Session Manager 기반 EC2 접속
- Free Tier 준수 (t2.micro/t3.micro)
- 완벽한 리소스 정리 (removalPolicy: DESTROY)
- GitHub Actions + Docker + Slack 통합
- 일별 5문제 퀴즈 및 자동화 테스트
- 모든 콘텐츠 한국어 제공

## 커리큘럼 구조

### Week 1: Cloud Operations Foundation & Core Networking
- Day 1-5: VPC 기초부터 고급 네트워킹까지
- Day 6-7: 통합 실습 및 복습

### Week 2: Storage & Database Foundations
- Day 8-13: S3, EBS, EFS, RDS, Aurora
- Day 14: 통합 실습 및 복습

### Week 3: Compute & Governance
- Day 15-20: EC2, Lambda, Container, Config, Cost Management
- Day 21: 통합 실습 및 복습

### Week 4: Integration & Advanced Scenarios
- Day 22-27: CloudFormation, Monitoring, Security, DR, Multi-Region
- Day 28-30: 최종 통합 프로젝트 및 시험 준비

## 프로젝트 구조

```
.
├── src/                    # 소스 코드
│   ├── models/            # 데이터 모델 (Pydantic)
│   ├── generators/        # 콘텐츠 생성 엔진
│   ├── validators/        # 콘텐츠 검증 시스템
│   └── utils/             # 유틸리티 함수
├── templates/             # Jinja2 템플릿
│   ├── readme.md.j2
│   ├── console_lab.md.j2
│   └── cdk_lab.md.j2
├── tests/                 # 테스트 코드
├── output/                # 생성된 커리큘럼 출력
│   ├── syllabus.md
│   └── week{n}/day{n}/
└── config.yaml            # 시스템 설정
```

## 설치 및 실행

### 요구사항

- Python 3.9+
- pip 또는 uv

### 설치

```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는
venv\Scripts\activate     # Windows

# 의존성 설치
pip install -r requirements.txt
```

### 실행

```bash
# 30일 전체 실러버스 생성
python -m src.main generate-syllabus

# 특정 일차 콘텐츠 생성
python -m src.main generate-day --week 1 --day 1

# 전체 커리큘럼 생성
python -m src.main generate-all
```

## 생성되는 콘텐츠

각 일차별로 다음 콘텐츠가 자동 생성됩니다:

### README.md
- Overview (학습 목표 및 실제 시나리오)
- Architecture Diagram (Mermaid.js)
- Key Concepts (What, Why, Official Docs)
- Hands-on Part 1: Console Lab
- Hands-on Part 2: CDK Lab
- Verification (자동화 테스트)
- Daily Quiz (5문제 + 정답 + 해설)

### part1_console/
- 단계별 콘솔 실습 가이드
- SSM Session Manager 접속 방법
- 완벽한 리소스 정리 절차

### part2_cdk/
- TypeScript/Python CDK 코드
- GitHub Actions CI/CD 설정
- Dockerfile
- Slack 알림 통합
- pytest 테스트 코드

## 핵심 원칙

### 1. Free Tier 준수
모든 실습은 AWS Free Tier 범위 내에서 진행됩니다.
- EC2: t2.micro 또는 t3.micro
- RDS: db.t2.micro 또는 db.t3.micro
- 기타 서비스: Free Tier 한도 내 사용

### 2. 완벽한 정리 (Perfect Cleanup)
비용 발생을 방지하기 위한 완벽한 리소스 정리:
- Console Lab: 단계별 수동 삭제 가이드
- CDK Lab: `removalPolicy: DESTROY`, `autoDeleteObjects: true`

### 3. 실무 중심 학습
- 실제 비즈니스 시나리오 기반
- GitHub Actions + Docker + Slack 통합
- VS Code Remote SSH 지원

### 4. 검증 및 테스트
- pytest 기반 자동화 테스트
- boto3 + moto를 통한 AWS 서비스 모킹
- CDK Assertions를 통한 인프라 테스트

## 개발

### 테스트 실행

```bash
# 전체 테스트
pytest

# 특정 테스트
pytest tests/test_syllabus_generator.py

# 커버리지 확인
pytest --cov=src tests/
```

### 새로운 일차 추가

1. `config.yaml`에서 커리큘럼 설정 수정
2. 필요시 템플릿 커스터마이징 (`templates/`)
3. 콘텐츠 생성 실행
4. 검증 테스트 실행

## 기술 스택

- **언어**: Python 3.9+
- **데이터 검증**: Pydantic
- **템플릿 엔진**: Jinja2
- **설정 관리**: PyYAML
- **테스트**: pytest, moto
- **CDK**: AWS CDK (TypeScript/Python)
- **CI/CD**: GitHub Actions
- **컨테이너**: Docker
- **알림**: Slack

## 라이선스

MIT License

## 기여

이슈 및 풀 리퀘스트를 환영합니다.

## 문의

프로젝트 관련 문의사항은 이슈를 통해 남겨주세요.
