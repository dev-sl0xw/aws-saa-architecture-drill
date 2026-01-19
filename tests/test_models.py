"""
데이터 모델 테스트

Pydantic 모델의 검증 및 직렬화를 테스트합니다.
"""

import pytest
from datetime import datetime

from src.models import (
    Syllabus,
    Week,
    DayOverview,
    DailyContent,
    DailyContentMetadata,
    OverviewSection,
    ScenarioSection,
    Concept,
    Quiz,
    Question,
    CurriculumConfig,
)


class TestSyllabusModels:
    """실러버스 모델 테스트"""
    
    def test_day_overview_creation(self):
        """DayOverview 생성 테스트"""
        day = DayOverview(
            day_number=1,
            global_day_number=1,
            topic="Cloud Operations Foundation & VPC",
            aws_services=["VPC", "EC2"],
            difficulty="beginner",
            estimated_hours=4
        )
        
        assert day.day_number == 1
        assert day.global_day_number == 1
        assert day.topic == "Cloud Operations Foundation & VPC"
        assert len(day.aws_services) == 2
    
    def test_week_creation(self):
        """Week 생성 테스트"""
        week = Week(
            week_number=1,
            theme="Cloud Operations Foundation",
            description="클라우드 운영 기초",
            days=[]
        )
        
        assert week.week_number == 1
        assert week.theme == "Cloud Operations Foundation"
    
    def test_syllabus_creation(self):
        """Syllabus 생성 테스트"""
        syllabus = Syllabus()
        
        assert syllabus.metadata.target_exam == "SAA-C03"
        assert syllabus.metadata.total_days == 30
        assert len(syllabus.weeks) == 0
    
    def test_syllabus_get_total_days(self):
        """Syllabus 총 일수 계산 테스트"""
        day1 = DayOverview(
            day_number=1,
            global_day_number=1,
            topic="Day 1"
        )
        day2 = DayOverview(
            day_number=2,
            global_day_number=2,
            topic="Day 2"
        )
        
        week = Week(
            week_number=1,
            theme="Week 1",
            description="Test week",
            days=[day1, day2]
        )
        
        syllabus = Syllabus(weeks=[week])
        
        assert syllabus.get_total_days() == 2


class TestDailyContentModels:
    """일별 콘텐츠 모델 테스트"""
    
    def test_concept_creation(self):
        """Concept 생성 테스트"""
        concept = Concept(
            name="VPC",
            what="Virtual Private Cloud",
            why="네트워크 격리를 위해 필요",
            official_docs=["https://docs.aws.amazon.com/vpc/"]
        )
        
        assert concept.name == "VPC"
        assert len(concept.official_docs) == 1
    
    def test_question_creation(self):
        """Question 생성 테스트"""
        question = Question(
            question_number=1,
            question_text="VPC란 무엇인가?",
            options=["A. 옵션1", "B. 옵션2", "C. 옵션3", "D. 옵션4"],
            correct_answer="A",
            explanation="VPC는 Virtual Private Cloud입니다."
        )
        
        assert question.question_number == 1
        assert len(question.options) == 4
        assert question.correct_answer == "A"
    
    def test_quiz_validation(self):
        """Quiz 검증 테스트 - 정확히 5문제"""
        questions = [
            Question(
                question_number=i,
                question_text=f"문제 {i}",
                options=["A", "B", "C", "D"],
                correct_answer="A",
                explanation="해설"
            )
            for i in range(1, 6)
        ]
        
        quiz = Quiz(questions=questions)
        assert len(quiz.questions) == 5
    
    def test_quiz_validation_fails_with_wrong_count(self):
        """Quiz 검증 실패 테스트 - 5문제가 아닌 경우"""
        questions = [
            Question(
                question_number=1,
                question_text="문제 1",
                options=["A", "B", "C", "D"],
                correct_answer="A",
                explanation="해설"
            )
        ]
        
        with pytest.raises(Exception):  # Pydantic ValidationError
            Quiz(questions=questions)


class TestConfigModel:
    """설정 모델 테스트"""
    
    def test_config_creation(self):
        """CurriculumConfig 생성 테스트"""
        config = CurriculumConfig()
        
        assert config.language == "ko"
        assert config.target_exam == "SAA-C03"
        assert config.duration == 30
        assert config.free_tier_only is True
        assert config.default_instance_type == "t2.micro"
    
    def test_config_custom_values(self):
        """CurriculumConfig 커스텀 값 테스트"""
        config = CurriculumConfig(
            duration=60,
            default_instance_type="t3.micro",
            default_cdk_language="python"
        )
        
        assert config.duration == 60
        assert config.default_instance_type == "t3.micro"
        assert config.default_cdk_language == "python"
