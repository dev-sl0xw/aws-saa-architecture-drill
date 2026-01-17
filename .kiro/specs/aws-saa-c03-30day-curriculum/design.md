# Design Document: AWS SAA-C03 30일 한국어 커리큘럼 시스템

## Overview

이 시스템은 AWS Solutions Architect Associate (SAA-C03) 자격증 준비를 위한 30일 학습 커리큘럼을 생성하고 관리합니다. 시스템은 두 가지 주요 컴포넌트로 구성됩니다:

1. **Curriculum Generator**: 30일 전체 실러버스와 일별 학습 콘텐츠를 생성
2. **Content Template Engine**: 일관된 형식의 README.md 파일과 실습 자료를 생성

시스템의 핵심 철학은 "Learn by Doing"입니다. 각 일차는 AWS 콘솔에서의 수동 실습(Mental Model 구축)과 AWS CDK를 통한 코드 구현(IaC 숙달)을 결합하여 깊이 있는 학습을 제공합니다.

## Architecture

```mermaid
graph TB
    subgraph "Input Layer"
        A[User Requirements] --> B[Curriculum Planner]
    end
    
    subgraph "Planning Layer"
        B --> C[Syllabus Generator]
        C --> D[30-Day Syllabus]
    end
    
    subgraph "Content Generation Layer"
        D --> E[Daily Content Generator]
        E --> F[Template Engine]
        F --> G[README Generator]
        F --> H[Console Lab Generator]
        F --> I[CDK Lab Generator]
        F --> J[Quiz Generator]
    end
    
    subgraph "Output Layer"
        G --> K[week{n}/day{n}/README.md]
        H --> L[week{n}/day{n}/part1_console/]
        I --> M[week{n}/day{n}/part2_cdk/]
        J --> K
    end
    
    subgraph "Validation Layer"
        K --> N[Content Validator]
        L --> N
        M --> N
        N --> O[Quality Checks]
    end
```

### Architecture Decisions

1. **Template-Based Generation**: 모든 콘텐츠는 일관된 템플릿을 사용하여 생성됩니다. 이는 학습자가 구조에 익숙해지고 콘텐츠에 집중할 수 있게 합니다.

2. **Separation of Concerns**: 콘솔 실습과 CDK 실습을 명확히 분리하여 각각의 학습 목표를 달성합니다.
   - Part 1 (Console): 리소스 간 관계와 AWS 서비스 동작 이해
   - Part 2 (CDK): 인프라 자동화 및 코드로서의 인프라 관리

3. **Progressive Complexity**: Week 1-2는 기초 및 약점 영역에 집중하고, 후반부는 통합 시나리오로 진행합니다.

## Components and Interfaces

### 1. Curriculum Planner

**Purpose**: 사용자 요구사항을 분석하여 30일 학습 계획을 수립합니다.

**Interface**:
```typescript
interface CurriculumPlanner {
  analyzeLearnerProfile(profile: LearnerProfile): WeaknessAnalysis;
  generateLearningPath(analysis: WeaknessAnalysis): LearningPath;
}

interface LearnerProfile {
  strengths: string[];  // e.g., ["Serverless", "CI/CD"]
  weaknesses: string[];  // e.g., ["Networking", "Database"]
  targetExam: string;    // "SAA-C03"
  duration: number;      // 30 days
}

interface WeaknessAnalysis {
  priorityTopics: Topic[];
  recommendedSequence: string[];
}
```

### 2. Syllabus Generator

**Purpose**: 30일 전체 실러버스를 생성합니다.

**Interface**:
```typescript
interface SyllabusGenerator {
  generateSyllabus(learningPath: LearningPath): Syllabus;
}

interface Syllabus {
  weeks: Week[];
  totalDays: number;
  examDomains: ExamDomain[];
}

interface Week {
  weekNumber: number;
  theme: string;
  days: Day[];
}

interface Day {
  dayNumber: number;
  topic: string;
  awsServices: string[];
  learningObjectives: string[];
  prerequisites: string[];
}
```

**Syllabus Structure**:
- **Week 1**: Cloud Operations Foundation & Core Networking
  - Day 1: Cloud Operations Foundation & VPC Basics
  - Day 2: VPC Advanced (Subnets, Route Tables, NAT)
  - Day 3: VPC Security (Security Groups, NACLs)
  - Day 4: VPC Connectivity (VPC Peering, Transit Gateway)
  - Day 5: Hybrid Connectivity (VPN, Direct Connect)
  - Day 6-7: Review & Integration Lab

- **Week 2**: Storage & Database Foundations
  - Day 8: S3 Fundamentals & Storage Classes
  - Day 9: S3 Advanced (Versioning, Lifecycle, Replication)
  - Day 10: EBS & EFS
  - Day 11: RDS Fundamentals
  - Day 12: RDS High Availability (Multi-AZ, Read Replicas)
  - Day 13: Aurora & Database Migration
  - Day 14: Review & Integration Lab

- **Week 3**: Compute & Governance
  - Day 15: EC2 Fundamentals & Instance Types
  - Day 16: EC2 Advanced (Auto Scaling, Load Balancing)
  - Day 17: Lambda & Serverless Patterns
  - Day 18: Container Services (ECS, EKS)
  - Day 19: AWS Config & Compliance
  - Day 20: Cost Management & Tagging Strategy
  - Day 21: Review & Integration Lab

- **Week 4**: Integration & Advanced Scenarios
  - Day 22: CloudFormation & IaC Best Practices
  - Day 23: Monitoring & Logging (CloudWatch, CloudTrail)
  - Day 24: Security & IAM Deep Dive
  - Day 25: Disaster Recovery Strategies
  - Day 26: Multi-Region Architecture
  - Day 27: Serverless Application Integration
  - Day 28: Final Integration Project (Part 1)
  - Day 29: Final Integration Project (Part 2)
  - Day 30: Review & Exam Preparation

### 3. Daily Content Generator

**Purpose**: 각 일차별 상세 콘텐츠를 생성합니다.

**Interface**:
```typescript
interface DailyContentGenerator {
  generateDailyContent(day: Day): DailyContent;
}

interface DailyContent {
  readme: ReadmeContent;
  consoleLab: ConsoleLabContent;
  cdkLab: CdkLabContent;
  quiz: QuizContent;
}
```

### 4. Template Engine

**Purpose**: 일관된 형식의 콘텐츠를 생성하기 위한 템플릿 엔진입니다.

**Interface**:
```typescript
interface TemplateEngine {
  renderReadme(content: ReadmeContent): string;
  renderConsoleLab(content: ConsoleLabContent): string;
  renderCdkLab(content: CdkLabContent): string;
  renderQuiz(content: QuizContent): string;
}
```

### 5. README Generator

**Purpose**: 통합 가이드 README.md 파일을 생성합니다.

**Interface**:
```typescript
interface ReadmeGenerator {
  generateOverview(day: Day): OverviewSection;
  generateScenario(day: Day): ScenarioSection;
  generateArchitectureDiagram(day: Day): MermaidDiagram;
  generateKeyConcepts(day: Day): KeyConceptsSection;
  generateHandsOnGuide(day: Day): HandsOnSection;
  generateVerification(day: Day): VerificationSection;
}

interface OverviewSection {
  title: string;
  description: string;
  learningObjectives: string[];
}

interface ScenarioSection {
  context: string;
  businessRequirements: string[];
  technicalChallenges: string[];
}

interface KeyConceptsSection {
  concepts: Concept[];
}

interface Concept {
  name: string;
  what: string;           // 정의
  why: string;            // 시나리오에서 필요한 이유
  configRationale: string; // 설정값 선택 이유
  officialDocs: string[]; // AWS 공식 문서 URL
}
```

### 6. Console Lab Generator

**Purpose**: AWS 콘솔 실습 가이드를 생성합니다.

**Interface**:
```typescript
interface ConsoleLabGenerator {
  generateObjectives(day: Day): string[];
  generateProcedures(day: Day): Procedure[];
  generateCleanupSteps(day: Day): CleanupStep[];
}

interface Procedure {
  stepNumber: number;
  title: string;
  instructions: string[];
  screenshots: string[];  // 스크린샷 파일명 또는 상세 설명
  expectedOutcome: string;
  troubleshooting: string[];
}

interface CleanupStep {
  stepNumber: number;
  resourceType: string;
  deletionOrder: number;
  instructions: string[];
  verification: string;
}
```

**Console Lab Principles**:
- SSM Session Manager를 사용한 EC2 접속 (SSH 대신)
- 리소스 간 연결 관계 시각화 및 이해
- 수동 작업을 통한 AWS 서비스 동작 원리 파악
- Part 2 진행 전 완벽한 리소스 삭제

### 7. CDK Lab Generator

**Purpose**: AWS CDK 실습 가이드 및 코드를 생성합니다.

**Interface**:
```typescript
interface CdkLabGenerator {
  generateCdkStack(day: Day, language: CdkLanguage): CdkStackCode;
  generateCiCdPipeline(day: Day): GitHubActionsWorkflow;
  generateTests(day: Day): TestCode;
}

interface CdkStackCode {
  language: "typescript" | "python";
  stackCode: string;
  constructCode: string[];
  configCode: string;
}

interface GitHubActionsWorkflow {
  workflowYaml: string;
  dockerfileContent: string;
  slackIntegration: SlackConfig;
}

interface TestCode {
  unitTests: string;
  integrationTests: string;
  cdkAssertions: string;
}
```

**CDK Lab Principles**:
- TypeScript 또는 Python 사용
- Free Tier 준수 (t2.micro/t3.micro)
- VS Code Remote SSH 지원 (Security Group Port 22 + Key Pair)
- Perfect Cleanup (removalPolicy: DESTROY, autoDeleteObjects: true)
- GitHub Actions + Docker + Slack 통합
- AWS CDK API Reference 문서 링크 포함

### 8. Quiz Generator

**Purpose**: 일별 5문제 퀴즈를 생성합니다.

**Interface**:
```typescript
interface QuizGenerator {
  generateQuiz(day: Day): Quiz;
}

interface Quiz {
  questions: Question[];
}

interface Question {
  questionNumber: number;
  questionText: string;
  options: string[];      // 4개의 선택지
  correctAnswer: string;  // A, B, C, D
  explanation: string;    // 상세 해설
  relatedConcept: string; // 관련 개념
}
```

### 9. Content Validator

**Purpose**: 생성된 콘텐츠의 품질을 검증합니다.

**Interface**:
```typescript
interface ContentValidator {
  validateReadme(readme: string): ValidationResult;
  validateConsoleLabCleanup(lab: ConsoleLabContent): ValidationResult;
  validateCdkCleanup(cdk: CdkLabContent): ValidationResult;
  validateQuiz(quiz: Quiz): ValidationResult;
  validateKoreanLanguage(content: string): ValidationResult;
}

interface ValidationResult {
  isValid: boolean;
  errors: ValidationError[];
  warnings: ValidationWarning[];
}

interface ValidationError {
  field: string;
  message: string;
  severity: "error" | "warning";
}
```

**Validation Rules**:
- 모든 콘텐츠가 한국어로 작성되었는지 확인
- README.md에 필수 섹션이 모두 포함되었는지 확인
- Console Lab에 cleanup 단계가 포함되었는지 확인
- CDK Lab에 removalPolicy와 autoDeleteObjects가 설정되었는지 확인
- Quiz가 정확히 5문제이며 정답과 해설이 포함되었는지 확인
- AWS 공식 문서 URL이 유효한지 확인

## Data Models

### Syllabus Data Model

```typescript
interface Syllabus {
  metadata: {
    version: string;
    createdAt: Date;
    targetExam: string;
    totalDays: number;
  };
  weeks: Week[];
}

interface Week {
  weekNumber: number;
  theme: string;
  description: string;
  days: DayOverview[];
}

interface DayOverview {
  dayNumber: number;
  globalDayNumber: number;  // 1-30
  topic: string;
  awsServices: string[];
  difficulty: "beginner" | "intermediate" | "advanced";
  estimatedHours: number;
}
```

### Daily Content Data Model

```typescript
interface DailyContent {
  metadata: {
    dayNumber: number;
    weekNumber: number;
    topic: string;
    createdAt: Date;
  };
  overview: {
    description: string;
    learningObjectives: string[];
    prerequisites: string[];
  };
  scenario: {
    context: string;
    businessRequirements: string[];
    technicalChallenges: string[];
  };
  architectureDiagram: string;  // Mermaid.js syntax
  keyConcepts: Concept[];
  consoleLab: ConsoleLabContent;
  cdkLab: CdkLabContent;
  verification: VerificationContent;
  quiz: Quiz;
}

interface ConsoleLabContent {
  objectives: string[];
  procedures: Procedure[];
  cleanupSteps: CleanupStep[];
  estimatedTime: number;  // minutes
}

interface CdkLabContent {
  language: "typescript" | "python";
  environment: {
    instanceType: string;
    securityGroupRules: SecurityGroupRule[];
    keyPairName: string;
  };
  stackCode: string;
  cicdPipeline: {
    githubActionsWorkflow: string;
    dockerfile: string;
    slackWebhook: string;
  };
  tests: {
    unitTests: string;
    integrationTests: string;
    cdkAssertions: string;
  };
  cleanupConfig: {
    removalPolicy: string;
    autoDeleteObjects: boolean;
  };
  estimatedTime: number;  // minutes
}

interface VerificationContent {
  objectives: string[];
  testCases: TestCase[];
  tools: string[];  // ["pytest", "boto3", "moto", "CDK Assertions"]
}

interface TestCase {
  name: string;
  description: string;
  testCode: string;
  expectedResult: string;
}
```

### Configuration Data Model

```typescript
interface CurriculumConfig {
  language: "ko";
  targetExam: "SAA-C03";
  duration: 30;
  freeTierOnly: true;
  cicdTool: "github-actions";
  containerTool: "docker";
  notificationTool: "slack";
  ec2AccessMethod: "ssm-session-manager";
  cdkLanguages: ["typescript", "python"];
  defaultInstanceType: "t2.micro" | "t3.micro";
}
```

## Error Handling

### Error Categories

1. **Content Generation Errors**
   - Missing required sections in README
   - Invalid Mermaid diagram syntax
   - Incomplete cleanup instructions

2. **Validation Errors**
   - Non-Korean content detected
   - Missing AWS documentation URLs
   - Invalid CDK code syntax
   - Missing removalPolicy or autoDeleteObjects

3. **Configuration Errors**
   - Invalid instance type (not Free Tier)
   - Missing Security Group rules for SSH
   - Invalid GitHub Actions workflow syntax

### Error Handling Strategy

```typescript
class ContentGenerationError extends Error {
  constructor(
    public day: number,
    public section: string,
    public details: string
  ) {
    super(`Day ${day} - ${section}: ${details}`);
  }
}

class ValidationError extends Error {
  constructor(
    public validationType: string,
    public failures: ValidationFailure[]
  ) {
    super(`Validation failed: ${validationType}`);
  }
}

interface ErrorHandler {
  handleGenerationError(error: ContentGenerationError): void;
  handleValidationError(error: ValidationError): void;
  logError(error: Error): void;
  retryGeneration(day: Day, maxRetries: number): DailyContent;
}
```

**Error Recovery**:
- 콘텐츠 생성 실패 시 템플릿 기본값 사용
- 검증 실패 시 경고 로그 출력 및 수동 수정 요청
- 3회 재시도 후 실패 시 사용자에게 알림

## Testing Strategy

### Unit Tests

각 컴포넌트의 개별 기능을 테스트합니다:

1. **Syllabus Generator Tests**
   - 30일 실러버스가 올바르게 생성되는지 확인
   - Week 1-2에 약점 영역이 우선 배치되는지 확인
   - 모든 SAA-C03 exam domain이 포함되는지 확인

2. **Template Engine Tests**
   - README 템플릿이 모든 필수 섹션을 포함하는지 확인
   - Mermaid 다이어그램 구문이 유효한지 확인
   - 한국어 콘텐츠가 올바르게 렌더링되는지 확인

3. **Console Lab Generator Tests**
   - SSM Session Manager 접속 가이드가 포함되는지 확인
   - Cleanup 단계가 올바른 순서로 생성되는지 확인
   - 모든 리소스 삭제 검증 단계가 포함되는지 확인

4. **CDK Lab Generator Tests**
   - Free Tier 인스턴스 타입이 사용되는지 확인
   - removalPolicy: DESTROY가 설정되는지 확인
   - autoDeleteObjects: true가 S3 버킷에 설정되는지 확인
   - Security Group에 Port 22가 포함되는지 확인

5. **Quiz Generator Tests**
   - 정확히 5문제가 생성되는지 확인
   - 모든 문제에 정답과 해설이 포함되는지 확인
   - 한국어로 작성되는지 확인

6. **Content Validator Tests**
   - 영어 콘텐츠를 감지하는지 확인
   - 필수 섹션 누락을 감지하는지 확인
   - 잘못된 cleanup 설정을 감지하는지 확인

### Property-Based Tests

이 시스템은 주로 콘텐츠 생성 시스템이므로, property-based testing은 제한적으로 적용됩니다. 대신 다음과 같은 invariant를 검증합니다:

**Testing Tools**:
- Unit tests: pytest (Python) 또는 Jest (TypeScript)
- Mocking: moto (AWS services)
- CDK testing: AWS CDK Assertions
- Integration tests: boto3 + actual AWS resources (cleanup 필수)

**Test Configuration**:
- 모든 테스트는 한국어 주석 포함
- CDK 테스트는 실제 배포 없이 synthesize만 수행
- Integration 테스트는 Free Tier 리소스만 사용
- 테스트 후 자동 cleanup 보장

**Test Coverage Goals**:
- Unit test coverage: 80% 이상
- 모든 CDK 스택에 대한 snapshot 테스트
- 모든 cleanup 로직에 대한 검증 테스트
- 모든 validation rule에 대한 테스트


## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property Reflection

After analyzing all acceptance criteria, I identified several areas of redundancy:

1. **Language validation** (1.5, 8.5) can be consolidated into a single comprehensive property
2. **Cleanup completeness** (3.5, 6.2, 6.4, 6.5) can be combined into one property about resource coverage
3. **Directory structure** (9.1, 9.2, 9.3, 9.4, 9.5) can be consolidated into a single property about file system structure
4. **Section presence** (2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7) can be combined into one property about README completeness
5. **CDK cleanup configuration** (4.4, 6.3) are testing the same thing and can be merged

The following properties represent the unique, non-redundant validation requirements:

### Property 1: Complete Syllabus Coverage

*For any* generated syllabus, it should contain exactly 30 days of content and cover all AWS SAA-C03 exam domains (Compute, Storage, Database, Networking, Security, Cost Optimization, Monitoring, High Availability).

**Validates: Requirements 1.1, 10.1**

### Property 2: Weak Area Prioritization

*For any* generated curriculum, topics from weak areas (Networking, Database, Storage, Governance) should appear within the first 14 days (weeks 1-2).

**Validates: Requirements 1.2**

### Property 3: Integration Scenario Sequencing

*For any* generated curriculum, topics labeled as "integration" or "advanced scenarios" should appear after day 21.

**Validates: Requirements 1.3, 10.5**

### Property 4: Directory Structure Consistency

*For any* generated curriculum, all content directories should follow the pattern `week{n}/day{n}/` and each day directory should contain `README.md`, `part1_console/`, and `part2_cdk/` subdirectories.

**Validates: Requirements 1.4, 9.1, 9.2, 9.3, 9.4, 9.5**

### Property 5: Korean Language Completeness

*For any* generated content (README, quiz, lab instructions), all text should be written in Korean language, with the exception of code blocks, URLs, and technical identifiers.

**Validates: Requirements 1.5, 8.5**

### Property 6: README Section Completeness

*For any* generated daily README.md file, it should contain all required sections: Overview with scenario, Architecture Diagram (Mermaid.js), Key Concepts (What/Why/Docs), Hands-on Part 1 (Console), Hands-on Part 2 (CDK), Verification, and Daily Quiz.

**Validates: Requirements 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7**

### Property 7: AWS Documentation References

*For any* generated Key Concepts section, each concept should include at least one valid AWS official documentation URL (docs.aws.amazon.com or AWS CDK API reference).

**Validates: Requirements 2.8, 4.9**

### Property 8: Console Lab SSM Access

*For any* generated Console Lab content, EC2 access instructions should mention SSM Session Manager and should not include SSH connection instructions for EC2 instances.

**Validates: Requirements 3.2**

### Property 9: Console Lab Cleanup Completeness

*For any* generated Console Lab, the cleanup section should include deletion instructions for every resource type that was created in the procedures section.

**Validates: Requirements 3.4, 3.5, 6.2, 6.4, 6.5**

### Property 10: CDK Free Tier Compliance

*For any* generated CDK code that creates EC2 instances, the instance type should be either `t2.micro` or `t3.micro`.

**Validates: Requirements 4.2**

### Property 11: CDK SSH Access Configuration

*For any* generated CDK code, if it creates EC2 instances, it should include Security Group rules allowing inbound traffic on port 22 and should create or reference a key pair.

**Validates: Requirements 4.3**

### Property 12: CDK Perfect Cleanup Configuration

*For any* generated CDK code, resources that persist data (S3 buckets, DynamoDB tables, RDS instances) should have `removalPolicy: RemovalPolicy.DESTROY` configured, and S3 buckets should have `autoDeleteObjects: true`.

**Validates: Requirements 4.4, 6.3**

### Property 13: CI/CD Tool Selection

*For any* generated CDK Lab content, CI/CD configuration should use GitHub Actions (not AWS CodePipeline), include Docker configuration, and include Slack notification setup.

**Validates: Requirements 4.5, 4.6, 4.7**

### Property 14: CDK Code Syntax Validity

*For any* generated CDK code blocks, the code should be syntactically valid TypeScript or Python and should use proper CDK construct patterns.

**Validates: Requirements 4.1, 4.8**

### Property 15: Governance Topic Coverage

*For any* generated 30-day curriculum, at least one day should cover AWS Config, at least one day should cover tagging strategy with cost allocation tags, and at least one day should cover cost monitoring.

**Validates: Requirements 5.1, 5.2, 5.4**

### Property 16: CDK Tagging Implementation

*For any* generated CDK stack code, it should include tag configuration using `Tags.of(stack).add()` or equivalent tagging mechanism.

**Validates: Requirements 5.3**

### Property 17: Resilience Pattern Inclusion

*For any* generated architecture diagram or description, if it includes compute or database resources, it should mention at least one resilience pattern (multi-AZ, auto-scaling, backup, or replication).

**Validates: Requirements 6.1**

### Property 18: Test Framework Usage

*For any* generated Verification section, Python test code should use pytest, should import boto3 for AWS interactions, should use moto for mocking, and CDK tests should use CDK Assertions.

**Validates: Requirements 7.1, 7.2, 7.3, 7.4**

### Property 19: Test Coverage Completeness

*For any* generated test code, there should be at least one test case for each major component (resource type) mentioned in the lab procedures.

**Validates: Requirements 7.5, 7.6**

### Property 20: Quiz Structure Compliance

*For any* generated Daily Quiz, it should contain exactly 5 questions, each question should have 4 options (A, B, C, D), one correct answer, and a detailed explanation in Korean.

**Validates: Requirements 8.1, 8.2, 8.3**

### Property 21: Quiz Content Alignment

*For any* generated Daily Quiz, the questions should reference concepts that appear in the Key Concepts section of the same day's content.

**Validates: Requirements 8.4**

## Property Testing Implementation Notes

Since this is a content generation system, property-based testing will focus on validating the structure and completeness of generated content rather than testing algorithmic correctness. The properties above will be implemented as:

1. **Structure validation properties**: Check that generated files and directories match expected patterns
2. **Content validation properties**: Check that generated text contains required sections and keywords
3. **Configuration validation properties**: Check that generated code includes required settings
4. **Reference validation properties**: Check that URLs and links are valid and accessible

Each property will be tested by:
1. Generating sample content for a specific day
2. Parsing the generated content (README, code files, directory structure)
3. Asserting that the property holds for the generated content
4. Running tests with multiple different day configurations to ensure properties hold universally
