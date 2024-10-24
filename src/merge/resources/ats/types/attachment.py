# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .attachment_attachment_type import AttachmentAttachmentType
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Attachment(UniversalBaseModel):
    """
    # The Attachment Object

    ### Description

    The `Attachment` object is used to represent a file attached to a candidate.

    ### Usage Example

    Fetch from the `LIST Attachments` endpoint and view attachments accessible by a company.
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

    file_name: typing.Optional[str] = pydantic.Field()
    """
    The attachment's name.
    """

    file_url: typing.Optional[str] = pydantic.Field()
    """
    The attachment's url.
    """

    candidate: typing.Optional[str] = pydantic.Field()
    """
    
    """

    attachment_type: typing.Optional[AttachmentAttachmentType] = pydantic.Field()
    """
    The attachment's type.
    
    - `RESUME` - RESUME
    - `COVER_LETTER` - COVER_LETTER
    - `OFFER_LETTER` - OFFER_LETTER
    - `OTHER` - OTHER
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
