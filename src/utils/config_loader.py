"""
설정 파일 로더

config.yaml 파일을 읽어 CurriculumConfig 객체로 변환합니다.
"""

import yaml
from pathlib import Path
from typing import Optional

from ..models.config import CurriculumConfig


def load_config(config_path: Optional[str] = None) -> CurriculumConfig:
    """
    설정 파일을 로드합니다.
    
    Args:
        config_path: 설정 파일 경로 (기본값: config.yaml)
    
    Returns:
        CurriculumConfig 객체
    
    Raises:
        FileNotFoundError: 설정 파일이 없는 경우
        ValueError: 설정 파일 형식이 잘못된 경우
    """
    if config_path is None:
        config_path = "config.yaml"
    
    config_file = Path(config_path)
    
    if not config_file.exists():
        raise FileNotFoundError(f"설정 파일을 찾을 수 없습니다: {config_path}")
    
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            config_data = yaml.safe_load(f)
        
        return CurriculumConfig(**config_data)
    
    except yaml.YAMLError as e:
        raise ValueError(f"설정 파일 파싱 오류: {e}")
    except Exception as e:
        raise ValueError(f"설정 파일 로드 오류: {e}")
