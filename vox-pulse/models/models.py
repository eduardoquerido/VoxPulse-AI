from typing import List

from pydantic import BaseModel, Field


class PoliticianMetrics(BaseModel):
    name: str = Field(..., description="Full name of the politician")
    sentiment_score: int = Field(
        ..., ge=0, le=100, description="Overall digital sentiment from 0 to 100"
    )
    economic_trust: int = Field(
        ..., ge=0, le=100, description="Public confidence in their economic policies"
    )
    digital_presence: int = Field(
        ...,
        ge=0,
        le=100,
        description="Strength of their social media and search footprint",
    )
    social_approval: int = Field(
        ..., ge=0, le=100, description="General approval rating on social issues"
    )
    public_security: int = Field(
        ...,
        ge=0,
        le=100,
        description="Perception of effectiveness in crime fighting, police management, and public order policies",
    )


class ComparisonOutput(BaseModel):
    results: List[PoliticianMetrics]
