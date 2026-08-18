Following this official documentation - https://fastapi.tiangolo.com/learn/


### Python Types 
- FastAPI leevrages this language concept heavily
- Metadata Annotations is also a Python Language concept it leverages
- What is uses these for, 
  - Define Requirements - define request Path params , query params, headers , bodies , dependencies 
  - Convert data - the data on the request can be validated
  - Validate data - each request data can be validated
  - document the API - the Open AI spec document that it generates

- 


### Concurrency and async/await

- code blacks that can be run by different threads is annotated with the async keyword and implicitly the thread that needs access with await on the current processing thread to exit
- Asyncronous
  - program that needs to wait for an external operation that is slow
  - it has a way to be asynchronized with the slow process. It can go off do other things and come back and pick back up once the process it was waitng for is done
  - this is also called Concurrency which is different from parallelism 
- async/await
  - syntax to indicate that a code block needs to pause
- Coroutines 
  - Code black that can be paused


Path Parameters → Query Parameters → Request Body → Validation → Response Models → Errors → Dependencies → Security basics → SQL databases → Bigger Applications → Background Tasks → Testing.


## Tutorial 

- Library Skills - [Library Skills](https://library-skills.io/)
- it stays aligned with the version of fast api you are using 
- 
  - How to keep these updated?

Basics 

- FastAPI() is a class that provides all functionalities to the API
- project.toml file should define the module (*main*) in which the fastAPI class is instantiate and the name of the instance (*app*) which is the main point of interaction.
- path , operation decoration on the function that implements the path operation -> Vocabulary!


- Path Parameters 
  - FastAPI uses the  declared type to  
    - for parameter parsing converting them to the
    - validating the path parameter sent in the path params - done under the hood by Pydantic
    - documentation in the schema docs
  - Order matters - path operations declaration order is imp /users/me  should be declared before /users/{user_name} because the path operationa re evaluated in order by FastAPI
  - FastAPI gives 
    - Data parsing 
    - Data validation 
    - API annotation and documentations
- Query Parameters
  - Can be set to default values 
  - can be made optional by setting type to None and default as None
  - can be made mandatory 
  - can have a mix of all the above
  - get the same validation , parsing and documentation benefits as Path parameters

- Request Body
  - You need to use Pydantic Models
  - declare them as the path operation function arguments
  - when using Query Parameters and Request Body m, the singular types (str , int , bool float , etc.) are parsed as the Query Parameters. The pydantic model type will be parsed as the Request Body
  
- Annotated for path , query and response parameters
  - The syntax looks like this: Annotated[TheActualType, Metadata1, Metadata2, ...]
  - Allows you to provide extra metadata or validations along with type hints
  - Frameworks lie FastAPi and pydantic use these to do validationn ,serializing , documentation
  - use can use Path() , Query() etc. from fastapi or can use pydantics validator fuctions like [BeforeValidator](https://pydantic.dev/docs/validation/latest/concepts/validators/#field-before-validator), or just add custom validations
  - [Read More](https://dev.to/thearjun/supercharge-your-python-types-with-annotated-29f4)

- Multiple body parameters with a mix of Query and path
  - By default non singular type parameters are treated as request params 
  - if there are multiple such non singular type params then fast API with expect a json with the parameter names as the key 
  - if you additionally want a singular body  param then use  Body()
  - you can also use embed = tru is you have a single request parameter but you want that to be the key in the request sent by the client
  - [Read More](https://fastapi.tiangolo.com/tutorial/body-multiple-params/)
  - 
- Pydantic's Fields 
  - is similar to Path , query , Bosy from fastAPI and can be used with Pydantic model fields as are the others used for path operation function parameters
  
- Pydantics Model config 
  - a dictionalry of values that can be used to define the configuration of the models
  - [Read More](https://pydantic.dev/docs/validation/latest/api/pydantic/config/)

- Pydantic core 
- written in Rust 
- faster for validations and serializations 
- 

- Return Type 
- 1. Use the path operation function return type 
- 2. Use the path operation decorators parameter to declare the return model , FastAPi will do the Response Model generation
- 3. When you want to declare the return type but the function returns an object with more fields then to get tooling support and FastAPI filtering , use Inheritence 
- 4. Disable response Model generation when you want the response type to be a union of type s(this or that)
- 5. If response model is a pydantic model but the model has a lot of optional fields , that are not set , then we can exclude them form the response instead of sending all empty values or default values(FastAPI can infer if a value was explicitly set to a value same as teh default or if the value was infact just the default) or None ,  *response_model_exclude_unset* , *response_model_exclude_defaults* , *response_model_exclude_none*. We can also include of exclude values explicitly *response_model_exclude* , *response_model_include*
- 6. Getting a Pydantic model from another Pydantic model , use .model_dump() and unpack it with **, additionally provide any extra fields 
- 7. response_model can be Union , List , some arbitary dictionary 
- Use inheritence freely between pydantic models if you want the model to have different states. this is how the JSON REsponse , Response , RedirectREsp


Handling Exceptions 
- Raised HTTPException will be handled by FastAPI. You can return anything in the content of the exception and FastAPI will take case of converting to JSON 
- Custom exceptions handler can be declared using the decorator @app.exception_handler(exception:Exception). The handler will get a Request and the exception
- DefaultExceptionHandlers - same as above but the Exception passed to the decorator will be the defaultException whoes behaviour is to be overrided
  

- Python json.dumps v/s fastAPI's jsonable_encoder v/s pydantics model_dump 

---

- Dependencies 
  - Dependency Injection - leverage Type Annotation with Depends() to declare the dependency and the Framework takes care of injecting the values , including them in the OpenAPI schema
  - Dependency functions can be sync or async , the framework will take care.
  - You can also create a typing alias instead of repeating the Annotated type with dependencies
  - You need anything that is a Callable to be passed as the depends parameter. So it can be a function or a class as well 
  - you can hve deep dependency trees
  - in case these is a common dependency in the tree then the framework caches the result rather than calling repeatedly, you can ignore the cache by explicitly specifying not to use it
  - There can be case where the **dependencies don't return anything** or you don't want to use the returned value. You just want the dependency function to be called -> then just add then as parameters in the path operation decorator
  - When declaring dependencies in the decorator, if the dependency returns any value it will not be used
  - **Global Dependencies** - If you want all the path operations to have a dependency then you can pass it to the FastAPI module itself as the dependencies parameter. individual dependencies can also be defined in addition to the global ones
  - **Dependencies with Yield** - Function that do something extra before exiting (tear down , cleanup , context manager exit code , closing code)
- 
- 

- Security
  - Support several schemes for security
  -  Password FLow 
     -  OAuth2 - the BE can be independent of the server that authenticates it
     -  Use PyJWT to generate and verify JWT tokens in Python
     -  Use pwdlib to handle password hashes - recommended algo - Argon2
- Middleware
  - @app.middleware decorator or the app.middleware() method
  - Can have multiple middleware where each is stacked on teh other in execution order
  - 


- Background Tasks
  - Run after the response is returned.
  - Use Celery or so when you need heavy computation or jobs that need not be run by the same process



### Key Python Language features that astAPI leverages as a framework
- Context Managers 
- TYpe hin
