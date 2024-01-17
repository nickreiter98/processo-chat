from enum import Enum
from instructor import OpenAISchema
from pydantic import Field

class RequestType(str, Enum):
    """User Type"""
    process_visualization = "process_visualization"
    process_optimization = "process_optimization"
    process_mining = "process_mining"

class UnderlyingData(str, Enum):
    event_log_sepsis_data = "./data/xes/Sepsis Cases - Event Log.xes"
    event_log_sports_data = None


class RequestDetails(OpenAISchema):
    """User Details"""
    process_field: str = Field(..., description="the requested task belongs a prcess from this specific business branch")
    request_type: RequestType = Field(..., description="the requested task belongs to this process type")
    underlying_data: UnderlyingData = Field(..., description="the requested task is based on this underlying data")