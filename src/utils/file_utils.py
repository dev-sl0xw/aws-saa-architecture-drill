"""
파일 유틸리티

파일 및 디렉토리 작업을 위한 헬퍼 함수들입니다.
"""

from pathlib import Path
from typing import Optional


def ensure_directory(directory: str) -> Path:
    """
    디렉토리가 존재하는지 확인하고, 없으면 생성합니다.
    
    Args:
        directory: 디렉토리 경로
    
    Returns:
        Path 객체
    """
    dir_path = Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def write_file(file_path: str, content: str, encoding: str = "utf-8") -> None:
    """
    파일에 내용을 씁니다.
    
    Args:
        file_path: 파일 경로
        content: 파일 내용
        encoding: 인코딩 (기본값: utf-8)
    """
    path = Path(file_path)
    ensure_directory(str(path.parent))
    
    with open(path, "w", encoding=encoding) as f:
        f.write(content)


def read_file(file_path: str, encoding: str = "utf-8") -> str:
    """
    파일 내용을 읽습니다.
    
    Args:
        file_path: 파일 경로
        encoding: 인코딩 (기본값: utf-8)
    
    Returns:
        파일 내용
    
    Raises:
        FileNotFoundError: 파일이 없는 경우
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")
    
    with open(path, "r", encoding=encoding) as f:
        return f.read()
