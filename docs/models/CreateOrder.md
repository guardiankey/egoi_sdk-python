# egoi_api.model.create_order.CreateOrder

Create data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Create data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**order_id** | str,  | str,  | Order ID is any non-empty unique string | 
**order_total** | decimal.Decimal, int, float,  | decimal.Decimal,  | Ecommerce cart total | [optional] value must be a 64 bit float
**cart_id** | str,  | str,  | Cart ID that originated this order | [optional] 
**order_date** | str, datetime,  | str,  | Date and hour of the order | [optional] value must conform to RFC-3339 date-time
**order_status** | str,  | str,  | Status of the order | [optional] must be one of ["created", "pending", "canceled", "completed", "unknown", ] if omitted the server will use the default value of "unknown"
**[contact](#contact)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact | [optional] 
**[products](#products)** | list, tuple,  | tuple,  | List of products | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contact

Contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ContactBaseExtraFull](ContactBaseExtraFull.md) | [**ContactBaseExtraFull**](ContactBaseExtraFull.md) | [**ContactBaseExtraFull**](ContactBaseExtraFull.md) |  | 

# products

List of products

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of products | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderProduct**](OrderProduct.md) | [**OrderProduct**](OrderProduct.md) | [**OrderProduct**](OrderProduct.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

