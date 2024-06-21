# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .employee_company import EmployeeCompany
from .employee_employment_status import EmployeeEmploymentStatus
from .employee_ethnicity import EmployeeEthnicity
from .employee_gender import EmployeeGender
from .employee_groups_item import EmployeeGroupsItem
from .employee_home_location import EmployeeHomeLocation
from .employee_marital_status import EmployeeMaritalStatus
from .employee_pay_group import EmployeePayGroup
from .employee_team import EmployeeTeam
from .employee_work_location import EmployeeWorkLocation
from .remote_data import RemoteData


class Employee(pydantic_v1.BaseModel):
    """
    # The Employee Object

    ### Description

    The `Employee` object is used to represent any person who has been employed by a company.

    ### Usage Example

    Fetch from the `LIST Employee` endpoint and filter by `ID` to show all employees.
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

    employee_number: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee's number that appears in the third-party integration's UI.
    """

    company: typing.Optional[EmployeeCompany] = pydantic_v1.Field()
    """
    The ID of the employee's company.
    """

    first_name: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee's first name.
    """

    last_name: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee's last name.
    """

    preferred_name: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee's preferred first name.
    """

    display_full_name: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee's full name, to use for display purposes. If a preferred first name is available, the full name will include the preferred first name.
    """

    username: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee's username that appears in the remote UI.
    """

    groups: typing.Optional[typing.List[typing.Optional[EmployeeGroupsItem]]]
    work_email: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee's work email.
    """

    personal_email: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee's personal email.
    """

    mobile_phone_number: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee's mobile phone number.
    """

    employments: typing.Optional[typing.List[typing.Optional[EmployeeEmploymentsItem]]] = pydantic_v1.Field()
    """
    Array of `Employment` IDs for this Employee.
    """

    home_location: typing.Optional[EmployeeHomeLocation] = pydantic_v1.Field()
    """
    The employee's home address.
    """

    work_location: typing.Optional[EmployeeWorkLocation] = pydantic_v1.Field()
    """
    The employee's work address.
    """

    manager: typing.Optional[EmployeeManager] = pydantic_v1.Field()
    """
    The employee ID of the employee's manager.
    """

    team: typing.Optional[EmployeeTeam] = pydantic_v1.Field()
    """
    The employee's team.
    """

    pay_group: typing.Optional[EmployeePayGroup] = pydantic_v1.Field()
    """
    The employee's pay group
    """

    ssn: typing.Optional[str] = pydantic_v1.Field()
    """
    The employee's social security number.
    """

    gender: typing.Optional[EmployeeGender] = pydantic_v1.Field()
    """
    The employee's gender.
    
    - `MALE` - MALE
    - `FEMALE` - FEMALE
    - `NON-BINARY` - NON-BINARY
    - `OTHER` - OTHER
    - `PREFER_NOT_TO_DISCLOSE` - PREFER_NOT_TO_DISCLOSE
    """

    ethnicity: typing.Optional[EmployeeEthnicity] = pydantic_v1.Field()
    """
    The employee's ethnicity.
    
    - `AMERICAN_INDIAN_OR_ALASKA_NATIVE` - AMERICAN_INDIAN_OR_ALASKA_NATIVE
    - `ASIAN_OR_INDIAN_SUBCONTINENT` - ASIAN_OR_INDIAN_SUBCONTINENT
    - `BLACK_OR_AFRICAN_AMERICAN` - BLACK_OR_AFRICAN_AMERICAN
    - `HISPANIC_OR_LATINO` - HISPANIC_OR_LATINO
    - `NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER` - NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER
    - `TWO_OR_MORE_RACES` - TWO_OR_MORE_RACES
    - `WHITE` - WHITE
    - `PREFER_NOT_TO_DISCLOSE` - PREFER_NOT_TO_DISCLOSE
    """

    marital_status: typing.Optional[EmployeeMaritalStatus] = pydantic_v1.Field()
    """
    The employee's filing status as related to marital status.
    
    - `SINGLE` - SINGLE
    - `MARRIED_FILING_JOINTLY` - MARRIED_FILING_JOINTLY
    - `MARRIED_FILING_SEPARATELY` - MARRIED_FILING_SEPARATELY
    - `HEAD_OF_HOUSEHOLD` - HEAD_OF_HOUSEHOLD
    - `QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD` - QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD
    """

    date_of_birth: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The employee's date of birth.
    """

    hire_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The date that the employee was hired, usually the day that an offer letter is signed. If an employee has multiple hire dates from previous employments, this represents the most recent hire date. Note: If you're looking for the employee's start date, refer to the start_date field.
    """

    start_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The date that the employee started working. If an employee was rehired, the most recent start date will be returned.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the third party's employee was created.
    """

    employment_status: typing.Optional[EmployeeEmploymentStatus] = pydantic_v1.Field()
    """
    The employment status of the employee.
    
    - `ACTIVE` - ACTIVE
    - `PENDING` - PENDING
    - `INACTIVE` - INACTIVE
    """

    termination_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The employee's termination date.
    """

    avatar: typing.Optional[str] = pydantic_v1.Field()
    """
    The URL of the employee's avatar image.
    """

    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field()
    """
    Custom fields configured for a given model.
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
        extra = pydantic_v1.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


from .employee_employments_item import EmployeeEmploymentsItem  # noqa: E402
from .employee_manager import EmployeeManager  # noqa: E402

Employee.update_forward_refs()
