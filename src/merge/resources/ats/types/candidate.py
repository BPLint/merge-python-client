# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .candidate_attachments_item import CandidateAttachmentsItem
from .email_address import EmailAddress
from .phone_number import PhoneNumber
from .remote_data import RemoteData
from .url import Url


class Candidate(pydantic_v1.BaseModel):
    """
    # The Candidate Object

    ### Description

    The `Candidate` object is used to represent profile information about a given Candidate. Because it is specific to a Candidate, this information stays constant across applications.

    ### Usage Example

    Fetch from the `LIST Candidates` endpoint and filter by `ID` to show all candidates.
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

    first_name: typing.Optional[str] = pydantic_v1.Field()
    """
    The candidate's first name.
    """

    last_name: typing.Optional[str] = pydantic_v1.Field()
    """
    The candidate's last name.
    """

    company: typing.Optional[str] = pydantic_v1.Field()
    """
    The candidate's current company.
    """

    title: typing.Optional[str] = pydantic_v1.Field()
    """
    The candidate's current title.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the third party's candidate was created.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the third party's candidate was updated.
    """

    last_interaction_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the most recent interaction with the candidate occurred.
    """

    is_private: typing.Optional[bool] = pydantic_v1.Field()
    """
    Whether or not the candidate is private.
    """

    can_email: typing.Optional[bool] = pydantic_v1.Field()
    """
    Whether or not the candidate can be emailed.
    """

    locations: typing.Optional[typing.List[typing.Optional[str]]] = pydantic_v1.Field()
    """
    The candidate's locations.
    """

    phone_numbers: typing.Optional[typing.List[PhoneNumber]]
    email_addresses: typing.Optional[typing.List[EmailAddress]]
    urls: typing.Optional[typing.List[Url]]
    tags: typing.Optional[typing.List[typing.Optional[str]]] = pydantic_v1.Field()
    """
    Array of `Tag` names as strings.
    """

    applications: typing.Optional[typing.List[typing.Optional[CandidateApplicationsItem]]] = pydantic_v1.Field()
    """
    Array of `Application` object IDs.
    """

    attachments: typing.Optional[typing.List[typing.Optional[CandidateAttachmentsItem]]] = pydantic_v1.Field()
    """
    Array of `Attachment` object IDs.
    """

    remote_was_deleted: typing.Optional[bool]
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

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


from .candidate_applications_item import CandidateApplicationsItem  # noqa: E402

Candidate.update_forward_refs()
