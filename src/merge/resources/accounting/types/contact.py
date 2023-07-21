# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .accounting_phone_number import AccountingPhoneNumber
from .contact_status import ContactStatus
from .remote_data import RemoteData


class Contact(pydantic.BaseModel):
    """
    # The Contact Object
    ### Description
    The `Contact` object refers to either a supplier or a customer.

    ### Usage Example
    Fetch from the `LIST Contacts` endpoint and view a company's contacts.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    name: typing.Optional[str] = pydantic.Field(description="The contact's name.")
    is_supplier: typing.Optional[bool] = pydantic.Field(description="Whether the contact is a supplier.")
    is_customer: typing.Optional[bool] = pydantic.Field(description="Whether the contact is a customer.")
    email_address: typing.Optional[str] = pydantic.Field(description="The contact's email address.")
    tax_number: typing.Optional[str] = pydantic.Field(description="The contact's tax number.")
    status: typing.Optional[ContactStatus] = pydantic.Field(
        description=("The contact's status\n" "\n" "* `ACTIVE` - ACTIVE\n" "* `ARCHIVED` - ARCHIVED\n")
    )
    currency: typing.Optional[str] = pydantic.Field(description="The currency the contact's transactions are in.")
    remote_updated_at: typing.Optional[str] = pydantic.Field(description="When the third party's contact was updated.")
    company: typing.Optional[str] = pydantic.Field(description="The company the contact belongs to.")
    addresses: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(
        description="`Address` object IDs for the given `Contacts` object."
    )
    phone_numbers: typing.Optional[typing.List[AccountingPhoneNumber]] = pydantic.Field(
        description="`AccountingPhoneNumber` object for the given `Contacts` object."
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted by third party webhooks."
    )
    modified_at: typing.Optional[str] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}