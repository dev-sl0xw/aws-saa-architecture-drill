"""
실러버스 데이터 모델

30일 커리큘럼의 전체 구조를 정의합니다.
"""

from datetime import datetime
from typing import List, Literal
from pydantic import BaseModel, Field


class DayOverview(BaseModel):
    """일차 개요 정보"""
    
    day_number: int = Field(..., ge=1, le=7, description="주 내 일차 번호 (1-7)")
    global_day_number: int = Field(..., ge=1, le=30, description="전체 일차 번호 (1-30)")
    topic: str = Field(..., min_length=1, description="일차 주제")
    aws_services: List[str] = Field(default_factory=list, description="다루는 AWS 서비스 목록")
    difficulty: Literal["beginner", "intermediate", "advanced"] = Field(
        default="beginner",
        description="난이도"
    )
    estimated_hours: int = Field(default=4, ge=1, le=8, description="예상 학습 시간 (시간)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "day_number": 1,
                "global_day_number": 1,
                "topic": "Cloud Operations Foundation & VPC",
                "aws_services": ["VPC", "EC2", "CloudWatch"],
                "difficulty": "beginner",
                "estimated_hours": 4
            }
        }


class Week(BaseModel):
    """주차 정보"""
    
    week_number: int = Field(..., ge=1, le=4, description="주차 번호 (1-4)")
    theme: str = Field(..., min_length=1, description="주차 테마")
    description: str = Field(..., min_length=1, description="주차 설명")
    days: List[DayOverview] = Field(default_factory=list, description="일차 목록")
    
    class Config:
        json_schema_extra = {
            "example": {
                "week_number": 1,
                "theme": "Cloud Operations Foundation & Core Networking",
                "description": "클라우드 운영 기초와 핵심 네트워킹 개념을 학습합니다.",
                "days": []
            }
        }


class SyllabusMetadata(BaseModel):
    """실러버스 메타데이터"""
    
    version: str = Field(default="1.0.0", description="실러버스 버전")
    created_at: datetime = Field(default_factory=datetime.now, description="생성 시각")
    target_exam: str = Field(default="SAA-C03", description="목표 자격증")
    total_days: int = Field(default=30, ge=1, description="총 일수")
    language: str = Field(default="ko", description="콘텐츠 언어")
    
    class Config:
        json_schema_extra = {
            "example": {
                "version": "1.0.0",
                "created_at": "2024-01-01T00:00:00",
                "target_exam": "SAA-C03",
                "total_days": 30,
                "language": "ko"
            }
        }


class Syllabus(BaseModel):
    """30일 커리큘럼 실러버스"""
    
    metadata: SyllabusMetadata = Field(default_factory=SyllabusMetadata, description="메타데이터")
    weeks: List[Week] = Field(default_factory=list, description="주차 목록")
    
    def get_day_by_global_number(self, global_day: int) -> DayOverview | None:
        """전체 일차 번호로 일차 정보 조회"""
        for week in self.weeks:
            for day in week.days:
                if day.global_day_number == global_day:
                    return day
        return None
    
    def get_total_days(self) -> int:
        """총 일차 수 계산"""
        return sum(len(week.days) for week in self.weeks)
    
    class Config:
        json_schema_extra = {
            "example": {
                "metadata": {
                    "version": "1.0.0",
                    "target_exam": "SAA-C03",
                    "total_days": 30
                },
                "weeks": []
            }
        }
