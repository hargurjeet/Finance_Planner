from pydantic import BaseModel, Field, validator

class UserInput(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=18, le=59)
    current_monthly_income: float = Field(..., gt=0)
    current_monthly_savings: float = Field(..., ge=0)
    target_monthly_income: float = Field(..., gt=0)

    @validator("current_monthly_savings")
    def savings_cant_exceed_income(cls, v, values):
        if "current_monthly_income" in values and v > values["current_monthly_income"]:
            raise ValueError("Monthly savings cannot exceed monthly income")
        return v