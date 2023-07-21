# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AddressTypeEnum(str, enum.Enum):
    """
    * `BILLING` - BILLING
    * `SHIPPING` - SHIPPING
    """

    BILLING = "BILLING"
    SHIPPING = "SHIPPING"

    def visit(self, billing: typing.Callable[[], T_Result], shipping: typing.Callable[[], T_Result]) -> T_Result:
        if self is AddressTypeEnum.BILLING:
            return billing()
        if self is AddressTypeEnum.SHIPPING:
            return shipping()