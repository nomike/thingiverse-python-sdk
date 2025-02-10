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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.image_summary_schema import ImageSummarySchema
from typing import Optional, Set
from typing_extensions import Self

class FileSchema(BaseModel):
    """
    FileSchema
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
    public_url: Optional[StrictStr] = None
    download_url: Optional[StrictStr] = None
    threejs_url: Optional[StrictStr] = None
    thumbnail: Optional[StrictStr] = None
    default_image: Optional[ImageSummarySchema] = None
    var_date: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="date")
    formatted_size: Optional[StrictStr] = Field(default=None, description="a formatted string of a filesize")
    meta_data: Optional[List[StrictStr]] = None
    download_count: Optional[StrictInt] = None
    direct_url: Optional[StrictStr] = Field(default=None, description="This will return null if it's not in the 'printable' file list (eg a pdf)")
    __properties: ClassVar[List[str]] = ["id", "name", "size", "url", "public_url", "download_url", "threejs_url", "thumbnail", "default_image", "date", "formatted_size", "meta_data", "download_count", "direct_url"]

    @field_validator('var_date')
    def var_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", value):
            raise ValueError(r"must validate the regular expression /\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/")
        return value

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
        """Create an instance of FileSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default_image
        if self.default_image:
            _dict['default_image'] = self.default_image.to_dict()
        # set to None if default_image (nullable) is None
        # and model_fields_set contains the field
        if self.default_image is None and "default_image" in self.model_fields_set:
            _dict['default_image'] = None

        # set to None if direct_url (nullable) is None
        # and model_fields_set contains the field
        if self.direct_url is None and "direct_url" in self.model_fields_set:
            _dict['direct_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "size": obj.get("size"),
            "url": obj.get("url"),
            "public_url": obj.get("public_url"),
            "download_url": obj.get("download_url"),
            "threejs_url": obj.get("threejs_url"),
            "thumbnail": obj.get("thumbnail"),
            "default_image": ImageSummarySchema.from_dict(obj["default_image"]) if obj.get("default_image") is not None else None,
            "date": obj.get("date"),
            "formatted_size": obj.get("formatted_size"),
            "meta_data": obj.get("meta_data"),
            "download_count": obj.get("download_count"),
            "direct_url": obj.get("direct_url")
        })
        return _obj


