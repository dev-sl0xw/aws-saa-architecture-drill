"""
데이터 모델 패키지

AWS SAA-C03 30일 커리큘럼 시스템의 핵심 데이터 모델을 정의합니다.
"""

from .syllabus import Syllabus, Week, DayOverview
from .daily_content import (
    DailyContent,
    OverviewSection,
    ScenarioSection,
    Concept,
    KeyConceptsSection,
    ConsoleLabContent,
    Procedure,
    CleanupStep,
    CdkLabContent,
    SecurityGroupRule,
    CiCdPipeline,
    TestContent,
    CleanupConfig,
    VerificationContent,
    TestCase,
    Quiz,
    Question,
)
from .config import CurriculumConfig

__all__ = [
    # Syllabus models
    "Syllabus",
    "Week",
    "DayOverview",
    # Daily content models
    "DailyContent",
    "OverviewSection",
    "ScenarioSection",
    "Concept",
    "KeyConceptsSection",
    "ConsoleLabContent",
    "Procedure",
    "CleanupStep",
    "CdkLabContent",
    "SecurityGroupRule",
    "CiCdPipeline",
    "TestContent",
    "CleanupConfig",
    "VerificationContent",
    "TestCase",
    "Quiz",
    "Question",
    # Config
    "CurriculumConfig",
]
