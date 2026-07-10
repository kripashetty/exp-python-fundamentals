


## The Premise 
    - Python is a Dynamically typed Language. 
    - The type of a variable can be known only at Runtime.
    - Rapid dev is great but you need better type checking for more stable code



## Benefits 
    - Typing to validate and serialize 
    - easier to debug
    - intergrates with Static type checker
    -can validate simple to very nested
    - can decide how strictly to enforce the validation 
    - Serialization - dict and JSON string - needed for self documenting API's 
    - Performnace - Written in rust - very fast - REST application need to scale so this speed is great
    

 ## Used by 
    - FastAPi 
    - Langchain 
    - other


## Install 


## Model 
    - Primary way of defining data Schemas
    - similar to a dataclass 
    - focus is on Parsing , validation and serialization 


## Field Class
    - Base Model - validate with predefined types 
    - Fields - add custom validations 

## Custom Validators

1. __field_validator__
    - complex validations eg. that uses the value from other fields in the validation logic
    -   defined as Class methods 
    - cannot be used when there is a need to compare multiple fields or the model as a whole 

2. __model_validator__ 
    - 


 ## Decorators 
    - To validate function input values 
    - 

## Base Settings
- Parse and validate environment valriables 


 ## Questions
 - What is the emain vaidator that was installed 
 - Fields for  Validation - what is teh config settings Model config dict

 ## Decorators 
    - To validate function input values 

    
     