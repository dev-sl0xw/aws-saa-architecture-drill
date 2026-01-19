"""
일별 콘텐츠 데이터 모델

각 일차별 상세 학습 콘텐츠 구조를 정의합니다.
"""

from datetime import datetime
from typing import List, Literal
from pydantic import BaseModel, Field, HttpUrl


class DailyContentMetadata(BaseModel):
    """일별 콘텐츠 메타데이터"""
    
    day_number: int = Field(..., ge=1, le=7, description="주 내 일차 번호")
    week_number: int = Field(..., ge=1, le=4, description="주차 번호")
    global_day_number: int = Field(..., ge=1, le=30, description="전체 일차 번호")
    topic: str = Field(..., min_length=1, description="일차 주제")
    created_at: datetime = Field(default_factory=datetime.now, description="생성 시각")


class OverviewSection(BaseModel):
    """개요 섹션"""
    
    description: str = Field(..., min_length=1, description="일차 설명")
    learning_objectives: List[str] = Field(default_factory=list, description="학습 목표")
    prerequisites: List[str] = Field(default_factory=list, description="선수 지식")


class ScenarioSection(BaseModel):
    """실제 시나리오 섹션"""
    
    context: str = Field(..., min_length=1, description="시나리오 배경")
    business_requirements: List[str] = Field(default_factory=list, description="비즈니스 요구사항")
    technical_challenges: List[str] = Field(default_factory=list, description="기술적 과제")


class Concept(BaseModel):
    """핵심 개념"""
    
    name: str = Field(..., min_length=1, description="개념 이름")
    what: str = Field(..., min_length=1, description="정의")
    why: str = Field(..., min_length=1, description="시나리오에서 필요한 이유")
    config_rationale: str = Field(default="", description="설정값 선택 이유")
    official_docs: List[str] = Field(default_factory=list, description="AWS 공식 문서 URL")


class KeyConceptsSection(BaseModel):
    """핵심 개념 섹션"""
    
    concepts: List[Concept] = Field(default_factory=list, description="개념 목록")


class Procedure(BaseModel):
    """콘솔 실습 절차"""
    
    step_number: int = Field(..., ge=1, description="단계 번호")
    title: str = Field(..., min_length=1, description="단계 제목")
    instructions: List[str] = Field(default_factory=list, description="실행 지침")
    screenshots: List[str] = Field(default_factory=list, description="스크린샷 또는 상세 설명")
    expected_outcome: str = Field(default="", description="예상 결과")
    troubleshooting: List[str] = Field(default_factory=list, description="문제 해결 팁")


class CleanupStep(BaseModel):
    """리소스 정리 단계"""
    
    step_number: int = Field(..., ge=1, description="단계 번호")
    resource_type: str = Field(..., min_length=1, description="리소스 타입")
    deletion_order: int = Field(..., ge=1, description="삭제 순서")
    instructions: List[str] = Field(default_factory=list, description="삭제 지침")
    verification: str = Field(default="", description="삭제 확인 방법")


class ConsoleLabContent(BaseModel):
    """콘솔 실습 콘텐츠"""
    
    objectives: List[str] = Field(default_factory=list, description="실습 목표")
    procedures: List[Procedure] = Field(default_factory=list, description="실습 절차")
    cleanup_steps: List[CleanupStep] = Field(default_factory=list, description="정리 단계")
    estimated_time: int = Field(default=60, ge=1, description="예상 소요 시간 (분)")


class SecurityGroupRule(BaseModel):
    """보안 그룹 규칙"""
    
    port: int = Field(..., ge=1, le=65535, description="포트 번호")
    protocol: str = Field(default="tcp", description="프로토콜")
    source: str = Field(default="0.0.0.0/0", description="소스 CIDR")
    description: str = Field(default="", description="규칙 설명")


class CiCdPipeline(BaseModel):
    """CI/CD 파이프라인 설정"""
    
    github_actions_workflow: str = Field(default="", description="GitHub Actions YAML")
    dockerfile: str = Field(default="", description="Dockerfile 내용")
    slack_webhook: str = Field(default="", description="Slack Webhook URL")


class TestContent(BaseModel):
    """테스트 코드"""
    
    unit_tests: str = Field(default="", description="단위 테스트")
    integration_tests: str = Field(default="", description="통합 테스트")
    cdk_assertions: str = Field(default="", description="CDK Assertions")


class CleanupConfig(BaseModel):
    """정리 설정"""
    
    removal_policy: str = Field(default="DESTROY", description="삭제 정책")
    auto_delete_objects: bool = Field(default=True, description="객체 자동 삭제")


class CdkLabContent(BaseModel):
    """CDK 실습 콘텐츠"""
    
    language: Literal["typescript", "python"] = Field(default="typescript", description="구현 언어")
    instance_type: str = Field(default="t2.micro", description="인스턴스 타입")
    security_group_rules: List[SecurityGroupRule] = Field(default_factory=list, description="보안 그룹 규칙")
    key_pair_name: str = Field(default="", description="키 페어 이름")
    stack_code: str = Field(default="", description="CDK 스택 코드")
    cicd_pipeline: CiCdPipeline = Field(default_factory=CiCdPipeline, description="CI/CD 파이프라인")
    tests: TestContent = Field(default_factory=TestContent, description="테스트 코드")
    cleanup_config: CleanupConfig = Field(default_factory=CleanupConfig, description="정리 설정")
    estimated_time: int = Field(default=90, ge=1, description="예상 소요 시간 (분)")


class TestCase(BaseModel):
    """테스트 케이스"""
    
    name: str = Field(..., min_length=1, description="테스트 이름")
    description: str = Field(..., min_length=1, description="테스트 설명")
    test_code: str = Field(default="", description="테스트 코드")
    expected_result: str = Field(default="", description="예상 결과")


class VerificationContent(BaseModel):
    """검증 콘텐츠"""
    
    objectives: List[str] = Field(default_factory=list, description="검증 목표")
    test_cases: List[TestCase] = Field(default_factory=list, description="테스트 케이스")
    tools: List[str] = Field(
        default_factory=lambda: ["pytest", "boto3", "moto", "CDK Assertions"],
        description="사용 도구"
    )


class Question(BaseModel):
    """퀴즈 문제"""
    
    question_number: int = Field(..., ge=1, le=5, description="문제 번호")
    question_text: str = Field(..., min_length=1, description="문제 내용")
    options: List[str] = Field(..., min_length=4, max_length=4, description="선택지 (4개)")
    correct_answer: Literal["A", "B", "C", "D"] = Field(..., description="정답")
    explanation: str = Field(..., min_length=1, description="해설")
    related_concept: str = Field(default="", description="관련 개념")


class Quiz(BaseModel):
    """일별 퀴즈"""
    
    questions: List[Question] = Field(..., min_length=5, max_length=5, description="문제 목록 (정확히 5개)")


class DailyContent(BaseModel):
    """일별 콘텐츠"""
    
    metadata: DailyContentMetadata = Field(..., description="메타데이터")
    overview: OverviewSection = Field(..., description="개요")
    scenario: ScenarioSection = Field(..., description="시나리오")
    architecture_diagram: str = Field(default="", description="아키텍처 다이어그램 (Mermaid.js)")
    key_concepts: KeyConceptsSection = Field(default_factory=KeyConceptsSection, description="핵심 개념")
    console_lab: ConsoleLabContent = Field(default_factory=ConsoleLabContent, description="콘솔 실습")
    cdk_lab: CdkLabContent = Field(default_factory=CdkLabContent, description="CDK 실습")
    verification: VerificationContent = Field(default_factory=VerificationContent, description="검증")
    quiz: Quiz = Field(..., description="일별 퀴즈")
