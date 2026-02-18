import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from crewai import Agent, Task, Crew
from retirement_planner.config.llm_config import get_llm

def test_llm():
    print("Testing LLM with CrewAI...")
    try:
        llm = get_llm()
        print(f"✓ LLM initialized: {type(llm)}")
        print(f"✓ Model: {llm.model}")
        
        agent = Agent(
            role="Test Agent",
            goal="Say hello",
            backstory="A simple test agent",
            llm=llm,
            verbose=True
        )
        
        task = Task(
            description="Say hello in one sentence",
            expected_output="A greeting",
            agent=agent
        )
        
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result = crew.kickoff()
        
        print(f"\n✓ Result: {result}")
        print("\n✓ LLM configuration is working with CrewAI!")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_llm()
