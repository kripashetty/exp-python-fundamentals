'''
Define a Booking Pydantic model that rejects bookings where check_out isn’t strictly after check_in. 
The rule compares two fields together, not one in isolation.
Example : 
>>> from datetime import date
>>> Booking(
...     guest_name="Carla",
...     check_in=date(2026, 5, 1),
...     check_out=date(2026, 5, 5),
... ).check_out
datetime.date(2026, 5, 5)
>>> Booking(
...     guest_name="Carla",
...     check_in=date(2026, 5, 10),
...     check_out=date(2026, 5, 3),
... )
ValidationError: check_out must be after check_in


Requirements : 
Define Booking as a BaseModel subclass.
Booking has three fields:
    guest_name: a string
    check_in: a date
    check_out: a date
A Booking where check_out is not strictly after check_in should raise pydantic.ValidationError.
'''



from datetime import date
from typing import Self

from pydantic import BaseModel, model_validator


class Booking(BaseModel):
    """A hotel booking. `check_out` must be after `check_in`."""
    guest_name: str
    check_in: date
    check_out: date
    
    @model_validator(mode="after")
    def check_out_validator(self)->Self : 
        if(self.check_in>=self.check_out):
            raise ValueError("A Booking check_out should be strictly after check_in")
        return self
        
        
if __name__ == "__main__":
    booking = Booking(guest_name="Carla",check_in=date(2026, 5, 10), check_out=date(2026, 5, 3))
    