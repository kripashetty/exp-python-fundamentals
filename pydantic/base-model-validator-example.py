"""
Write a function clean_order(payload) that uses a Pydantic Order model to validate a raw order dictionary 
and return a normalized dict. Pydantic coerces compatible string input (so "42" becomes 42), and invalid input raises pydantic.ValidationError.

>>> clean_order({
...     "order_id": 42,
...     "customer_email": "ana@x.co",
...     "total": 7.5,
... })
{'order_id': 42, 'customer_email': 'ana@x.co', 'total': 7.5}
>>> clean_order({
...     "order_id": "nope",
...     "customer_email": "ana@x.co",
...     "total": 1.99,
... })
ValidationError: order_id - Input should be a valid integer



Requirements
Define an Order Pydantic model that inherits from BaseModel.
Order has three fields:
order_id: an integer
customer_email: an email address
total: a float
clean_order() validates the payload against Order and returns a normalized dict.
Invalid input should raise pydantic.ValidationError.
"""


from pydantic import BaseModel, EmailStr



class Order(BaseModel):
    """An e-commerce order."""
    order_id: int
    customer_email: EmailStr
    total: float


def clean_order(payload)-> dict:
    """Validate a raw order dict and return a normalized dict."""
    # takes a dict and validates and vonverts an object 
    normalized_dict = Order.model_validate(payload)
    # Check the type of the variable
    print(type(normalized_dict)) 
    
    # Print normalized Dict
    print(normalized_dict.model_dump())
    # Print normalized JSON
    print(normalized_dict.model_dump_json())
    return normalized_dict.model_dump()


if __name__ == "__main__":
    # Valid Input
    clean_order({"order_id": 42,"customer_email": "ana@x.co", "total": 7.5,})
    # Valid Input - Pydantic will coerce the string "42" to int
    clean_order({"order_id": "42","customer_email": "ana@x.co", "total": 7.5,})
    # # Valid Input - Pydantic will validate missing fields
    # # clean_order({"order_id": "42", "total": 7.5,})
    # # Invalid input - "nope" is not a number
    # clean_order({"order_id": "nope","customer_email": "ana@x.co", "total": 7.5,})