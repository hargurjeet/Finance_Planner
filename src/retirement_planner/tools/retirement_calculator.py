from crewai.tools import tool
from retirement_planner.config.setting import settings

@tool("Retirement Calculator")
def retirement_calculator_tool(
    current_age: int,
    current_monthly_income: float,
    current_monthly_savings: float,
    target_monthly_income: float,
    annual_return_rate: float = 0.07,
    inflation_rate: float = 0.03,
    retirement_age: int = 60
) -> dict:
    """
    Calculates retirement projections including:
    - Years until retirement
    - Required retirement corpus
    - Projected savings at retirement
    - Monthly savings gap
    - Inflation-adjusted target income
    """
    years_to_retirement = retirement_age - current_age
    months_to_retirement = years_to_retirement * 12
    monthly_return = annual_return_rate / 12

    # Inflation-adjusted target monthly income at retirement
    inflation_adjusted_target = target_monthly_income * (
        (1 + inflation_rate) ** years_to_retirement
    )

    # Required corpus to sustain retirement for 25 years (till age 85)
    # Using present value of annuity formula
    retirement_duration_months = 25 * 12
    real_rate = (1 + annual_return_rate) / (1 + inflation_rate) - 1
    monthly_real_rate = real_rate / 12

    required_corpus = inflation_adjusted_target * (
        (1 - (1 + monthly_real_rate) ** -retirement_duration_months)
        / monthly_real_rate
    )

    # Projected corpus from current savings (future value of annuity)
    projected_corpus = current_monthly_savings * (
        ((1 + monthly_return) ** months_to_retirement - 1)
        / monthly_return
    )

    # Monthly savings needed to hit required corpus
    required_monthly_savings = required_corpus * (
        monthly_return
        / ((1 + monthly_return) ** months_to_retirement - 1)
    )

    savings_gap = required_monthly_savings - current_monthly_savings
    savings_rate = (current_monthly_savings / current_monthly_income) * 100

    return {
        "years_to_retirement": years_to_retirement,
        "inflation_adjusted_target_income": round(inflation_adjusted_target, 2),
        "required_corpus": round(required_corpus, 2),
        "projected_corpus": round(projected_corpus, 2),
        "corpus_gap": round(required_corpus - projected_corpus, 2),
        "current_monthly_savings": round(current_monthly_savings, 2),
        "required_monthly_savings": round(required_monthly_savings, 2),
        "monthly_savings_gap": round(savings_gap, 2),
        "current_savings_rate_pct": round(savings_rate, 2),
        "on_track": projected_corpus >= required_corpus
    }
