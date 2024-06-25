# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .remote_data import RemoteData
from .time_off_balance_employee import TimeOffBalanceEmployee
from .time_off_balance_policy_type import TimeOffBalancePolicyType


class TimeOffBalance(pydantic_v1.BaseModel):
    """
    # The TimeOffBalance Object

    ### Description

    The `TimeOffBalance` object is used to represent current balances for an employee's Time Off plan.

    ### Usage Example

    Fetch from the `LIST TimeOffBalances` endpoint and filter by `ID` to show all time off balances.
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

    employee: typing.Optional[TimeOffBalanceEmployee] = pydantic_v1.Field()
    """
    The employee the balance belongs to.
    """

    balance: typing.Optional[float] = pydantic_v1.Field()
    """
    The current remaining PTO balance, always measured in terms of hours.
    """

    used: typing.Optional[float] = pydantic_v1.Field()
    """
    The amount of PTO used in terms of hours.
    """

    policy_type: typing.Optional[TimeOffBalancePolicyType] = pydantic_v1.Field()
    """
    The policy type of this time off balance.
    
    - `VACATION` - VACATION
    - `SICK` - SICK
    - `PERSONAL` - PERSONAL
    - `JURY_DUTY` - JURY_DUTY
    - `VOLUNTEER` - VOLUNTEER
    - `BEREAVEMENT` - BEREAVEMENT
    """

    remote_was_deleted: typing.Optional[bool] = pydantic_v1.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

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
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
