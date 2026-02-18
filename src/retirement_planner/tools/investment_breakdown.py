from crewai.tools import tool

@tool("Investment Breakdown Calculator")
def investment_breakdown_tool(
    monthly_savings: float,
    age: int,
    risk_profile: str = "moderate"
) -> dict:
    """
    Suggests an investment allocation based on age and risk profile.
    Returns percentage split across asset classes.
    """
    # Rule of thumb: 100 - age = equity allocation
    equity_pct = min(max(100 - age, 30), 80)

    if risk_profile == "aggressive":
        equity_pct = min(equity_pct + 10, 90)
    elif risk_profile == "conservative":
        equity_pct = max(equity_pct - 10, 30)

    debt_pct = 100 - equity_pct
    equity_amount = monthly_savings * (equity_pct / 100)
    debt_amount = monthly_savings * (debt_pct / 100)

    return {
        "equity_allocation_pct": equity_pct,
        "debt_allocation_pct": debt_pct,
        "monthly_equity_amount": round(equity_amount, 2),
        "monthly_debt_amount": round(debt_amount, 2),
        "suggested_instruments": {
            "equity": ["Index Funds", "ETFs", "Diversified Mutual Funds"],
            "debt": ["PPF", "NPS", "Debt Mutual Funds", "Fixed Deposits"]
        }
    }
