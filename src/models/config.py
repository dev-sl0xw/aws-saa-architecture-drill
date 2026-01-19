"""
시스템 설정 데이터 모델

커리큘럼 생성 시스템의 전역 설정을 정의합니다.
"""

from typing import List, Literal
from pydantic import BaseModel, Field


class CurriculumConfig(BaseModel):
    """커리큘럼 설정"""
    
    # 기본 설정
    language: Literal["ko"] = Field(default="ko", description="콘텐츠 언어")
    target_exam: str = Field(default="SAA-C03", description="목표 자격증")
    duration: int = Field(default=30, ge=1, description="총 일수")
    
    # AWS 설정
    free_tier_only: bool = Field(default=True, description="Free Tier만 사용")
    default_instance_type: Literal["t2.micro", "t3.micro"] = Field(
        default="t2.micro",
        description="기본 인스턴스 타입"
    )
    ec2_access_method: Literal["ssm-session-manager", "ssh"] = Field(
        default="ssm-session-manager",
        description="EC2 접속 방법"
    )
    
    # 개발 도구 설정
    cicd_tool: Literal["github-actions", "aws-codepipeline"] = Field(
        default="github-actions",
        description="CI/CD 도구"
    )
    container_tool: Literal["docker", "podman"] = Field(
        default="docker",
        description="컨테이너 도구"
    )
    notification_tool: Literal["slack", "email"] = Field(
        default="slack",
        description="알림 도구"
    )
    
    # CDK 설정
    cdk_languages: List[Literal["typescript", "python"]] = Field(
        default=["typescript", "python"],
        description="지원 CDK 언어"
    )
    default_cdk_language: Literal["typescript", "python"] = Field(
        default="typescript",
        description="기본 CDK 언어"
    )
    
    # 콘텐츠 생성 설정
    include_architecture_diagrams: bool = Field(default=True, description="아키텍처 다이어그램 포함")
    include_quizzes: bool = Field(default=True, description="퀴즈 포함")
    include_verification_tests: bool = Field(default=True, description="검증 테스트 포함")
    
    # 학습자 프로필 (약점 영역)
    weak_areas: List[str] = Field(
        default=["Networking", "Database", "Storage", "Governance"],
        description="약점 영역 (Week 1-2에 우선 배치)"
    )
    
    # 출력 설정
    output_directory: str = Field(default="output", description="출력 디렉토리")
    template_directory: str = Field(default="templates", description="템플릿 디렉토리")
    
    class Config:
        json_schema_extra = {
            "example": {
                "language": "ko",
                "target_exam": "SAA-C03",
                "duration": 30,
                "free_tier_only": True,
                "default_instance_type": "t2.micro",
                "ec2_access_method": "ssm-session-manager",
                "cicd_tool": "github-actions",
                "container_tool": "docker",
                "notification_tool": "slack",
                "cdk_languages": ["typescript", "python"],
                "default_cdk_language": "typescript",
                "weak_areas": ["Networking", "Database", "Storage", "Governance"]
            }
        }
