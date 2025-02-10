# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**bio_html** | **str** |  | [optional] 
**level** | **int** | Is the user an admin or moderator? This will return 10 if user is a normal user | [optional] 
**location** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**registered** | **datetime** |  | [optional] 
**last_active** | **datetime** |  | [optional] 
**cover_image** | **str** |  | [optional] 
**things_url** | **str** |  | [optional] 
**copies_url** | **str** |  | [optional] 
**likes_url** | **str** |  | [optional] 
**printers** | [**List[UserPrintersInner]**](UserPrintersInner.md) |  | [optional] 
**programs** | [**List[UserProgramsInner]**](UserProgramsInner.md) |  | [optional] 
**types** | [**List[UserTypesInner]**](UserTypesInner.md) |  | [optional] 
**skill_level** | **str** |  | [optional] 
**accepts_tips** | **bool** |  | [optional] 
**groups** | [**List[UserGroupsInner]**](UserGroupsInner.md) |  | [optional] 
**website** | **str** |  | [optional] 
**twitter** | [**UserTwitter**](UserTwitter.md) |  | [optional] 
**count_of_followers** | **int** |  | [optional] 
**count_of_following** | **int** |  | [optional] 
**count_of_designs** | **int** |  | [optional] 
**collection_count** | **int** |  | [optional] 
**make_count** | **int** |  | [optional] 
**like_count** | **int** |  | [optional] 
**has_favorite** | **bool** |  | [optional] 
**favorite_count** | **int** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**is_moderator** | **bool** |  | [optional] 
**is_featured** | **bool** |  | [optional] 
**is_verified** | **bool** |  | [optional] 
**is_following** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


