# Django-RestFul Api app

## requirements 

* Django - `pip install django`
* Django Rest FrameWork  - `pip install djangorestframework`
* Django Rest Jwt - `pip install djangorestframework-jwt`

### My apps
* api_basic
    

**Serializers**
* to package and unpackage api data to and from the server so that it can  be understood by other technologies and it is very customizable
* whereas for data where we dont need to alter and play with fields much its better to use ModelSerializer

**ModelSerializer**
* very easy to use and better option for smaller applications


**Function based views**
* REST framework provides two wrappers you can use to write API views.

* The @api_view decorator for working with function based views.
* The APIView class for working with class-based views.
* These wrappers provide a few bits of functionality such as making sure you receive Request instances in your view, and adding context to Response objects so that content negotiation can be performed.

* The wrappers also provide behaviour such as returning 405 Method Not Allowed responses when appropriate, and handling any ParseError exceptions that occur when accessing request.data with malformed input.






