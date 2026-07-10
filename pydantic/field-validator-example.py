'''
Define a Coupon Pydantic model that rejects any discount_percent value that isn’t a multiple of 5.
Example : 
>>> Coupon(code="SAVE10", discount_percent=10).discount_percent
10
>>> Coupon(code="SAVE3", discount_percent=3)
ValidationError: discount_percent must be a multiple of 5


Requirements : 
Define Coupon as a BaseModel subclass.
Coupon has two fields:
    code: a string
    discount_percent: an integer
Constructing a Coupon with a discount_percent that isn’t a multiple of 5 should raise pydantic.ValidationError.
'''



from pydantic import BaseModel, field_validator


class Coupon(BaseModel):
    """A discount coupon. `discount_percent` must be a multiple of 5."""
    code: str
    discount_percent: int
    
    @field_validator("discount_percent")
    @classmethod
    def discount_percent_validator(cls,discount_percent: int )-> int:
        if  discount_percent%5 != 0 :
            raise ValueError("discount_percent must be a multiple of 5")
        # Without return discount_percent, Pydantic would set the field to None after validation, which is a silent bug.
        return discount_percent
    
    
    
if __name__ == "__main__":
    coupon = Coupon(code="SAVE10", discount_percent=10)
    coupon = Coupon(code="SAVE10", discount_percent=9)