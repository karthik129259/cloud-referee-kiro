# Cloud Referee

A command-line tool that compares AWS Bedrock and OpenAI API based on user constraints, providing trade-off analysis instead of a single recommendation.

## Problem Statement

Developers frequently face challenges when selecting AI platforms:
- Most recommendations are one-sided without context
- Trade-offs between services are not clearly explained
- Decision criteria vary based on project requirements

## Solution

Cloud Referee takes user-defined constraints and generates a balanced comparison:
- Analyzes both options objectively
- Lists pros and cons for each service
- Provides conditional recommendations based on specific use cases

## Architecture Flowchart

```mermaid
flowchart TD
    A[User Starts Application] --> B[app.py]
    B --> C{Input Constraints}
    
    C --> D[Budget: low/medium/high]
    C --> E[Data Privacy: low/high]
    C --> F[Scalability: low/high]
    C --> G[Vendor Lock-in: low/high]
    
    D --> H[CloudReferee.compare]
    E --> H
    F --> H
    G --> H
    
    H --> I[referee.py]
    
    I --> J{Analyze Each Constraint}
    
    J --> K[Data Privacy Analysis]
    J --> L[Budget Analysis]
    J --> M[Scalability Analysis]
    J --> N[Vendor Lock-in Analysis]
    
    K --> O[Generate AWS Bedrock Pros/Cons]
    L --> O
    M --> O
    N --> O
    
    K --> P[Generate OpenAI API Pros/Cons]
    L --> P
    M --> P
    N --> P
    
    O --> Q[Build Conditional Verdict]
    P --> Q
    
    Q --> R[Output Results]
    
    R --> S[AWS Bedrock: Pros and Cons]
    R --> T[OpenAI API: Pros and Cons]
    R --> U[Conditional Recommendation]
```

## Decision Logic Flowchart

```mermaid
flowchart LR
    subgraph Input
        A1[Budget]
        A2[Data Privacy]
        A3[Scalability]
        A4[Vendor Lock-in]
    end
    
    subgraph Analysis
        B1{Privacy = High?}
        B2{Budget = Low?}
        B3{Scalability = High?}
        B4{Lock-in = Low?}
    end
    
    subgraph AWS Bedrock Factors
        C1[VPC Integration]
        C2[Enterprise Pricing]
        C3[Auto-scaling]
        C4[Multi-model Access]
    end
    
    subgraph OpenAI API Factors
        D1[Simple Integration]
        D2[Pay-per-token]
        D3[Standard REST API]
        D4[GPT-4 Access]
    end
    
    A2 --> B1
    A1 --> B2
    A3 --> B3
    A4 --> B4
    
    B1 -->|Yes| C1
    B1 -->|No| D1
    B2 -->|Yes| D2
    B2 -->|No| C2
    B3 -->|Yes| C3
    B3 -->|No| D1
    B4 -->|Yes| D3
    B4 -->|No| C4
```

## Component Diagram

```mermaid
flowchart TB
    subgraph Application Layer
        APP[app.py<br>Entry Point]
    end
    
    subgraph Core Logic
        REF[referee.py<br>CloudReferee Class]
        COMP[compare method]
        VERD[_build_verdict method]
    end
    
    subgraph Data Layer
        PROMPT[prompts/referee_prompt.txt]
        SERVICES[Service Definitions]
    end
    
    subgraph Output
        PROS[Pros List]
        CONS[Cons List]
        VERDICT[Conditional Verdict]
    end
    
    APP --> REF
    REF --> COMP
    COMP --> VERD
    REF --> SERVICES
    REF --> PROMPT
    COMP --> PROS
    COMP --> CONS
    VERD --> VERDICT
```

## Features

- Constraint-based comparison (budget, data privacy, scalability, vendor lock-in)
- Structured pros/cons output for both AWS Bedrock and OpenAI API
- Conditional verdict system (no absolute "best" answer)
- CLI interface for quick evaluation

## Project Structure

```
cloud-referee-kiro/
├── app.py                      # Main application entry point
├── referee.py                  # Core comparison logic
├── prompts/
│   └── referee_prompt.txt      # Referee prompt template
├── .kiro/                      # Kiro configuration
└── README.md
```

## Installation

```bash
git clone https://github.com/karthik129259/cloud-referee-kiro.git
cd cloud-referee-kiro
```

## Usage

```bash
python app.py
```

The application will prompt for the following constraints:
- Budget: low / medium / high
- Data Privacy: low / high
- Scalability: low / high
- Vendor Lock-in Tolerance: low / high

## Example Output

```
============================================================
CLOUD REFEREE - AWS Bedrock vs OpenAI API
============================================================

Enter your constraints to get a personalized comparison:

Budget (low/medium/high): medium
Data Privacy requirement (low/high): high
Scalability needs (low/high): high
Vendor lock-in tolerance (low/high): low

============================================================
COMPARISON RESULTS
============================================================

AWS BEDROCK
  Pros:
     - Data stays within AWS infrastructure - better for compliance
     - VPC integration for isolated environments
     - Flexible pricing with multiple model options
     - Seamless scaling with AWS infrastructure
     - Auto-scaling and load balancing built-in
     - Access to multiple AI models (Claude, Llama, Titan, etc.)
     - Native AWS service integration (Lambda, S3, etc.)
  Cons:
     - Tighter AWS ecosystem integration may increase dependency

OPENAI API
  Pros:
     - Transparent token-based pricing
     - Easier to switch - standard REST API
     - Model-agnostic integration possible
     - Access to GPT-4 and latest OpenAI models
     - Extensive documentation and community support
     - Rapid model updates and improvements
  Cons:
     - Data sent to external OpenAI servers
     - Rate limits may require enterprise plan

============================================================
VERDICT (Trade-off Based)
============================================================

Choose AWS BEDROCK if:
   - You need high data privacy and compliance (HIPAA, SOC2)
   - You are already in the AWS ecosystem
   - You need access to multiple AI models (Claude, Llama, Titan)
   - You require enterprise-grade scaling

Choose OPENAI API if:
   - You want fastest access to cutting-edge GPT models
   - You prefer simple setup and integration
   - You are building prototypes or MVPs quickly
   - You want strong community support and resources

Based on your HIGH data privacy requirement:
   AWS Bedrock is strongly recommended
```

## How It Works

1. User inputs constraints via CLI
2. `CloudReferee` class evaluates constraints against service characteristics
3. Pros and cons are dynamically generated based on input
4. Conditional verdict provides context-aware recommendations

## Technical Details

- Language: Python 3
- Dependencies: None (standard library only)
- Architecture: Modular design with separate referee logic

## Comparison Criteria

| Constraint | AWS Bedrock Advantage | OpenAI API Advantage |
|------------|----------------------|---------------------|
| High Data Privacy | Data stays in AWS VPC | - |
| Low Budget | - | Predictable per-token pricing |
| High Scalability | Native AWS auto-scaling | - |
| Low Vendor Lock-in | - | Standard REST API |

## AI for Bharat - Kiro Week 6 Challenge

This project was developed for the Kiro Week 6: The Referee challenge.

Challenge objective: Build a tool that compares options and explains trade-offs, helping users make informed decisions rather than providing single-answer recommendations.

## Development

Built using Kiro for:
- Prompt engineering and refinement
- Code structure generation
- Logic optimization

## License

MIT
