# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .employee import Employee
from .employment import Employment
from .team import Team
import typing
import pydantic
import datetime as dt
from .bank_info_employee import BankInfoEmployee
from .bank_info_account_type import BankInfoAccountType
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.pydantic_utilities import update_forward_refs


class BankInfo(UniversalBaseModel):
    """
    # The BankInfo Object

    ### Description

    The `BankInfo` object is used to represent the Bank Account information for an Employee.

    ### Usage Example

    Fetch from the `LIST BankInfo` endpoint and filter by `ID` to show all bank information.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was modified by Merge.
    """

    employee: typing.Optional[BankInfoEmployee] = pydantic.Field()
    """
    The employee with this bank account.
    """

    account_number: typing.Optional[str] = pydantic.Field()
    """
    The account number.
    """

    routing_number: typing.Optional[str] = pydantic.Field()
    """
    The routing number.
    """

    bank_name: typing.Optional[str] = pydantic.Field()
    """
    The bank name.
    """

    account_type: typing.Optional[BankInfoAccountType] = pydantic.Field()
    """
    The bank account type
    
    - `SAVINGS` - SAVINGS
    - `CHECKING` - CHECKING
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the matching bank object was created in the third party system.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Employee, BankInfo=BankInfo)
update_forward_refs(Employment, BankInfo=BankInfo)
update_forward_refs(Team, BankInfo=BankInfo)
