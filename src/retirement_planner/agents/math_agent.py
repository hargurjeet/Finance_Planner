from crewai import Agent
from retirement_planner.config.llm_config import get_llm
from retirement_planner.tools.retirement_calculator import retirement_calculator_tool

def make_math_agent() -> Agent:
    return Agent(
        role="Quantitative Financial Analyst",
        goal=(
            "Perform precise retirement calculations and present a clear, "
            "detailed mathematical summary of the retirement projections."
        ),
        backstory=(
            "You are a quantitative analyst with deep expertise in financial "
            "modelling and retirement mathematics. You translate complex numbers "
            "into clear summaries that anyone can understand, always showing your "
            "workings and highlighting whether someone is on track or has a gap "
            "to bridge."
        ),
        tools=[retirement_calculator_tool],
        llm=get_llm(),
        verbose=True
    )
