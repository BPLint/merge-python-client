# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .account_owner import AccountOwner
from .address import Address
from .phone_number import PhoneNumber
from .remote_data import RemoteData
from .remote_field import RemoteField


class Account(pydantic_v1.BaseModel):
    """
    # The Account Object

    ### Description

    The `Account` object is used to represent a company in a CRM system.

    ### Usage Example

    TODO
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

    owner: typing.Optional[AccountOwner] = pydantic_v1.Field()
    """
    The account's owner.
    """

    name: typing.Optional[str] = pydantic_v1.Field()
    """
    The account's name.
    """

    description: typing.Optional[str] = pydantic_v1.Field()
    """
    The account's description.
    """

    industry: typing.Optional[str] = pydantic_v1.Field()
    """
    The account's industry.
    """

    website: typing.Optional[str] = pydantic_v1.Field()
    """
    The account's website.
    """

    number_of_employees: typing.Optional[int] = pydantic_v1.Field()
    """
    The account's number of employees.
    """

    addresses: typing.Optional[typing.List[Address]]
    phone_numbers: typing.Optional[typing.List[PhoneNumber]]
    last_activity_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The last date (either most recent or furthest in the future) of when an activity occurs in an account.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the CRM system account data was last modified by a user with a login.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the third party's account was created.
    """

    remote_was_deleted: typing.Optional[bool]
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]
    remote_fields: typing.Optional[typing.List[RemoteField]]

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
