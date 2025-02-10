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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.comment_attachments_inner import CommentAttachmentsInner
from openapi_client.models.comment_modified import CommentModified
from openapi_client.models.thing_schema import ThingSchema
from openapi_client.models.user_summary_schema1 import UserSummarySchema1
from typing import Optional, Set
from typing_extensions import Self

class Comment(BaseModel):
    """
    Comment
    """ # noqa: E501
    id: StrictInt
    url: Optional[StrictStr] = None
    target_type: Optional[StrictStr] = None
    target_id: Optional[StrictInt] = None
    public_url: Optional[StrictStr] = None
    target_url: Optional[StrictStr] = None
    body: Optional[StrictStr] = None
    body_html: Optional[StrictStr] = None
    user: Optional[UserSummarySchema1] = None
    added: Optional[datetime] = None
    modified: Optional[CommentModified] = None
    parent_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    parent_url: Optional[StrictStr] = None
    parent_user_name: Optional[StrictStr] = None
    is_deleted: Optional[StrictBool] = None
    attachments: Optional[List[CommentAttachmentsInner]] = None
    needs_moderation: Optional[StrictBool] = None
    is_root_comment: Optional[StrictBool] = None
    has_children: Optional[StrictBool] = None
    recaptcha_token: Optional[StrictStr] = None
    can_comment: Optional[StrictBool] = None
    things: Optional[List[ThingSchema]] = None
    __properties: ClassVar[List[str]] = ["id", "url", "target_type", "target_id", "public_url", "target_url", "body", "body_html", "user", "added", "modified", "parent_id", "parent_url", "parent_user_name", "is_deleted", "attachments", "needs_moderation", "is_root_comment", "has_children", "recaptcha_token", "can_comment", "things"]

    @field_validator('target_type')
    def target_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['grouptopic', 'message', 'thing', 'make', 'app']):
            raise ValueError("must be one of enum values ('grouptopic', 'message', 'thing', 'make', 'app')")
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
        """Create an instance of Comment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified
        if self.modified:
            _dict['modified'] = self.modified.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in things (list)
        _items = []
        if self.things:
            for _item_things in self.things:
                if _item_things:
                    _items.append(_item_things.to_dict())
            _dict['things'] = _items
        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if parent_user_name (nullable) is None
        # and model_fields_set contains the field
        if self.parent_user_name is None and "parent_user_name" in self.model_fields_set:
            _dict['parent_user_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Comment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "url": obj.get("url"),
            "target_type": obj.get("target_type"),
            "target_id": obj.get("target_id"),
            "public_url": obj.get("public_url"),
            "target_url": obj.get("target_url"),
            "body": obj.get("body"),
            "body_html": obj.get("body_html"),
            "user": UserSummarySchema1.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "added": obj.get("added"),
            "modified": CommentModified.from_dict(obj["modified"]) if obj.get("modified") is not None else None,
            "parent_id": obj.get("parent_id"),
            "parent_url": obj.get("parent_url"),
            "parent_user_name": obj.get("parent_user_name"),
            "is_deleted": obj.get("is_deleted"),
            "attachments": [CommentAttachmentsInner.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "needs_moderation": obj.get("needs_moderation"),
            "is_root_comment": obj.get("is_root_comment"),
            "has_children": obj.get("has_children"),
            "recaptcha_token": obj.get("recaptcha_token"),
            "can_comment": obj.get("can_comment"),
            "things": [ThingSchema.from_dict(_item) for _item in obj["things"]] if obj.get("things") is not None else None
        })
        return _obj


