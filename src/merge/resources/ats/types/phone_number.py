# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .phone_number_phone_number_type import PhoneNumberPhoneNumberType


class PhoneNumber(pydantic_v1.BaseModel):
    """
    # The PhoneNumber Object

    ### Description

    The `PhoneNumber` object is used to represent a candidate's phone number.

    ### Usage Example

    Fetch from the `GET Candidate` endpoint and view their phone numbers.
    """

    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was modified by Merge.
    """

    value: typing.Optional[str] = pydantic_v1.Field()
    """
    The phone number.
    """

    phone_number_type: typing.Optional[PhoneNumberPhoneNumberType] = pydantic_v1.Field()
    """
    The type of phone number.
    
    - `HOME` - HOME
    - `WORK` - WORK
    - `MOBILE` - MOBILE
    - `SKYPE` - SKYPE
    - `OTHER` - OTHER
    """

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
