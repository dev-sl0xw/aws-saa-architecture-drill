# Requirements Document

## Introduction

AWS Solutions Architect Associate (SAA-C03) 자격증 범위의 인프라 지식을 밑바닥부터 체계적으로 학습하기 위한 30일 커리큘럼 시스템입니다. 이 시스템은 AWS 콘솔 실습과 AWS CDK 코드 구현을 통해 실무 중심의 학습 경험을 제공합니다.

## Glossary

- **Curriculum_System**: 30일 학습 커리큘럼을 생성하고 관리하는 시스템
- **Daily_Content**: 각 일차별 학습 콘텐츠 (README.md 및 실습 자료)
- **Console_Lab**: AWS 콘솔을 통한 수동 실습 파트
- **CDK_Lab**: AWS CDK를 사용한 IaC 구현 파트
- **Syllabus**: 30일 전체 학습 계획 및 주제 구성
- **Verification_Test**: 각 일차별 학습 검증을 위한 자동화 테스트
- **Cleanup_Guide**: 리소스 삭제 및 비용 방지를 위한 정리 가이드
- **Quiz**: 각 일차별 5문제 퀴즈 (정답 및 해설 포함)

## Requirements

### Requirement 1: 30일 커리큘럼 구조 생성

**User Story:** As a learner, I want a 30-day structured curriculum, so that I can systematically learn AWS SAA-C03 topics from foundation to advanced integration.

#### Acceptance Criteria

1. THE Curriculum_System SHALL generate a complete 30-day syllabus covering all AWS SAA-C03 exam domains
2. WHEN organizing the curriculum, THE Curriculum_System SHALL prioritize weak areas (Networking, Database, Storage, Governance) in weeks 1-2
3. WHEN organizing the curriculum, THE Curriculum_System SHALL place integration scenarios in the later weeks
4. THE Curriculum_System SHALL structure content in week/day hierarchy with consistent directory naming
5. THE Curriculum_System SHALL ensure all content is written in Korean language

### Requirement 2: 일별 콘텐츠 생성

**User Story:** As a learner, I want comprehensive daily content with theory and hands-on labs, so that I can understand concepts deeply and practice implementation.

#### Acceptance Criteria

1. WHEN generating daily content, THE Curriculum_System SHALL create a README.md file containing all required sections
2. THE Daily_Content SHALL include an Overview section with a real-world scenario
3. THE Daily_Content SHALL include an Architecture Diagram using Mermaid.js syntax
4. THE Daily_Content SHALL include a Key Concepts section with What, Why (Context), and Official Docs subsections
5. THE Daily_Content SHALL include separate Hands-on sections for Console (Part 1) and CDK (Part 2)
6. THE Daily_Content SHALL include a Verification section with test specifications
7. THE Daily_Content SHALL include a Daily Quiz section with exactly 5 questions, answers, and explanations
8. THE Daily_Content SHALL reference official AWS documentation URLs for each concept

### Requirement 3: 콘솔 실습 가이드 (Part 1)

**User Story:** As a learner, I want step-by-step console instructions, so that I can understand resource relationships and AWS service interactions through manual operations.

#### Acceptance Criteria

1. THE Console_Lab SHALL provide clear objectives focused on understanding resource connections
2. THE Console_Lab SHALL use SSM Session Manager for EC2 access instead of SSH
3. THE Console_Lab SHALL include step-by-step procedures with screenshots or detailed descriptions
4. THE Console_Lab SHALL include a cleanup section with manual resource deletion instructions
5. WHEN cleanup instructions are provided, THE Console_Lab SHALL ensure all resources are deleted before proceeding to Part 2

### Requirement 4: CDK 실습 가이드 (Part 2)

**User Story:** As a developer, I want to implement infrastructure as code using AWS CDK, so that I can automate and version control my infrastructure.

#### Acceptance Criteria

1. THE CDK_Lab SHALL use TypeScript or Python as the implementation language
2. THE CDK_Lab SHALL configure EC2 instances with t2.micro or t3.micro instance types for Free Tier compliance
3. THE CDK_Lab SHALL enable VS Code Remote SSH access by configuring Security Groups to allow port 22 and creating key pairs
4. THE CDK_Lab SHALL implement perfect cleanup with removalPolicy: DESTROY and autoDeleteObjects: true
5. THE CDK_Lab SHALL integrate GitHub Actions for CI/CD instead of AWS CodePipeline
6. THE CDK_Lab SHALL integrate Docker for build processes
7. THE CDK_Lab SHALL integrate Slack notifications for deployment status
8. THE CDK_Lab SHALL include CDK code examples with proper TypeScript/Python syntax
9. THE CDK_Lab SHALL reference AWS CDK API documentation URLs

### Requirement 5: 거버넌스 및 비용 관리

**User Story:** As a cloud administrator, I want governance and cost management practices, so that I can maintain compliance and control costs.

#### Acceptance Criteria

1. THE Curriculum_System SHALL include AWS Config setup and usage in the curriculum
2. THE Curriculum_System SHALL include a tagging strategy with cost allocation tags
3. THE Curriculum_System SHALL ensure all CDK stacks implement proper tagging
4. THE Curriculum_System SHALL include cost monitoring and alerting practices
5. THE Curriculum_System SHALL follow Cloud Operations on AWS Day 1 principles

### Requirement 6: 복원력 및 완벽한 정리

**User Story:** As a learner, I want resilient architectures and complete cleanup procedures, so that I can learn best practices and avoid unexpected costs.

#### Acceptance Criteria

1. WHEN designing architectures, THE Curriculum_System SHALL include resilience patterns (multi-AZ, auto-scaling, backup)
2. THE Cleanup_Guide SHALL provide complete resource deletion instructions for console operations
3. THE Cleanup_Guide SHALL ensure CDK stacks are configured for automatic resource deletion
4. THE Cleanup_Guide SHALL verify all resources are deleted to prevent cost accumulation
5. THE Cleanup_Guide SHALL include verification steps to confirm successful cleanup

### Requirement 7: 검증 및 테스트

**User Story:** As a learner, I want automated tests to verify my implementations, so that I can confirm my understanding and catch errors early.

#### Acceptance Criteria

1. THE Verification_Test SHALL use pytest for Python-based tests
2. THE Verification_Test SHALL use boto3 for AWS API interactions
3. THE Verification_Test SHALL use moto for AWS service mocking
4. THE Verification_Test SHALL use AWS CDK Assertions for infrastructure testing
5. THE Verification_Test SHALL include test cases for each major component in the daily lab
6. THE Verification_Test SHALL provide clear pass/fail criteria

### Requirement 8: 일별 퀴즈

**User Story:** As a learner, I want daily quizzes to test my knowledge, so that I can reinforce learning and identify gaps.

#### Acceptance Criteria

1. THE Quiz SHALL contain exactly 5 multiple-choice questions per day
2. THE Quiz SHALL include correct answers for all questions
3. THE Quiz SHALL include detailed explanations for each answer
4. THE Quiz SHALL cover key concepts from that day's content
5. THE Quiz SHALL be written in Korean language

### Requirement 9: 디렉토리 구조 및 파일 조직

**User Story:** As a learner, I want a consistent directory structure, so that I can easily navigate and find content.

#### Acceptance Criteria

1. THE Curriculum_System SHALL create directories following the pattern: week{n}/day{n}/
2. WHEN creating daily directories, THE Curriculum_System SHALL include README.md at the day level
3. WHEN creating daily directories, THE Curriculum_System SHALL include part1_console/ subdirectory
4. WHEN creating daily directories, THE Curriculum_System SHALL include part2_cdk/ subdirectory
5. THE Curriculum_System SHALL maintain consistent naming conventions across all weeks and days

### Requirement 10: 첫 번째 산출물

**User Story:** As a learner, I want to see the complete syllabus and first day's content, so that I can understand the curriculum scope and start learning immediately.

#### Acceptance Criteria

1. THE Curriculum_System SHALL generate a complete 30-day syllabus document
2. THE Curriculum_System SHALL generate complete Week 1 / Day 1 content with topic "Cloud Operations Foundation & VPC"
3. THE Day 1 content SHALL include all required sections: Overview, Architecture Diagram, Key Concepts, Console Lab, CDK Lab, Verification, and Quiz
4. THE Day 1 content SHALL demonstrate the template and quality standard for all subsequent days
5. THE syllabus SHALL show clear progression from foundational topics to integration scenarios
