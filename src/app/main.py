import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from retirement_planner.schemas.user_input import UserInput
from retirement_planner.crew.retirement_crew import run_retirement_crew

def get_user_inputs() -> UserInput:
    print("\n========================================")
    print("   🏦  Retirement Planner - powered by AI")
    print("========================================\n")
    return UserInput(
        name                    = input("Your name                       : ").strip(),
        age                     = int(input("Your current age                : ")),
        current_monthly_income  = float(input("Current monthly income (£)      : ")),
        current_monthly_savings = float(input("Current monthly savings (£)     : ")),
        target_monthly_income   = float(input("Target monthly income at 60 (£) : ")),
    )

def main():
    user_input = get_user_inputs()
    print("\n⏳ Running your retirement analysis...\n")
    result = run_retirement_crew(user_input)
    print("\n========================================")
    print("         📋 YOUR RETIREMENT PLAN")
    print("========================================\n")
    print(result)

if __name__ == "__main__":
    main()