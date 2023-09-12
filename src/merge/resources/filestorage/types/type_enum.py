# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TypeEnum(str, enum.Enum):
    """
    * `USER` - USER
    * `GROUP` - GROUP
    * `COMPANY` - COMPANY
    * `ANYONE` - ANYONE
    """

    USER = "USER"
    GROUP = "GROUP"
    COMPANY = "COMPANY"
    ANYONE = "ANYONE"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        anyone: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TypeEnum.USER:
            return user()
        if self is TypeEnum.GROUP:
            return group()
        if self is TypeEnum.COMPANY:
            return company()
        if self is TypeEnum.ANYONE:
            return anyone()