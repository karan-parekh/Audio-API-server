# Audio API server
This application is a demonstration of a backend-file-management system using [Django REST framework](https://www.django-rest-framework.org/)

# Index
- Installation
- API Overview
- Testing


# Installation
1. Clone the repository to local machine
2. Create and activate a new venv
3. Install requirements `pip install -r requirements.txt`
4. Migrate migrations `python src/manage.py migrate`
5. Run server `python src/manage.py runserver`

# API Overview
**Visit `http://localhost:8000/api/` in your browser** 
## 1. API root
### Request
```
GET  /api/
```
### Response
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept {  
"song":  "http://localhost:8000/api/song/",
"podcast":  "http://localhost:8000/api/podcast/", 
"audiobook":  "http://localhost:8000/api/audiobook/"  
}
```
## 2. List API
### Request 
```
GET /api/<audioFileType>/
```
**Response:** List of all files in JSON
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
	{  
		"field": "value",
		"field": "value",
		...
	},
	{  
		"field": "value",
		"field": "value",
		...
	}
]
```

## 3. Retrieve API
### Request
```
GET /api/<audioFileType>/<audioFileID>/
```
**Reponse:**
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{  
	"field": "value",
	"field": "value",
	...
}
```


## 4. Create API
### Request
```
POST /api/<audioFileType>/
{  
	"field": "value",
	"field": "value",
	...
}
```
**Reponse:**
```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{  
	"field": "value",
	"field": "value",
	...
}
```

## 5. Delete API
### Request
```
DELETE  /api/<audioFileType>/<audioFileID>/
```
### Response
```
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

## Update API
### Request
```
PATCH  /api/<audioFileType>/<audioFileID>/
{
    "field": "new value",
}
```
### Response
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{  
	"field": "new value",
	"field": "value",
	...
}
```

# Testing
To run all tests run command `python src/manage.py test` in project directory
