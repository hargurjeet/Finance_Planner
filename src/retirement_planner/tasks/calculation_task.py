from crewai import Task, Agent
from retirement_planner.schemas.user_input import UserInput

def make_calculation_task(user_input: UserInput, agent: Agent) -> Task:
    return Task(
        description=(
            f"Perform a full retirement calculation for the following person:\n\n"
            f"  Name                   : {user_input.name}\n"
            f"  Age                    : {user_input.age}\n"
            f"  Current Monthly Income : £{user_input.current_monthly_income}\n"
            f"  Current Monthly Savings: £{user_input.current_monthly_savings}\n"
            f"  Target Monthly Income  : £{user_input.target_monthly_income} (at age 60)\n\n"
            f"Use the Retirement Calculator tool with these exact values. "
            f"Present a clearly formatted mathematical summary including:\n"
            f"  - Years to retirement\n"
            f"  - Required retirement corpus\n"
            f"  - Projected corpus from current savings\n"
            f"  - Corpus gap (if any)\n"
            f"  - Required vs current monthly savings\n"
            f"  - Whether they are currently on track\n"
            f"  - Inflation-adjusted target income at retirement\n"
        ),
        expected_output=(
            "A detailed mathematical summary with all retirement figures clearly "
            "labelled, including whether the person is on track and the savings "
            "gap or surplus."
        ),
        agent=agent
    )
