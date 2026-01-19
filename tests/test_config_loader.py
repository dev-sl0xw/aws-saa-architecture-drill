"""
설정 로더 테스트
"""

import pytest
from pathlib import Path

from src.utils.config_loader import load_config
from src.models.config import CurriculumConfig


class TestConfigLoader:
    """설정 로더 테스트"""
    
    def test_load_default_config(self):
        """기본 설정 파일 로드 테스트"""
        config = load_config()
        
        assert isinstance(config, CurriculumConfig)
        assert config.language == "ko"
        assert config.target_exam == "SAA-C03"
        assert config.duration == 30
    
    def test_load_nonexistent_config(self):
        """존재하지 않는 설정 파일 로드 테스트"""
        with pytest.raises(FileNotFoundError):
            load_config("nonexistent.yaml")
    
    def test_config_values(self):
        """설정 값 검증 테스트"""
        config = load_config()
        
        # AWS 설정
        assert config.free_tier_only is True
        assert config.default_instance_type in ["t2.micro", "t3.micro"]
        assert config.ec2_access_method == "ssm-session-manager"
        
        # 개발 도구 설정
        assert config.cicd_tool == "github-actions"
        assert config.container_tool == "docker"
        assert config.notification_tool == "slack"
        
        # CDK 설정
        assert "typescript" in config.cdk_languages
        assert config.default_cdk_language in ["typescript", "python"]
        
        # 약점 영역
        assert "Networking" in config.weak_areas
        assert "Database" in config.weak_areas
