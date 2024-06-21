# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .remote_data import RemoteData
from .time_off_approver import TimeOffApprover
from .time_off_employee import TimeOffEmployee
from .time_off_request_type import TimeOffRequestType
from .time_off_status import TimeOffStatus
from .time_off_units import TimeOffUnits


class TimeOff(pydantic_v1.BaseModel):
    """
    # The TimeOff Object

    ### Description

    The `TimeOff` object is used to represent all employees' Time Off entries.

    ### Usage Example

    Fetch from the `LIST TimeOffs` endpoint and filter by `ID` to show all time off requests.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic_v1.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was modified by Merge.
    """

    employee: typing.Optional[TimeOffEmployee] = pydantic_v1.Field()
    """
    The employee requesting time off.
    """

    approver: typing.Optional[TimeOffApprover] = pydantic_v1.Field()
    """
    The Merge ID of the employee with the ability to approve the time off request.
    """

    status: typing.Optional[TimeOffStatus] = pydantic_v1.Field()
    """
    The status of this time off request.
    
    - `REQUESTED` - REQUESTED
    - `APPROVED` - APPROVED
    - `DECLINED` - DECLINED
    - `CANCELLED` - CANCELLED
    - `DELETED` - DELETED
    """

    employee_note: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee note for this time off request.
    """

    units: typing.Optional[TimeOffUnits] = pydantic_v1.Field()
    """
    The measurement that the third-party integration uses to count time requested.
    
    - `HOURS` - HOURS
    - `DAYS` - DAYS
    """

    amount: typing.Optional[float] = pydantic_v1.Field()
    """
    The time off quantity measured by the prescribed “units”.
    """

    request_type: typing.Optional[TimeOffRequestType] = pydantic_v1.Field()
    """
    The type of time off request.
    
    - `VACATION` - VACATION
    - `SICK` - SICK
    - `PERSONAL` - PERSONAL
    - `JURY_DUTY` - JURY_DUTY
    - `VOLUNTEER` - VOLUNTEER
    - `BEREAVEMENT` - BEREAVEMENT
    """

    start_time: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The day and time of the start of the time requested off.
    """

    end_time: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The day and time of the end of the time requested off.
    """

    remote_was_deleted: typing.Optional[bool]
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
