# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .address_request import AddressRequest
from .email_address_request import EmailAddressRequest
from .phone_number_request import PhoneNumberRequest
from .remote_field_request import RemoteFieldRequest


class LeadRequest(pydantic.BaseModel):
    """
    # The Lead Object
    ### Description
    The `Lead` object is used to represent an individual who is a potential customer.
    ### Usage Example
    TODO
    """

    owner: typing.Optional[str] = pydantic.Field(description="The lead's owner.")
    lead_source: typing.Optional[str] = pydantic.Field(description="The lead's source.")
    title: typing.Optional[str] = pydantic.Field(description="The lead's title.")
    company: typing.Optional[str] = pydantic.Field(description="The lead's company.")
    first_name: typing.Optional[str] = pydantic.Field(description="The lead's first name.")
    last_name: typing.Optional[str] = pydantic.Field(description="The lead's last name.")
    addresses: typing.Optional[typing.List[AddressRequest]]
    email_addresses: typing.Optional[typing.List[EmailAddressRequest]]
    phone_numbers: typing.Optional[typing.List[PhoneNumberRequest]]
    converted_date: typing.Optional[str] = pydantic.Field(description="When the lead was converted.")
    converted_contact: typing.Optional[str] = pydantic.Field(description="The contact of the converted lead.")
    converted_account: typing.Optional[str] = pydantic.Field(description="The account of the converted lead.")
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}