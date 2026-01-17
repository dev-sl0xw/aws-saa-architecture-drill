# Implementation Plan: AWS SAA-C03 30일 한국어 커리큘럼 시스템

## Overview

이 구현 계획은 AWS SAA-C03 자격증 준비를 위한 30일 한국어 커리큘럼 생성 시스템을 구축합니다. Python을 사용하여 콘텐츠 생성 엔진을 구현하고, 일관된 형식의 학습 자료를 자동으로 생성합니다.

구현은 다음 순서로 진행됩니다:
1. 프로젝트 구조 및 데이터 모델 설정
2. 실러버스 생성 엔진 구현
3. 일별 콘텐츠 생성 엔진 구현
4. 템플릿 엔진 및 검증 시스템 구현
5. 첫 번째 산출물 생성 (30일 실러버스 + Week 1 Day 1)

## Tasks

- [ ] 1. 프로젝트 구조 및 데이터 모델 설정
  - Python 프로젝트 디렉토리 구조 생성 (src/, tests/, templates/, output/)
  - 데이터 모델 클래스 정의 (Syllabus, Week, Day, DailyContent 등)
  - Pydantic을 사용한 데이터 검증 모델 구현
  - 설정 파일 (config.yaml) 생성 - 한국어, SAA-C03, 30일, Free Tier 등
  - _Requirements: 1.4, 9.1, 9.2, 9.3, 9.4_

- [ ]* 1.1 데이터 모델 검증 테스트 작성
  - **Property 4: Directory Structure Consistency**
  - **Validates: Requirements 1.4, 9.1, 9.2, 9.3, 9.4, 9.5**

- [ ] 2. 실러버스 생성 엔진 구현
  - [ ] 2.1 CurriculumPlanner 클래스 구현
    - 학습자 프로필 분석 (강점/약점 영역)
    - 30일 학습 경로 생성 로직
    - _Requirements: 1.1, 1.2, 1.3_
  
  - [ ] 2.2 SyllabusGenerator 클래스 구현
    - 4주 구조 생성 (Week 1-2: 기초/약점, Week 3-4: 통합)
    - 각 주별 테마 및 일별 주제 할당
    - SAA-C03 exam domain 전체 커버리지 보장
    - _Requirements: 1.1, 1.2, 1.3, 10.1, 10.5_
  
  - [ ] 2.3 실러버스 출력 기능 구현
    - Markdown 형식으로 30일 실러버스 문서 생성
    - 각 일차별 주제, AWS 서비스, 학습 목표 포함
    - _Requirements: 10.1, 10.5_

- [ ]* 2.4 실러버스 생성 검증 테스트
  - **Property 1: Complete Syllabus Coverage**
  - **Property 2: Weak Area Prioritization**
  - **Property 3: Integration Scenario Sequencing**
  - **Validates: Requirements 1.1, 1.2, 1.3, 10.1, 10.5**

- [ ] 3. Checkpoint - 실러버스 생성 확인
  - 30일 실러버스가 올바르게 생성되는지 확인
  - 모든 테스트가 통과하는지 확인
  - 사용자에게 질문이 있으면 물어보기

- [ ] 4. 일별 콘텐츠 생성 엔진 구현
  - [ ] 4.1 DailyContentGenerator 클래스 구현
    - Day 정보를 받아 DailyContent 객체 생성
    - Overview, Scenario, Key Concepts 생성 로직
    - _Requirements: 2.1, 2.2, 2.4_
  
  - [ ] 4.2 Architecture Diagram Generator 구현
    - Mermaid.js 구문으로 아키텍처 다이어그램 생성
    - 각 일차의 AWS 서비스 및 리소스 관계 시각화
    - _Requirements: 2.3_
  
  - [ ] 4.3 Key Concepts Generator 구현
    - What (정의), Why (시나리오 맥락), Official Docs (AWS 문서 URL) 생성
    - AWS 공식 문서 URL 자동 생성 및 검증
    - _Requirements: 2.4, 2.8_

- [ ]* 4.4 콘텐츠 생성 검증 테스트
  - **Property 6: README Section Completeness**
  - **Property 7: AWS Documentation References**
  - **Validates: Requirements 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8**

- [ ] 5. Console Lab 생성 엔진 구현
  - [ ] 5.1 ConsoleLabGenerator 클래스 구현
    - 학습 목표 생성 (리소스 연결 관계 이해)
    - 단계별 절차 생성 (스크린샷 설명 포함)
    - SSM Session Manager 접속 가이드 포함
    - _Requirements: 3.1, 3.2, 3.3_
  
  - [ ] 5.2 Console Lab Cleanup Generator 구현
    - 생성된 모든 리소스에 대한 삭제 절차 생성
    - 삭제 순서 및 검증 단계 포함
    - Part 2 진행 전 완전 삭제 보장
    - _Requirements: 3.4, 3.5, 6.2, 6.4, 6.5_

- [ ]* 5.3 Console Lab 검증 테스트
  - **Property 8: Console Lab SSM Access**
  - **Property 9: Console Lab Cleanup Completeness**
  - **Validates: Requirements 3.2, 3.4, 3.5, 6.2, 6.4, 6.5**

- [ ] 6. CDK Lab 생성 엔진 구현
  - [ ] 6.1 CdkLabGenerator 클래스 구현
    - TypeScript 또는 Python CDK 코드 생성
    - Free Tier 인스턴스 타입 (t2.micro/t3.micro) 사용
    - Security Group Port 22 + Key Pair 설정
    - _Requirements: 4.1, 4.2, 4.3_
  
  - [ ] 6.2 CDK Cleanup Configuration Generator 구현
    - removalPolicy: DESTROY 설정
    - autoDeleteObjects: true 설정 (S3)
    - 모든 리소스 자동 삭제 보장
    - _Requirements: 4.4, 6.3_
  
  - [ ] 6.3 CI/CD Pipeline Generator 구현
    - GitHub Actions workflow YAML 생성
    - Dockerfile 생성
    - Slack 알림 통합 설정
    - _Requirements: 4.5, 4.6, 4.7_
  
  - [ ] 6.4 CDK Tagging Strategy 구현
    - 모든 CDK 스택에 태그 추가
    - 비용 배분 태그 포함
    - _Requirements: 5.3_

- [ ]* 6.5 CDK Lab 검증 테스트
  - **Property 10: CDK Free Tier Compliance**
  - **Property 11: CDK SSH Access Configuration**
  - **Property 12: CDK Perfect Cleanup Configuration**
  - **Property 13: CI/CD Tool Selection**
  - **Property 14: CDK Code Syntax Validity**
  - **Property 16: CDK Tagging Implementation**
  - **Validates: Requirements 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 5.3, 6.3**

- [ ] 7. Verification 및 Quiz 생성 엔진 구현
  - [ ] 7.1 VerificationGenerator 클래스 구현
    - pytest 기반 테스트 코드 생성
    - boto3, moto, CDK Assertions 사용
    - 각 주요 컴포넌트에 대한 테스트 케이스 생성
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_
  
  - [ ] 7.2 QuizGenerator 클래스 구현
    - 정확히 5문제 생성
    - 각 문제에 4개 선택지, 정답, 상세 해설 포함
    - Key Concepts와 연계된 문제 생성
    - 한국어로 작성
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_

- [ ]* 7.3 Verification 및 Quiz 검증 테스트
  - **Property 18: Test Framework Usage**
  - **Property 19: Test Coverage Completeness**
  - **Property 20: Quiz Structure Compliance**
  - **Property 21: Quiz Content Alignment**
  - **Validates: Requirements 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 8.1, 8.2, 8.3, 8.4, 8.5**

- [ ] 8. 템플릿 엔진 및 README 생성 구현
  - [ ] 8.1 TemplateEngine 클래스 구현
    - Jinja2 템플릿 엔진 설정
    - README, Console Lab, CDK Lab 템플릿 생성
    - 한국어 콘텐츠 렌더링
    - _Requirements: 1.5, 2.1_
  
  - [ ] 8.2 ReadmeGenerator 클래스 구현
    - 모든 섹션을 통합한 README.md 생성
    - Mermaid 다이어그램 삽입
    - 한국어 형식 및 마크다운 구조 보장
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7_

- [ ]* 8.3 템플릿 렌더링 검증 테스트
  - **Property 5: Korean Language Completeness**
  - **Validates: Requirements 1.5, 8.5**

- [ ] 9. 콘텐츠 검증 시스템 구현
  - [ ] 9.1 ContentValidator 클래스 구현
    - README 필수 섹션 검증
    - 한국어 콘텐츠 검증 (영어 전용 섹션 감지)
    - Console Lab cleanup 완전성 검증
    - CDK cleanup 설정 검증
    - Quiz 구조 검증 (5문제, 정답, 해설)
    - AWS 문서 URL 유효성 검증
    - _Requirements: 모든 검증 관련 요구사항_
  
  - [ ] 9.2 ValidationResult 처리 로직 구현
    - 에러 및 경고 메시지 생성
    - 검증 실패 시 상세 리포트 출력
    - _Requirements: 모든 검증 관련 요구사항_

- [ ]* 9.3 검증 시스템 테스트
  - 각 검증 규칙에 대한 단위 테스트
  - 잘못된 콘텐츠 감지 테스트
  - 모든 Correctness Properties 검증

- [ ] 10. Checkpoint - 전체 시스템 통합 확인
  - 모든 컴포넌트가 올바르게 통합되었는지 확인
  - 모든 테스트가 통과하는지 확인
  - 사용자에게 질문이 있으면 물어보기

- [ ] 11. 거버넌스 및 복원력 콘텐츠 생성
  - [ ] 11.1 AWS Config 및 Tagging Strategy 콘텐츠 추가
    - Day 19 (AWS Config) 콘텐츠 생성
    - Day 20 (Cost Management & Tagging) 콘텐츠 생성
    - _Requirements: 5.1, 5.2, 5.4_
  
  - [ ] 11.2 Resilience Pattern 콘텐츠 추가
    - 아키텍처 다이어그램에 Multi-AZ, Auto Scaling 등 포함
    - 복원력 패턴 설명 추가
    - _Requirements: 6.1_

- [ ]* 11.3 거버넌스 콘텐츠 검증 테스트
  - **Property 15: Governance Topic Coverage**
  - **Property 17: Resilience Pattern Inclusion**
  - **Validates: Requirements 5.1, 5.2, 5.4, 6.1**

- [ ] 12. 첫 번째 산출물 생성
  - [ ] 12.1 30일 전체 실러버스 생성
    - SyllabusGenerator를 사용하여 완전한 30일 계획 생성
    - Markdown 파일로 출력 (syllabus.md)
    - _Requirements: 10.1_
  
  - [ ] 12.2 Week 1 / Day 1 상세 콘텐츠 생성
    - 주제: "Cloud Operations Foundation & VPC"
    - 모든 필수 섹션 포함 (Overview, Diagram, Concepts, Labs, Quiz)
    - week1/day1/ 디렉토리 구조 생성
    - README.md, part1_console/, part2_cdk/ 생성
    - _Requirements: 10.2, 10.3_
  
  - [ ] 12.3 Day 1 콘텐츠 품질 검증
    - ContentValidator로 모든 검증 규칙 확인
    - 템플릿 및 품질 표준 확인
    - _Requirements: 10.3_

- [ ]* 12.4 첫 번째 산출물 검증 테스트
  - Day 1 콘텐츠가 모든 요구사항을 충족하는지 확인
  - 실러버스가 30일 전체를 커버하는지 확인
  - **Validates: Requirements 10.1, 10.2, 10.3**

- [ ] 13. 최종 통합 및 문서화
  - [ ] 13.1 사용자 가이드 작성
    - 시스템 사용 방법 (한국어)
    - 커리큘럼 생성 명령어
    - 커스터마이징 방법
  
  - [ ] 13.2 개발자 문서 작성
    - 코드 구조 설명
    - 새로운 일차 추가 방법
    - 템플릿 수정 방법
  
  - [ ] 13.3 README.md 작성
    - 프로젝트 개요
    - 설치 및 실행 방법
    - 예제 출력물

- [ ] 14. 최종 Checkpoint - 전체 시스템 검증
  - 모든 테스트가 통과하는지 확인
  - 30일 실러버스 및 Day 1 콘텐츠가 완벽하게 생성되는지 확인
  - 사용자에게 최종 확인 요청

## Notes

- 모든 콘텐츠는 한국어로 작성됩니다 (코드 블록, URL, 기술 식별자 제외)
- Python 3.9+ 사용
- 주요 라이브러리: Pydantic (데이터 검증), Jinja2 (템플릿), PyYAML (설정), pytest (테스트)
- 테스트는 optional로 표시되어 있지만, 품질 보장을 위해 구현 권장
- 각 checkpoint에서 사용자 확인 후 다음 단계 진행
- Free Tier 준수 및 완벽한 cleanup이 핵심 원칙
