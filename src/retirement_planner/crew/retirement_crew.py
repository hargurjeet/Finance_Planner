from crewai import Crew, Process
from retirement_planner.agents.math_agent import make_math_agent
from retirement_planner.agents.planning_agent import make_planning_agent
from retirement_planner.tasks.calculation_task import make_calculation_task
from retirement_planner.tasks.planning_task import make_planning_task
from retirement_planner.schemas.user_input import UserInput

def run_retirement_crew(user_input: UserInput) -> str:
    math_agent    = make_math_agent()
    planning_agent = make_planning_agent()

    calculation_task = make_calculation_task(user_input, math_agent)
    planning_task    = make_planning_task(user_input, planning_agent, context=[calculation_task])

    crew = Crew(
        agents=[math_agent, planning_agent],
        tasks=[calculation_task, planning_task],
        process=Process.sequential,
        verbose=True
    )
    return crew.kickoff()