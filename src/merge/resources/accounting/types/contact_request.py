# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .accounting_phone_number_request import AccountingPhoneNumberRequest
from .contact_request_addresses_item import ContactRequestAddressesItem
from .contact_request_status import ContactRequestStatus


class ContactRequest(pydantic_v1.BaseModel):
    """
    # The Contact Object

    ### Description

    A `Contact` is an individual or business entity to which products and services are sold to or purchased from. The `Contact` model contains both Customers, in which products and services are sold to, and Vendors (or Suppliers), in which products and services are purchased from.

    - A `Contact` is a Vendor/Supplier if the `is_supplier` property is true.
    - A `Contact` is a customer if the `is_customer` property is true.

    ### Usage Example

    Fetch from the `LIST Contacts` endpoint and view a company's contacts.
    """

    name: typing.Optional[str] = pydantic_v1.Field()
    """
    The contact's name.
    """

    is_supplier: typing.Optional[bool] = pydantic_v1.Field()
    """
    Whether the contact is a supplier.
    """

    is_customer: typing.Optional[bool] = pydantic_v1.Field()
    """
    Whether the contact is a customer.
    """

    email_address: typing.Optional[str] = pydantic_v1.Field()
    """
    The contact's email address.
    """

    tax_number: typing.Optional[str] = pydantic_v1.Field()
    """
    The contact's tax number.
    """

    status: typing.Optional[ContactRequestStatus] = pydantic_v1.Field()
    """
    The contact's status
    
    - `ACTIVE` - ACTIVE
    - `ARCHIVED` - ARCHIVED
    """

    currency: typing.Optional[str] = pydantic_v1.Field()
    """
    The currency the contact's transactions are in.
    """

    company: typing.Optional[str] = pydantic_v1.Field()
    """
    The company the contact belongs to.
    """

    addresses: typing.Optional[typing.List[typing.Optional[ContactRequestAddressesItem]]] = pydantic_v1.Field()
    """
    `Address` object IDs for the given `Contacts` object.
    """

    phone_numbers: typing.Optional[typing.List[AccountingPhoneNumberRequest]] = pydantic_v1.Field()
    """
    `AccountingPhoneNumber` object for the given `Contacts` object.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

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
