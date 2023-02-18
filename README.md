<h1 style="color: #132A43; text-align: center">School Manager CX</h1>

### Project description

This project has an API developed in Python with the help of the Django framework, and an interface developed in React.js. As the name suggests, this is an application to be used by a school to manage students. [Access the INTERFACE repository by clicking here](https://github.com/renandcr/konia_project_interface).

<br>

<!-- ![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/renandcr/konia_project)
![Python version](https://img.shields.io/badge/python-3.10.4-yellow)
![Ubuntu version](https://img.shields.io/badge/ubuntu-20.04.5-green)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/renandcr/konia_project)
![GitHub repo size](https://img.shields.io/github/repo-size/renandcr/konia_project)
![GitHub top language](https://img.shields.io/github/languages/top/renandcr/konia_project)
![GitHub language count](https://img.shields.io/github/languages/count/renandcr/konia_project)
![GitHub](https://img.shields.io/github/license/renandcr/konia_project) -->

<br>

### Project status 👨‍💻 under development!

<br>

### Index

- [🛠️ Technologies used](#️-technologies-used)
- [🗺️ Diagram ER](#️-diagram-er)
- [📜 Documentation](#-documentation)
  - [Base URL](#base-url)
  - [School](#school)
    - [1 - Endpoints](#1---endpoints)
  - [Student](#student)
    - [2 - Endpoints](#2---endpoints)
  - [Course](#course)
    - [3 - Endpoints](#3---endpoints)
  - [User](#user)
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

<br>

## 🗺️ Diagram ER

<h4><img alt="Diagrama" src="assets/images/diagram_school_manager.png" style="border-radius: 4px"/></h4>

<br>

## 📜 Documentation

<br>

### Base URL

http://localhost:8000 - (tip: add an endpoint at the end)

<br>

### School

#### 1 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/school | Create school. |
| GET | /school_manager/school | Get schools. |
| PATCH | /school_manager/school/< school_id > | Update school. |
| DELETE | /school_manager/school/< school_id > | Delete school. |

<br>

<h3>👉 /school_manager/school - Create school</h3>

[back to Endpoints](#1---endpoints)

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

[back to Endpoints](#1---endpoints)

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
    "id": "34027f3a-10c9-4989-83a9-a62be44f2094",
    "name": "Cristóvão Colombo",
    "email": "cristovao_colombo_madureira@gmail.com",
    "zip_code": "84556213",
    "state": "PR",
    "city": "Curitiba",
    "street": "Madureira",
    "district": "Centro",
    "number": "1560",
    "phone": "41998935366",
    "created_at": "2023-02-15T13:54:24.854484Z"
  },
  {
    "id": "e9b81859-8adb-41e4-bb60-f58d77457177",
    "name": "Cristóvão Colombo",
    "email": "cristovao_colombo_dondocas@gmail.com",
    "zip_code": "86542133",
    "state": "PR",
    "city": "Maringá",
    "street": "Dondocas",
    "district": "Centro",
    "number": "1560",
    "phone": "44991934477",
    "created_at": "2023-02-15T13:55:10.946222Z"
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

<h3>👉 /school_manager/school/< school_id > - Update school</h3>

[back to Endpoints](#1---endpoints)

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

[back to Endpoints](#1---endpoints)

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

### Student

#### 2 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/student/< school_id > | Create student. |
| GET | /school_manager/student/< school_id > | Get students. |
| GET | /school_manager/student/< school_id >/< student_id > | Get student profile. |
| PATCH | /school_manager/student/< school_id >/< student_id > | Update student. |
| DELETE | /school_manager/student/< school_id >/< student_id > | Delete student. |

<br>

<h3>👉 /school_manager/student/< school_id > - Create student</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
POST /school_manager/student/< school_id >
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
  "first_name": "Tobias",
  "last_name": "Almeida Ramos",
  "email": "tobias@gmail.com",
  "date_of_birth": "13/06/1990",
  "cpf": "07568875950",
  "phone": "43996935598",
  "gender": "masculino"
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
  "id": "8bb2e07d-3091-4a04-a50a-e4027bdde1af",
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

<h3>👉 /school_manager/student/< school_id > - Get students</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
GET /school_manager/student/< school_id >
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
    "id": "463cb423-17ea-4569-9e72-d63dfd932fa6",
    "first_name": "Karina",
    "last_name": "Bastos de Melo",
    "email": "karina@gmail.com",
    "date_of_birth": "22/09/1998",
    "cpf": "07568827788",
    "phone": "43996935577",
    "gender": "feminino",
    "date_joined": "2023-02-17T23:20:29.433530Z",
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

<h3>👉 /school_manager/student/< school_id >/< student_id > - Get student profile</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
GET /school_manager/student/< school_id >/< student_id >
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
  "id": "463cb423-17ea-4569-9e72-d63dfd932fa6",
  "first_name": "Karina",
  "last_name": "Bastos de Melo",
  "email": "karina@gmail.com",
  "date_of_birth": "22/09/1998",
  "cpf": "07568827788",
  "phone": "43996935577",
  "gender": "feminino",
  "date_joined": "2023-02-17T23:20:29.433530Z",
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

<h3>Response returned for school or student not found</h3>

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

<h3>👉 /school_manager/student/< school_id >/< student_id > - Update student</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/student/< school_id >/< student_id >
Host: localhost:8000
Content-type: aplication/json
Authorization: Bearer token
```

<h3>Request body</h3>

```json
{
  "email": "karina_bastos@gmail.com",
  "phone": "43996935599"
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
  "id": "463cb423-17ea-4569-9e72-d63dfd932fa6",
  "first_name": "Karina",
  "last_name": "Bastos de Melo",
  "email": "karina_bastos@gmail.com",
  "date_of_birth": "22/09/1998",
  "cpf": "07568827788",
  "phone": "43996935599",
  "gender": "feminino",
  "date_joined": "2023-02-17T23:20:29.433530Z",
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

<h3>Response returned for school or student not found</h3>

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

<h3>👉 /school_manager/student/< school_id >/< student_id > - Delete student</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/student/< school_id >/< student_id >
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

<h3>Response returned for school or student not found</h3>

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

| Method | Route                                              | Description    |
| ------ | -------------------------------------------------- | -------------- |
| POST   | /school_manager/course/< school_id >               | Create course. |
| GET    | /school_manager/course/< school_id >               | Get courses.   |
| GET    | /school_manager/course/< school_id >/< course_id > | Get a course.  |
| PATCH  | /school_manager/course/< school_id >/< course_id > | Update course. |
| DELETE | /school_manager/course/< school_id >/< course_id > | Delete course. |

<br>

<h3>👉 /school_manager/course/< school_id > - Create course </h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
POST /school_manager/course/< school_id >
Host: localhost:8000
Content-type: application/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "name": "JavaScript",
  "description": "Desenvolvimento de aplicações web."
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
  "id": 1,
  "name": "JavaScript",
  "description": "Desenvolvimento de aplicações web.",
  "created_at": "2023-02-05T23:41:52.908114Z",
  "school_id": "1"
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

<h3>👉 /school_manager/course/< school_id > - Get courses</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
GET /school_manager/course/< school_id >
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
    "id": 1,
    "name": "JavaScript",
    "description": "Desenvolvimento de aplicações web.",
    "created_at": "2023-02-05T23:41:52.908114Z",
    "school_id": "1"
  },
  {
    "id": 2,
    "name": "HTML",
    "description": "Linguagem de Marcação de HiperTexto para desenvolvimento de aplicações web.",
    "created_at": "2023-02-05T23:41:52.908114Z",
    "school_id": "1"
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

<h3>👉 /school_manager/course/< school_id >/< course_id > - Get a course</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
GET /school_manager/course/< school_id >/< course_id >
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
    "id": 1,
    "name": "JavaScript",
    "description": "Desenvolvimento de aplicações web.",
    "created_at": "2023-02-05T23:41:52.908114Z",
    "school_id": "1"
  },
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

<h3>👉 /school_manager/course/< school_id >/< course_id > - Update course

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/course/< school_id >/< course_id >
Host: localhost:8000
Content-type: aplication/json
Authorization: Bearer token
```

<h3>Request body</h3>

```json
{
  "description": "O JavaScript é uma das mais importantes tecnologias voltadas para o front-end. Trata-se de uma linguagem de programação que permite implementar itens complexos em páginas web."
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
  "id": 1,
  "description": "O JavaScript é uma das mais importantes tecnologias voltadas para o front-end. Trata-se de uma linguagem de programação que permite implementar itens complexos em páginas web.",
  "created_at": "2023-02-05T23:41:52.908114Z",
  "school_id": "1"
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

<h3>👉 /school_manager/course/< school_id >/< course_id > - Delete course</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/course/< school_id >/< course_id >
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

### User

#### 4 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/user/< school_id > | Create user. |
| POST | /school_manager/login | Login. |
| GET | /school_manager/user/< school_id > | Get all users registered in a given school |
| PATCH | /school_manager/user/< school_id >/< employee_id > | Update user. |
| DELETE | /school_manager/user/< school_id >/< employee_id > | Delete user. |

<br>

<h3>👉 /school_manager/user/< school_id > - Create user</h3>

[back to Endpoints](#4---endpoints)

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

[back to Endpoints](#4---endpoints)

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

<h3>👉 /school_manager/user/< school_id > - Get all users registered in a given school</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
GET /school_manager/user/< school_id >
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

<h3>👉 /school_manager/user/< school_id >/< user_id > - Update user</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/user/< school_id >/< user_id >
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

<h3>Response returned for user or school not found</h3>

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

<h3>👉 /school_manager/user/< school_id >/< user_id > - Delete user</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/user/< school_id >/< user_id >
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

<h3>Response returned for user or school not found</h3>

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
| DELETE | /school_manager/address/< address_id >/< student_id > | Delete address. |

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

Licensed under [MIT]().
