'''
API - Application Programming Interface - is a way for computer programs to communicate with each other.

It's like a waiter in a restaurant - it brings you the food you ordered.

Main API interactions:
Endpoints - URLs that represent specific resources
HTTP Methods - GET, POST, PUT, DELETE, etc. 
Headers - Additional information about the request (e.g. type of content, authorization, etc.)
Body - The body of the request (usually JSON for REST APIs)
Response body - The response body from the API/server (JSON, XML, etc.)
Status Codes - 200 OK, 404 Not Found, 500 Internal Server Error, etc.

HTTP methods:
GET - Retrieve data from the server
POST - Create a new resource on the server
PUT - Update an existing resource on the server
DELETE - Delete a resource on the server

Status codes:
2xx - Success
3xx - Redirection
4xx - Client Error
5xx - Server Error
For testing it's important not only look at the status code, but also the response body.
Because the status code doesn't always mean that the request was successful.

Headers are used to provide additional information about the request.
Content type: application/json - means that the request body is in JSON format (there can be other types like application/xml, application/text, etc.)
Authorization: Bearer <token> - means that the request is authorized with a token
Accept: application/json - means that the client accepts the response in JSON format (there can be other types like application/xml, application/text, etc.)
Content-Type: application/json - means that the request body is in JSON format (there can be other types like application/xml, application/text, etc.)
Content-Length: 100 - means that the request body is 100 bytes long
Cache-Control: no-cache - means that the response should not be cached

Autorization and security:
API keys - a unique identifier for the API what you send in the header of the request or in params of the request
Bearer tokens - a unique identifier for the API what you send in the header of the request or in params of the request
Basic authentication - a username and password for the API
CORS - Cross-Origin Resource Sharing - a security feature that allows or restricts resources on a web page to be requested from another domain

Useful information:

Pagination - a technique to limit the number of results returned by the API
Filtering - a technique to filter the results returned by the API
Sorting - a technique to sort the results returned by the API
Validation - a technique to validate the data sent to the API
JSON Schema / OpenAPI - formal specification of the API (shows what data is expected an in what format)
Logs and tracing - records of requests and responses, statuses and errors -  useful for debugging and monitoring
Retry / backoff - in temporary errors (e.g. 500 Internal Server Error) we can retry the request after a certain amount of time

Tools:
Postman / Insomnia - GUI-tools for sending requests and testing APIs
curl/httpie - command line tools for sending requests and checking responses
requests (Python) - library for sending requests and checking responses HTTP
fetch / axios (JS) - libraries for sending requests and checking responses HTTP in browser/Node.js
FastAPI / Flask / Express - frameworks for building APIs in Python/JS
Swagger / OpenAPI - tools for documenting and specifying APIs






'''