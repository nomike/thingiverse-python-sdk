# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class MemberSchema(BaseModel):
    """
    MemberSchema
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    public_url: Optional[StrictStr] = None
    thumbnail: Optional[StrictStr] = None
    count_of_followers: Optional[StrictInt] = None
    count_of_following: Optional[StrictInt] = None
    count_of_designs: Optional[StrictInt] = None
    accepts_tips: Optional[StrictBool] = None
    is_following: Optional[StrictBool] = None
    location: Optional[StrictStr] = None
    cover: Optional[StrictStr] = None
    is_admin: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "name", "first_name", "last_name", "url", "public_url", "thumbnail", "count_of_followers", "count_of_following", "count_of_designs", "accepts_tips", "is_following", "location", "cover", "is_admin"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MemberSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MemberSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "url": obj.get("url"),
            "public_url": obj.get("public_url"),
            "thumbnail": obj.get("thumbnail"),
            "count_of_followers": obj.get("count_of_followers"),
            "count_of_following": obj.get("count_of_following"),
            "count_of_designs": obj.get("count_of_designs"),
            "accepts_tips": obj.get("accepts_tips"),
            "is_following": obj.get("is_following"),
            "location": obj.get("location"),
            "cover": obj.get("cover"),
            "is_admin": obj.get("is_admin")
        })
        return _obj


