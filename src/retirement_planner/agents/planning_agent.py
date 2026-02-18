from crewai import Agent
from retirement_planner.config.llm_config import get_llm
from retirement_planner.tools.investment_breakdown import investment_breakdown_tool

def make_planning_agent() -> Agent:
    return Agent(
        role="Retirement Planning Strategist",
        goal=(
            "Create a comprehensive, personalised retirement plan based on the "
            "individual's financial profile, lifestyle goals, and risk appetite."
        ),
        backstory=(
            "You are a seasoned financial planner with 20 years of experience "
            "helping individuals across all income brackets achieve financial "
            "independence. You specialise in long-term retirement strategies, "
            "asset allocation, and helping people understand their financial journey "
            "in simple, actionable terms."
        ),
        tools=[investment_breakdown_tool],
        llm=get_llm(),
        verbose=True
    )
