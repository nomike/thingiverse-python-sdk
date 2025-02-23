# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.category_schema import CategorySchema
from openapi_client.models.comment_schema import CommentSchema
from openapi_client.models.copy_schema import CopySchema
from openapi_client.models.thing_schema import ThingSchema
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

SUBSCRIPTIONS0DASHBOARDGET200RESPONSEITEMSINNERCONTENT_ONE_OF_SCHEMAS = ["CategorySchema", "CommentSchema", "CopySchema", "ThingSchema"]

class Subscriptions0DashboardGet200ResponseItemsInnerContent(BaseModel):
    """
    Subscriptions0DashboardGet200ResponseItemsInnerContent
    """
    # data type: ThingSchema
    oneof_schema_1_validator: Optional[ThingSchema] = None
    # data type: CopySchema
    oneof_schema_2_validator: Optional[CopySchema] = None
    # data type: CommentSchema
    oneof_schema_3_validator: Optional[CommentSchema] = None
    # data type: CategorySchema
    oneof_schema_4_validator: Optional[CategorySchema] = None
    actual_instance: Optional[Union[CategorySchema, CommentSchema, CopySchema, ThingSchema]] = None
    one_of_schemas: Set[str] = { "CategorySchema", "CommentSchema", "CopySchema", "ThingSchema" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = Subscriptions0DashboardGet200ResponseItemsInnerContent.model_construct()
        error_messages = []
        match = 0
        # validate data type: ThingSchema
        if not isinstance(v, ThingSchema):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ThingSchema`")
        else:
            match += 1
        # validate data type: CopySchema
        if not isinstance(v, CopySchema):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CopySchema`")
        else:
            match += 1
        # validate data type: CommentSchema
        if not isinstance(v, CommentSchema):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CommentSchema`")
        else:
            match += 1
        # validate data type: CategorySchema
        if not isinstance(v, CategorySchema):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CategorySchema`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in Subscriptions0DashboardGet200ResponseItemsInnerContent with oneOf schemas: CategorySchema, CommentSchema, CopySchema, ThingSchema. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in Subscriptions0DashboardGet200ResponseItemsInnerContent with oneOf schemas: CategorySchema, CommentSchema, CopySchema, ThingSchema. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ThingSchema
        try:
            instance.actual_instance = ThingSchema.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CopySchema
        try:
            instance.actual_instance = CopySchema.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CommentSchema
        try:
            instance.actual_instance = CommentSchema.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CategorySchema
        try:
            instance.actual_instance = CategorySchema.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Subscriptions0DashboardGet200ResponseItemsInnerContent with oneOf schemas: CategorySchema, CommentSchema, CopySchema, ThingSchema. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Subscriptions0DashboardGet200ResponseItemsInnerContent with oneOf schemas: CategorySchema, CommentSchema, CopySchema, ThingSchema. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CategorySchema, CommentSchema, CopySchema, ThingSchema]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


