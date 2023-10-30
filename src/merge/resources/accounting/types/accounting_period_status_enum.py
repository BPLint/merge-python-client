# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AccountingPeriodStatusEnum(str, enum.Enum):
    """
    * `ACTIVE` - ACTIVE
    * `INACTIVE` - INACTIVE
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is AccountingPeriodStatusEnum.ACTIVE:
            return active()
        if self is AccountingPeriodStatusEnum.INACTIVE:
            return inactive()