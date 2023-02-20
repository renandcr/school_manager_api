<h1 style="color: #132A43; text-align: center">School Manager CX</h1>

### Project description

This project has an API developed in Python with the help of the Django framework, and an interface developed in React.js. As the name suggests, this is an application to be used by a school for student management. [Access the INTERFACE repository by clicking here]().

<br>

![Python version](https://img.shields.io/badge/python-3.11.2-yellow)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/renandcr/school_manager_api)
![Ubuntu version](https://img.shields.io/badge/ubuntu-20.04.5-green)
![GitHub repo directory count](https://img.shields.io/github/directory-file-count/renandcr/school_manager_api)
![GitHub repo size](https://img.shields.io/github/repo-size/renandcr/school_manager_api)
![GitHub top language](https://img.shields.io/github/languages/top/renandcr/school_manager_api)
![GitHub](https://img.shields.io/github/license/renandcr/school_manager_api)

<br>

### Project status 👨‍💻 under development!

<br>

### Index

- [🛠️ Technologies used](#️-technologies-used)
- [🗺️ Diagram ER](#️-diagram-er)
- [📜 Documentation](#-documentation)
  - [Base URL](#base-url)
  - [User](#user)
    - [1 - Endpoints](#1---endpoints)
  - [School](#school)
    - [2 - Endpoints](#2---endpoints)
  - [Course](#course)
    - [3 - Endpoints](#3---endpoints)
  - [Student](#student)
    - [4 - Endpoints](#4---endpoints)
  - [Address](#address)
    - [5 - Endpoints](#5---endpoints)
- [Author](#author)
- [License](#license)

<br>

## 🛠️ Technologies used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django Rest Framework Simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

<br>

## 🗺️ Diagram ER

<h4><img alt="Diagrama" src="assets/images/diagram_school_manager.png" style="border-radius: 4px"/></h4>

<br>

## 📜 Documentation

<br>

### Base URL

http://localhost:8000 - (tip: add an endpoint at the end)

<br>

### User

#### 1 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/user/< school_id > | Create user. |
| POST | /school_manager/login | Login. |
| GET | /school_manager/user/get/< school_id >/ | Get all users registered in a given school. |
| PATCH | /school_manager/user/< user_id > | Update user. |
| DELETE | /school_manager/user/< user_id > | Delete user. |
| PATCH | /school_manager/user/< school_id >/< user_email > | Link a school to a user. |

<br>

<h3>👉 /school_manager/user/< school_id > - Create user</h3>

[back to Endpoints](#1---endpoints)

<h3>Request information</h3>

```
POST /school_manager/user/< school_id >
Host: localhost:8000
Content-type: application/json
```

<h3>Request body</h3>

```json
{
  "first_name": "Claudia",
  "last_name": "Amaral",
  "email": "claudia@gmail.com",
  "username": "claudia",
  "password": "123456"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
201 Created
```

```json
{
  "first_name": "Claudia",
  "last_name": "Amaral",
  "email": "claudia@gmail.com",
  "username": "claudia",
  "date_joined": "2023-02-17T12:29:35.729253Z",
  "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
}
```

<br>

<h3>Response returned for school not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>Response returned if there is the same email registered in the database</h3>

Status code

```
400 Bad Request
```

```json
{
  "email": ["user with this email already exists."]
}
```

<br>

<h3>👉 /school_manager/login - Login</h3>

[back to Endpoints](#1---endpoints)

<h3>Request information</h3>

```
POST /school_manager/login
Host: localhost:8000
Content-type: application/json
```

<h3>Request body</h3>

```json
{
  "email": "claudia@gmail.com",
  "password": "123456"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NjcyMzgwMSwiaWF0IjoxNjc2NjM3NDAxLCJqdGkiOiJhYmQ1YzJmYmEzNWY0MzMyYjVhNDMzZTFmM2Q4Yzg5NiIsInVzZXJfaWQiOiI5NGNhN2IyMS1hYjI4LTRjYjktYmQxYS05NmNkOTk0NTkwNzYifQ.Atwj2AHkKQ8M4s9F0HLoT-FYKhE4afoilN5JMP-fNVQ",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc2NjM3NzAxLCJpYXQiOjE2NzY2Mzc0MDEsImp0aSI6Ijk0ZDkwZDkyZmY0MzQ5OTg4YTg4NjFiYjEyZmRiNzExIiwidXNlcl9pZCI6Ijk0Y2E3YjIxLWFiMjgtNGNiOS1iZDFhLTk2Y2Q5OTQ1OTA3NiJ9.ROJj0Vh7Z5RL1jIvOPazp9nIPd2u3FhpbwwRSwMYulc"
}
```

<br>

<h3>Response returned for incorrect email or password</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "No active account found with the given credentials"
}
```

<br>

<h3>👉 /school_manager/user/get/< school_id >/ - Get all users registered in a given school</h3>

[back to Endpoints](#1---endpoints)

<h3>Request information</h3>

```
GET /school_manager/user/get/< school_id >/
Host: localhost:8000
Authorization: Bearer token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
[
  {
    "first_name": "Claudia",
    "last_name": "Amaral",
    "email": "claudia@gmail.com",
    "username": "claudia",
    "date_joined": "2023-02-17T12:29:35.729253Z",
    "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
  },
  {
    "first_name": "Fabiano",
    "last_name": "Almeida",
    "email": "fabiano@gmail.com",
    "username": "fabiano",
    "date_joined": "2023-02-17T12:45:51.462795Z",
    "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
  }
]
```

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for school not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/user/< user_id > - Update user</h3>

[back to Endpoints](#1---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/user/< user_id >
Host: localhost:8000
Content-type: aplication/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "email": "claudia_amaral@gmail.com"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
{
  "id": "94ca7b21-ab28-4cb9-bd1a-96cd99459076",
  "first_name": "Claudia",
  "last_name": "Amaral",
  "email": "claudia_amaral@gmail.com",
  "username": "claudia",
  "date_joined": "2023-02-17T12:29:35.729253Z",
  "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for user not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/user/< user_id > - Delete user</h3>

[back to Endpoints](#1---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/user/< user_id >
Host: localhost:8000
Authorization: Bearer token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
204 No Content
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for user not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/user/< school_id >/< user_email > - Link a school to a user</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/user/< school_id >/< user_email >
Host: localhost:8000
Authorization: Bearer token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
{
  "id": "ea1d272d-7a24-453a-b253-31b96edb1910",
  "first_name": "Leonardo",
  "last_name": "Pereira",
  "email": "leonardo@gmail.com",
  "username": "leonardo",
  "date_joined": "2023-02-20T21:58:33.188324Z",
  "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for school or user not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

### School

#### 2 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/school | Create school. |
| GET | /school_manager/school | Get schools. |
| GET | /school_manager/school< school_id > | Get a school. |
| PATCH | /school_manager/school/< school_id > | Update school. |
| DELETE | /school_manager/school/< school_id > | Delete school. |

<br>

<h3>👉 /school_manager/school - Create school</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
POST /school_manager/school
Host: localhost:8000
Content-type: application/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "name": "Cristóvão Colombo",
  "email": "cristovao_colombo_madureira@gmail.com",
  "zip_code": "84556213",
  "state": "PR",
  "city": "Curitiba",
  "street": "Madureira",
  "district": "Centro",
  "number": "1560",
  "phone": "41998935366"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
201 Created
```

```json
{
  "id": "a9249e36-9cbb-40d9-8eff-62da479a1446",
  "name": "Cristóvão Colombo",
  "email": "cristovao_colombo_madureira@gmail.com",
  "zip_code": "84556213",
  "state": "PR",
  "city": "Curitiba",
  "street": "Madureira",
  "district": "Centro",
  "number": "1560",
  "phone": "41998935366",
  "created_at": "2023-02-15T13:20:52.369426Z"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned if there is the same email registered in the database</h3>

Status code

```
400 Bad Request
```

```json
{
  "error": {
    "email": ["school with this email already exists."]
  }
}
```

<br>

<h3>👉 /school_manager/school - Get schools</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
GET /school_manager/school
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
[
  {
    "id": "c1d62c6f-5154-4789-a6a0-bac781e6aa58",
    "name": "Cristóvão Colombo",
    "email": "cristovao_colombo_dondocas@gmail.com",
    "zip_code": "86542133",
    "state": "PR",
    "city": "Maringá",
    "street": "Dondocas",
    "district": "Centro",
    "number": "1560",
    "phone": "44991934477",
    "created_at": "2023-02-16T23:57:00.757650Z"
  },
  {
    "id": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be",
    "name": "Cristóvão Colombo",
    "email": "cristovao_colombo_madureira@gmail.com",
    "zip_code": "86542589",
    "state": "PR",
    "city": "Curitiba",
    "street": "Madureira",
    "district": "Centro",
    "number": "3650",
    "phone": "44991934445",
    "created_at": "2023-02-16T23:57:54.340493Z"
  },
  {
    "id": "47375339-2546-4826-95e0-68ceff325f63",
    "name": "Cristóvão Colombo",
    "email": "cristovao_colombo_dale_carnegie@gmail.com",
    "zip_code": "84599777",
    "state": "PR",
    "city": "Londrina",
    "street": "Dale Carnegie",
    "district": "Centro",
    "number": "6533",
    "phone": "43991938877",
    "created_at": "2023-02-19T00:56:30.199970Z"
  }
]
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>
####################################
<h3>👉 /school_manager/school< school_id > - Get a school</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
GET /school_manager/school< school_id >
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
{
  "id": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be",
  "name": "Cristóvão Colombo",
  "email": "cristovao_colombo_madureira@gmail.com",
  "zip_code": "86542589",
  "state": "PR",
  "city": "Curitiba",
  "street": "Madureira",
  "district": "Centro",
  "number": "3650",
  "phone": "44991934445",
  "created_at": "2023-02-16T23:57:54.340493Z"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for school not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/school/< school_id > - Update school</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/school/< school_id >
Host: localhost:8000
Content-type: application/json
Authorization: Bearer Token
```

<br>

<h3>Request body</h3>

```json
{
  "email": "cristovao_colombo_madureira_2@gmail.com"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
{
  "id": "4c808757-a504-4168-93b2-847dbbd39ca2",
  "name": "Cristóvão Colombo",
  "email": "cristovao_colombo_madureira_2@gmail.com",
  "zip_code": "84556213",
  "state": "PR",
  "city": "Curitiba",
  "street": "Madureira",
  "district": "Centro",
  "number": "1560",
  "phone": "41998935366",
  "created_at": "2023-02-15T14:02:58.579198Z"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for no results found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/school/< school_id > - Delete school</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/school/< school_id >
Host: localhost:8000
Authorization: Bearer token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
204 No Content
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for no results found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

### Course

#### 3 - Endpoints

[back to index](#index)

| Method | Route                                                   | Description            |
| ------ | ------------------------------------------------------- | ---------------------- |
| POST   | /school_manager/course/create/< school_id >             | Create course.         |
| GET    | /school_manager/course/get/< school_id >                | Get courses.           |
| GET    | /school_manager/course/< course_id >                    | Get a course.          |
| PATCH  | /school_manager/course/< course_id >                    | Update course.         |
| DELETE | /school_manager/course/< course_id >                    | Delete course.         |
| POST   | /school_manager/course/add/< course_id >/< student_id > | Add student to course. |

<br>

<h3>👉 /school_manager/course/create/< school_id > - Create course </h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
POST /school_manager/course/create/< school_id >
Host: localhost:8000
Content-type: application/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "name": "JavaScript",
  "description": "Linguagem de programação com foco em desenvolvimento de aplicações web."
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
201 Created
```

```json
{
  "id": "4c6463ce-4203-4dfe-b0b6-10b899984656",
  "name": "JavaScript",
  "description": "Linguagem de programação com foco em desenvolvimento de aplicações web.",
  "created_at": "2023-02-18T23:37:10.589959Z",
  "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be",
  "students": []
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for school not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>Response returned if the course name already exists in the database</h3>

Status code

```
400 Bad Request
```

```json
{
  "name": ["course with this name already exists."]
}
```

<br>

<h3>👉 /school_manager/course/get/< school_id > - Get courses</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
GET /school_manager/course/get/< school_id >
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
[
  {
    "id": "710258b8-a6b9-4141-b085-608dfc32e1fd",
    "name": "JavaScript",
    "description": "Linguagem de programação com foco em desenvolvimento de aplicações web.",
    "created_at": "2023-02-18T23:39:22.462854Z",
    "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be",
    "students": []
  },
  {
    "id": "e719f81b-19d5-4197-9e30-6d9c83de6a1b",
    "name": "HTML",
    "description": "Linguagem de Marcação para desenvolvimento de aplicações web.",
    "created_at": "2023-02-18T23:48:52.269868Z",
    "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be",
    "students": []
  }
]
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for school not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/course/< course_id > - Get a course</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
GET /school_manager/course/< course_id >
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
{
  "id": "e719f81b-19d5-4197-9e30-6d9c83de6a1b",
  "name": "HTML5",
  "description": "Linguagem de Marcação para desenvolvimento de aplicações web.",
  "created_at": "2023-02-18T23:48:52.269868Z",
  "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be",
  "students": []
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for course not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/course/< course_id > - Update course

<br>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/course/< course_id >
Host: localhost:8000
Content-type: aplication/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "name": "HTML5"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

<br>

```json
{
  "id": "e719f81b-19d5-4197-9e30-6d9c83de6a1b",
  "name": "HTML5",
  "description": "Linguagem de Marcação para desenvolvimento de aplicações web.",
  "created_at": "2023-02-18T23:48:52.269868Z",
  "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be",
  "students": []
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for course not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/course/< course_id > - Delete course</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/course/< course_id >
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
204 No Content
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for course not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/course/add/< course_id >/< student_id > - Add student to course</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
POST /school_manager/course/add/< course_id >/< student_id >
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
{
  "id": "710258b8-a6b9-4141-b085-608dfc32e1fd",
  "name": "JavaScript",
  "description": "Linguagem de programação com foco em desenvolvimento de aplicações web.",
  "created_at": "2023-02-18T23:39:22.462854Z",
  "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be",
  "students": ["8bb2e07d-3091-4a04-a50a-e4027bdde1af"]
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for course or student not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

### Student

#### 4 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/student/create/< school_id > | Create student. |
| GET | /school_manager/student/get/< school_id > | Get students. |
| GET | /school_manager/student/< student_id > | Get student profile. |
| PATCH | /school_manager/student/< student_id > | Update student. |
| DELETE | /school_manager/student/< student_id > | Delete student. |

<br>

<h3>👉 /school_manager/student/create/< school_id > - Create student</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
POST /school_manager/student/create/< school_id >
Host: localhost:8000
Content-type: application/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```
In the 'gender' field, the possible options are: masculino, feminino, lgbt or outro.
```

```json
{
  "first_name": "Bernardo",
  "last_name": "Alves",
  "email": "bernardo@gmail.com",
  "date_of_birth": "23/07/2001",
  "cpf": "07568827777",
  "phone": "43996935456",
  "gender": "lgbt"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
201 Created
```

```json
{
  "id": "a186890d-24d9-483c-82d8-d95df91039e4",
  "address": null,
  "first_name": "Bernardo",
  "last_name": "Alves",
  "email": "bernardo@gmail.com",
  "date_of_birth": "23/07/2001",
  "cpf": "07568827777",
  "phone": "43996935456",
  "gender": "lgbt",
  "date_joined": "2023-02-19T01:07:23.513467Z",
  "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned if gender field is submitted incorrectly</h3>

Status code

```
400 Bad Request
```

```json
{
  "gender": ["\"masculin\" is not a valid choice."]
}
```

<br>

<h3>Response returned for school not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>Response returned for e-mail and cpf fields already existing in the database</h3>

Status code

```
400 Bad Request
```

```json
{
  "email": ["student with this email already exists."],
  "cpf": ["student with this cpf already exists."]
}
```

<br>

<h3>👉 /school_manager/student/get/< school_id > - Get students</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
GET /school_manager/student/get/< school_id >
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
[
  {
    "id": "8bb2e07d-3091-4a04-a50a-e4027bdde1af",
    "address": "ca929dce-cbfe-4af8-819a-a0d8db287065",
    "first_name": "Tobias",
    "last_name": "Almeida Ramos",
    "email": "tobias@gmail.com",
    "date_of_birth": "13/06/1990",
    "cpf": "07568875950",
    "phone": "43996935598",
    "gender": "masculino",
    "date_joined": "2023-02-17T22:51:23.066638Z",
    "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
  },
  {
    "id": "9f77c944-d537-4bb0-af23-1be85ebbdef6",
    "address": null,
    "first_name": "Karina",
    "last_name": "Bastos de Melo",
    "email": "karina@gmail.com",
    "date_of_birth": "22/09/1998",
    "cpf": "07568827788",
    "phone": "43996935577",
    "gender": "feminino",
    "date_joined": "2023-02-18T17:20:55.632551Z",
    "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
  },
  {
    "id": "a186890d-24d9-483c-82d8-d95df91039e4",
    "address": null,
    "first_name": "Bernardo",
    "last_name": "Alves",
    "email": "bernardo@gmail.com",
    "date_of_birth": "23/07/2001",
    "cpf": "07568827777",
    "phone": "43996935456",
    "gender": "lgbt",
    "date_joined": "2023-02-19T01:07:23.513467Z",
    "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
  }
]
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for school not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/student/< student_id > - Get student profile</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
GET /school_manager/student/< student_id >
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
{
  "id": "8bb2e07d-3091-4a04-a50a-e4027bdde1af",
  "address": "ca929dce-cbfe-4af8-819a-a0d8db287065",
  "first_name": "Tobias",
  "last_name": "Almeida Ramos",
  "email": "tobias@gmail.com",
  "date_of_birth": "13/06/1990",
  "cpf": "07568875950",
  "phone": "43996935598",
  "gender": "masculino",
  "date_joined": "2023-02-17T22:51:23.066638Z",
  "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for student not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/student/< student_id > - Update student</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/student/< student_id >
Host: localhost:8000
Content-type: aplication/json
Authorization: Bearer token
```

<h3>Request body</h3>

```json
{
  "email": "bernardo_alves@gmail.com"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

<br>

```json
{
  "id": "1b8fa597-785d-4eda-8928-38b428f8bcc1",
  "address": null,
  "first_name": "Bernardo",
  "last_name": "Alves",
  "email": "bernardo_alves@gmail.com",
  "date_of_birth": "23/07/2001",
  "cpf": "07568827777",
  "phone": "43996935456",
  "gender": "lgbt",
  "date_joined": "2023-02-19T01:26:59.035034Z",
  "school": "6e7642c7-bd7d-47c6-b4d0-adbb39d735be"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for student not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/student/< student_id > - Delete student</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/student/< student_id >
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
204 No Content
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for student not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

### Address

#### 5 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/address/create/< student_id > | Create address. |
| GET | /school_manager/address/< address_id >| Get a address. |
| PATCH | /school_manager/address/< address_id > | Update address. |
| DELETE | /school_manager/address/< address_id >| Delete address. |

<br>

<h3>👉 /school_manager/address/create/< student_id > - Create address</h3>

[back to Endpoints](#5---endpoints)

<h3>Request information</h3>

```
POST /school_manager/address/create/< student_id >
Host: localhost:8000
Content-type: application/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "zip_code": "84555667",
  "state": "PR",
  "city": "Curitiba",
  "street": "Fernando Pessoa",
  "district": "São Gonçalves",
  "number": "3550"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
201 Created
```

```json
{
  "id": "15661bd0-34fc-40f3-92b0-e2943b10e3da",
  "zip_code": "84555667",
  "state": "PR",
  "city": "Curitiba",
  "street": "Fernando Pessoa",
  "district": "São Gonçalves",
  "number": "3550",
  "date_joined": "2023-02-18T17:22:06.705045Z",
  "student": "9f77c944-d537-4bb0-af23-1be85ebbdef6"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned if the student already has a registered address</h3>

Status code

```
400 Bad Request
```

```json
{
  "student": ["address with this student already exists."]
}
```

<br>

<h3>Response returned for student not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/address/< address_id > - Get a address</h3>

[back to Endpoints](#5---endpoints)

<h3>Request information</h3>

```
GET /school_manager/address/< address_id >
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
{
  "id": "ca929dce-cbfe-4af8-819a-a0d8db287065",
  "zip_code": "85444777",
  "state": "PR",
  "city": "Curitiba",
  "street": "Iguaçu",
  "district": "Água azul",
  "number": "5588",
  "date_joined": "2023-02-18T16:42:21.385939Z",
  "student": "8bb2e07d-3091-4a04-a50a-e4027bdde1af"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for address not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/address/< address_id > - Update address</h3>

[back to Endpoints](#5---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/address/< address_id >
Host: localhost:8000
Content-type: aplication/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "street": "Iguaçu",
  "number": "5588"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
{
  "id": "ca929dce-cbfe-4af8-819a-a0d8db287065",
  "zip_code": "85444777",
  "state": "PR",
  "city": "Curitiba",
  "street": "Iguaçu",
  "district": "Água azul",
  "number": "5588",
  "date_joined": "2023-02-18T16:42:21.385939Z",
  "student": "8bb2e07d-3091-4a04-a50a-e4027bdde1af"
}
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for address not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

<h3>👉 /school_manager/address/< address_id > - Delete address</h3>

[back to Endpoints](#5---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/address/< address_id >
Host: localhost:8000
Authorization: Bearer Token
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
204 No Content
```

<br>

<h3>Response returned for unauthenticated user</h3>

Status code

```
401 Unauthorized
```

```json
{
  "detail": "Authentication credentials were not provided."
}
```

<br>

<h3>Response returned for address not found</h3>

Status code

```
404 Not Found
```

```json
{
  "detail": "Not found."
}
```

<br>

## Author

<h4><img alt="Foto de perfil" src="assets/images/profile_photo.JPG" style="width: 100px; border-radius: 50px"/></h4>
Renan Ribeiro 🚀

<br>

<br>

Made with ❤️ by Renan Ribeiro 👋 Get in touch!

![GMAIL](https://img.shields.io/badge/renandcribeiro@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)
<a href="https://www.linkedin.com/in/renandcr">
<img src="https://img.shields.io/badge/Renan-0077B5?style=flat-square&logo=linkedin&logoColor=white"/></a>

<br>

## License

Licensed under [MIT](https://github.com/renandcr/school_manager_api/new/development).
