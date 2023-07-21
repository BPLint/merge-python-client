# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .address import Address
from .email_address import EmailAddress
from .phone_number import PhoneNumber
from .remote_data import RemoteData
from .remote_field import RemoteField


class Contact(pydantic.BaseModel):
    """
    # The Contact Object
    ### Description
    The `Contact` object is used to represent an existing point of contact at a company in a CRM system.
    ### Usage Example
    TODO
    """

    first_name: typing.Optional[str] = pydantic.Field(description="The contact's first name.")
    last_name: typing.Optional[str] = pydantic.Field(description="The contact's last name.")
    account: typing.Optional[str] = pydantic.Field(description="The contact's account.")
    addresses: typing.Optional[typing.List[Address]]
    email_addresses: typing.Optional[typing.List[EmailAddress]]
    phone_numbers: typing.Optional[typing.List[PhoneNumber]]
    last_activity_at: typing.Optional[str] = pydantic.Field(description="When the contact's last activity occurred.")
    remote_created_at: typing.Optional[str] = pydantic.Field(description="When the third party's contact was created.")
    remote_was_deleted: typing.Optional[bool]
    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    modified_at: typing.Optional[str] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]
    remote_fields: typing.Optional[typing.List[RemoteField]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}