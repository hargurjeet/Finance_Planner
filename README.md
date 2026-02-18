# Finance Planner

An AI-powered retirement planning tool built with CrewAI and AWS Bedrock.

## Overview

Uses a multi-agent CrewAI system to:
1. Calculate retirement projections (corpus, savings gap, inflation-adjusted income)
2. Generate a personalised retirement plan with investment strategy

## Project Structure

```
src/
├── app/
│   ├── main.py               # Entry point
│   └── test_dummy.py         # CrewAI + Bedrock connectivity test
└── retirement_planner/
    ├── agents/
    │   ├── math_agent.py       # Quantitative Financial Analyst agent
    │   └── planning_agent.py   # Retirement Planning Strategist agent
    ├── config/
    │   ├── llm_config.py       # AWS Bedrock LLM setup
    │   └── setting.py          # App settings (pydantic)
    ├── crew/
    │   └── retirement_crew.py  # CrewAI crew orchestration
    ├── schemas/
    │   └── user_input.py       # User input validation
    ├── tasks/
    │   ├── calculation_task.py # Retirement calculation task
    │   └── planning_task.py    # Retirement planning task
    └── tools/
        ├── retirement_calculator.py  # Calculates corpus, gap, projections
        └── investment_breakdown.py   # Suggests asset allocation
```

## Prerequisites

- Python 3.12+
- AWS credentials configured with Bedrock access (`eu-west-2`)
- Corporate network: SSL certificate bypass required (see below)

## Installation

```bash
pip install crewai litellm botocore httpx pydantic pydantic-settings
```

## Configuration

Settings are managed via `setting.py` or `.env` file:

| Setting | Default | Description |
|---|---|---|
| `region` | `eu-west-2` | AWS region |
| `llm_model_env_var` | `ANTHROPIC_CLAUDE_3_7_SONNET_20250219_V1_0` | Bedrock model env var |
| `temperature` | `0.3` | LLM temperature |
| `retirement_age` | `60` | Target retirement age |
| `annual_return_rate` | `0.07` | Expected annual return |

## Running

```bash
cd src/app
python main.py
```

You will be prompted to enter:
- Name
- Current age
- Current monthly income (£)
- Current monthly savings (£)
- Target monthly income at retirement (£)

## Testing LLM Connectivity

```bash
cd src/app
python test_dummy.py
```

## SSL Certificate Fix (Corporate Network)

If you encounter `[SSL: CERTIFICATE_VERIFY_FAILED]` errors, the following patches are applied in `llm_config.py`:

```python
# Disable SSL for botocore (boto3/AWS SDK)
botocore.httpsession.URLLib3Session.send = patched_send

# Disable SSL for httpx (used by litellm/CrewAI)
httpx.Client.__init__ = patched_init
```

Also set `OTEL_SDK_DISABLED=true` to disable CrewAI telemetry which also triggers SSL errors.

## Agents

- **Quantitative Financial Analyst** - Uses `retirement_calculator` tool to compute projections
- **Retirement Planning Strategist** - Uses `investment_breakdown` tool to suggest asset allocation

## License

See [LICENSE](LICENSE)
