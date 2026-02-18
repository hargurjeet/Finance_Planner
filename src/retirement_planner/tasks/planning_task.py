from crewai import Task, Agent
from retirement_planner.schemas.user_input import UserInput

def make_planning_task(user_input: UserInput, agent: Agent, context: list) -> Task:
    return Task(
        description=(
            f"Using the mathematical summary from the retirement calculation, "
            f"develop a personalised retirement plan for {user_input.name}, aged {user_input.age}.\n\n"
            f"Their current monthly income is £{user_input.current_monthly_income} "
            f"and they save £{user_input.current_monthly_savings} per month.\n"
            f"Their target monthly income at retirement (age 60) is £{user_input.target_monthly_income}.\n\n"
            f"Use the Investment Breakdown Calculator to suggest an asset allocation. "
            f"Your plan should include:\n"
            f"  1. Executive summary of their retirement readiness\n"
            f"  2. Recommended monthly savings target\n"
            f"  3. Investment allocation strategy (equity vs debt split)\n"
            f"  4. Specific investment instruments to consider\n"
            f"  5. Key milestones to hit (e.g. at age 40, 50, 55)\n"
            f"  6. Risks and assumptions\n"
            f"  7. Actionable next steps\n"
        ),
        expected_output=(
            "A comprehensive, easy-to-read retirement plan with clear sections, "
            "actionable recommendations, and an investment strategy tailored to "
            "the individual's age and income profile."
        ),
        agent=agent,
        context=context
    )
