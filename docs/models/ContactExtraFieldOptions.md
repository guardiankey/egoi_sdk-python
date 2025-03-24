# egoi_api.model.contact_extra_field_options.ContactExtraFieldOptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**field_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | [optional] 
**format** | str,  | str,  | Extra field format | [optional] must be one of ["options", ] 
**[value](#value)** | list, tuple,  | tuple,  | Extra field options Id&#x27;s &lt;a href&#x3D;&#x27;/api/v3/#tag/Fields/operation/getAllFieldOptions&#x27; target&#x3D;&#x27;_blank&#x27;&gt;[Go to getAllFieldOptions documentation]&lt;/a&gt; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# value

Extra field options Id's <a href='/api/v3/#tag/Fields/operation/getAllFieldOptions' target='_blank'>[Go to getAllFieldOptions documentation]</a>

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Extra field options Id&#x27;s &lt;a href&#x3D;&#x27;/api/v3/#tag/Fields/operation/getAllFieldOptions&#x27; target&#x3D;&#x27;_blank&#x27;&gt;[Go to getAllFieldOptions documentation]&lt;/a&gt; | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

