<h1 style="color: #132A43; text-align: center">School Manager CX - API</h1>

### Project description

This project has an API developed in Python with the help of the Django framework, and an interface developed in React.js. School Manager CX is a school management platform where you can add new schools, enroll students, add courses, and add instructors and students to those courses. [Access the INTERFACE repository by clicking here](https://github.com/renandcr/school_manager_interface).

<br>

![Python version](https://img.shields.io/badge/python-3.11.2-yellow)
![Django version](https://img.shields.io/badge/django-4.1.7-green)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/renandcr/school_manager_api)
![GitHub language count](https://img.shields.io/github/languages/count/renandcr/school_manager_api)
![GitHub top language](https://img.shields.io/github/languages/top/renandcr/school_manager_api)
![GitHub repo size](https://img.shields.io/github/repo-size/renandcr/school_manager_api)
![GitHub repo directory count](https://img.shields.io/github/directory-file-count/renandcr/school_manager_api)
![GitHub](https://img.shields.io/github/license/renandcr/school_manager_api)

<br>

### 🖥️ Project status 🚀 In production! Access the website [here.](https://school-manager-interface.vercel.app/)

<br>

### Index

- [Technologies used](#️-technologies-used)
- [Auxiliary Tools](#auxiliary-tools)
- [Diagram ER](#️-diagram-er)
- [Documentation](#-documentation)
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

## Auxiliary Tools

- [Insomnia](https://insomnia.rest/)
- [Project Trello](https://trello.com/invite/b/ZhPBaw28/ATTI49e717feb94b1f616a16667ac4a286d0FB2C48B5/school-manager-cx)

<br>

## 🗺️ Diagram ER

<h4><img alt="Diagrama" src="assets/images/diagram_school_manager.png" style="border-radius: 4px"/></h4>

<br>

## 📜 Documentation

<br>

### Base URL

https://schoolmanagerapi-production.up.railway.app - (tip: add an endpoint at the end)

<br>

### User

#### 1 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/user | Create user. |
| POST | /school_manager/login | Login. |
| GET | /school_manager/user/get/< school_id >/ | Get all users registered in a given school. |
| PATCH | /school_manager/user/< user_id > | Update user. |
| DELETE | /school_manager/user/< user_id > | Delete user. |
| PATCH | /school_manager/user/< school_id >/< user_email > | Link a school to a user. |

<br>

<h3>👉 /school_manager/user - Create user</h3>

[back to Endpoints](#1---endpoints)

<h3>Request information</h3>

```
POST /school_manager/user
Host: localhost:8000
Content-type: application/json
```

<h3>Request body</h3>

```json
{
  "first_name": "Bruno",
  "last_name": "Pereira Bastos",
  "email": "bruno_pereira@gmail.com",
  "username": "Bruno Bastos",
  "role": "monitor(a) de ensino",
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
  "id": "7dc3e9dc-4d2f-4efb-80dd-0d5661032215",
  "first_name": "Bruno",
  "last_name": "Pereira Bastos",
  "email": "bruno_pereira@gmail.com",
  "username": "Bruno Bastos",
  "role": "monitor(a) de ensino",
  "date_joined": "2023-03-08T23:47:45.435387Z",
  "school": null
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
    "id": "160ff9ea-7289-4fb0-b51d-b5f3d99bf7db",
    "first_name": "Oscar",
    "last_name": "Wilde",
    "email": "oscar_wilde@gmail.com",
    "username": "Oscar Wilde",
    "role": "diretor(a)",
    "date_joined": "2023-03-04T21:55:33.052997Z",
    "school": "cd94916b-571b-4a6e-afa0-efe080861422"
  },
  {
    "id": "bf18613f-a78c-4ca1-8a05-6138d3a7aefc",
    "first_name": "André",
    "last_name": "Santos Da Costa",
    "email": "andre_costa@gmail.com",
    "username": "Andre Santos",
    "role": "instrutor(a) de ensino",
    "date_joined": "2023-03-08T13:48:42.317717Z",
    "school": "cd94916b-571b-4a6e-afa0-efe080861422"
  },
  {
    "id": "6a177046-1973-474f-ab31-c95faa1edc5d",
    "first_name": "Renata",
    "last_name": "Andretti Santana",
    "email": "renata_andretti@gmail.com",
    "username": "Renata Andretti",
    "role": "instrutor(a) de ensino",
    "date_joined": "2023-03-08T17:06:08.476909Z",
    "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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
  "email": "oscar_wilde@gmail.com",
  "role": "diretor(a)",
  "username": "Oscar Wilde"
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
  "id": "160ff9ea-7289-4fb0-b51d-b5f3d99bf7db",
  "first_name": "Oscar",
  "last_name": "Wilde",
  "email": "oscar_wilde@gmail.com",
  "username": "Oscar Wilde",
  "role": "diretor(a)",
  "date_joined": "2023-03-04T21:55:33.052997Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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
  "id": "160ff9ea-7289-4fb0-b51d-b5f3d99bf7db",
  "first_name": "Oscar",
  "last_name": "Wilde",
  "email": "oscar_wilde@gmail.com",
  "username": "Oscar Wilde",
  "role": "diretor(a)",
  "date_joined": "2023-03-04T21:55:33.052997Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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
  "branch": 3,
  "name": "Escola Cristóvão Colombo Madureira",
  "email": "cristovao_colombo_madureira@gmail.com",
  "zip_code": "86542589",
  "state": "PR",
  "city": "Curitiba",
  "street": "Madureira",
  "district": "Centro",
  "number": "3650",
  "phone": "44991934445"
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
  "id": "0dcddffb-d514-4024-a7f2-1ddbe7077add",
  "branch": "3",
  "name": "Escola Cristóvão Colombo Madureira",
  "email": "cristovao_colombo_madureira@gmail.com",
  "zip_code": "86542589",
  "state": "PR",
  "city": "Curitiba",
  "street": "Madureira",
  "district": "Centro",
  "number": "3650",
  "phone": "44991934445",
  "created_at": "2023-03-09T00:01:59.550638Z"
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
    "id": "cd94916b-571b-4a6e-afa0-efe080861422",
    "branch": "1",
    "name": "Escola Cristóvão Colombo Oswaldo Cruz",
    "email": "cristovao_colombo_oswaldo_cruz@gmail.com",
    "zip_code": "86800720",
    "state": "pr",
    "city": "Apucarana",
    "street": "Oswaldo Cruz",
    "district": "Centro",
    "number": "5468",
    "phone": "43999564185",
    "created_at": "2023-03-04T16:59:15.693756Z"
  },
  {
    "id": "1a707f7f-202d-49f7-8bd4-010ad81a5e6c",
    "branch": "2",
    "name": "Escola Cristóvão Colombo Piracicaba",
    "email": "cristovao_colombo_piracicaba@gmail.com",
    "zip_code": "85462321",
    "state": "pr",
    "city": "Maringá",
    "street": "Piracicaba",
    "district": "Centro",
    "number": "5263",
    "phone": "44996524365",
    "created_at": "2023-03-04T18:11:28.023295Z"
  },
  {
    "id": "0dcddffb-d514-4024-a7f2-1ddbe7077add",
    "branch": "3",
    "name": "Escola Cristóvão Colombo Madureira",
    "email": "cristovao_colombo_madureira@gmail.com",
    "zip_code": "86542589",
    "state": "PR",
    "city": "Curitiba",
    "street": "Madureira",
    "district": "Centro",
    "number": "3650",
    "phone": "44991934445",
    "created_at": "2023-03-09T00:01:59.550638Z"
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
  "id": "cd94916b-571b-4a6e-afa0-efe080861422",
  "branch": "1",
  "name": "Escola Cristóvão Colombo Oswaldo Cruz",
  "email": "cristovao_colombo_oswaldo_cruz@gmail.com",
  "zip_code": "86800720",
  "state": "pr",
  "city": "Apucarana",
  "street": "Oswaldo Cruz",
  "district": "Centro",
  "number": "5468",
  "phone": "43999564185",
  "created_at": "2023-03-04T16:59:15.693756Z"
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
  "phone": "44991938877"
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
  "id": "0dcddffb-d514-4024-a7f2-1ddbe7077add",
  "branch": "3",
  "name": "Escola Cristóvão Colombo Madureira",
  "email": "cristovao_colombo_madureira@gmail.com",
  "zip_code": "86542589",
  "state": "PR",
  "city": "Curitiba",
  "street": "Madureira",
  "district": "Centro",
  "number": "3650",
  "phone": "44991938877",
  "created_at": "2023-03-09T00:01:59.550638Z"
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

| Method | Route                                                          | Description                      |
| ------ | -------------------------------------------------------------- | -------------------------------- |
| POST   | /school_manager/course/create/< school_id >                    | Create course.                   |
| GET    | /school_manager/course/get/< school_id >                       | Get courses.                     |
| GET    | /school_manager/course/< course_id >                           | Get a course.                    |
| PATCH  | /school_manager/course/< course_id >                           | Update course.                   |
| DELETE | /school_manager/course/< course_id >                           | Delete course.                   |
| POST   | /school_manager/course/student/< course_id >/< student_email > | Add student to course.           |
| PATCH  | /school_manager/course/student/< course_id >/< student_email > | Remove student from a course.    |
| POST   | /school_manager/course/instructor/< course_id >/< user_email > | Add instructor to course.        |
| PATCH  | /school_manager/course/instructor/< course_id >/< user_email > | Remove instructor from a course. |

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
  "name": "Python",
  "description": "Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991."
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
  "id": "1157b984-3e1f-4a05-bfae-4f3adfc765b8",
  "students": [],
  "instructors": [],
  "name": "Python",
  "description": "Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.",
  "created_at": "2023-03-09T00:10:57.148024Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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
    "id": "5ed0f760-562b-4f7a-96c1-8958e724b42d",
    "students": [
      {
        "id": "9edd0ee1-566d-4bc8-8f43-cfd90e8b5f5c",
        "address": null,
        "first_name": "Alexandro",
        "last_name": "Paiva Vasconcelos",
        "email": "alex_paiva@gmail.com",
        "date_of_birth": "13/05/1994",
        "cpf": "07588897452",
        "phone": "43996521452",
        "gender": "masculino",
        "date_joined": "2023-03-04T17:12:13.446827Z",
        "school": "cd94916b-571b-4a6e-afa0-efe080861422"
      },
      {
        "id": "daf9a08c-362c-4550-9273-c89734c76cae",
        "address": null,
        "first_name": "Paula",
        "last_name": "Vieira Ventosa",
        "email": "paula_ventosa@gmail.com",
        "date_of_birth": "18/09/1996",
        "cpf": "07899632541",
        "phone": "44888526325",
        "gender": "feminino",
        "date_joined": "2023-03-04T18:17:53.569000Z",
        "school": "cd94916b-571b-4a6e-afa0-efe080861422"
      }
    ],
    "instructors": [
      {
        "id": "6a177046-1973-474f-ab31-c95faa1edc5d",
        "first_name": "Renata",
        "last_name": "Andretti Santana",
        "email": "renata_andretti@gmail.com",
        "username": "Renata Andretti",
        "role": "instrutor(a) de ensino",
        "date_joined": "2023-03-08T17:06:08.476909Z",
        "school": "cd94916b-571b-4a6e-afa0-efe080861422"
      },
      {
        "id": "bf18613f-a78c-4ca1-8a05-6138d3a7aefc",
        "first_name": "André",
        "last_name": "Santos Da Costa",
        "email": "andre_costa@gmail.com",
        "username": "Andre Santos",
        "role": "instrutor(a) de ensino",
        "date_joined": "2023-03-08T13:48:42.317717Z",
        "school": "cd94916b-571b-4a6e-afa0-efe080861422"
      }
    ],
    "name": "JavaScript",
    "description": "JavaScript é uma linguagem de programação interpretada estruturada, de script em alto nível com tipagem dinâmica fraca e multiparadigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web.",
    "created_at": "2023-03-04T18:18:51.534763Z",
    "school": "cd94916b-571b-4a6e-afa0-efe080861422"
  },
  {
    "id": "0dd3ba4c-0022-4a78-9140-1c5c928d3f1a",
    "students": [],
    "instructors": [],
    "name": "CSS3",
    "description": "Cascading Style Sheets é um mecanismo para adicionar estilos a uma página web, aplicado diretamente nas tags HTML ou ficar contido dentro das tags <style>. Também é possível, adicionar estilos adicionando um link para um arquivo CSS que contém os estilos.",
    "created_at": "2023-03-04T18:19:28.579401Z",
    "school": "cd94916b-571b-4a6e-afa0-efe080861422"
  },
  {
    "id": "4c541e97-3090-48d6-9768-fb21fd2162c6",
    "students": [],
    "instructors": [],
    "name": "HTML5",
    "description": "HTML é uma linguagem de marcação utilizada na construção de páginas na Web. Documentos HTML podem ser interpretados por navegadores. A tecnologia é fruto da junção entre os padrões HyTime e SGML.",
    "created_at": "2023-03-04T18:20:23.852259Z",
    "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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
  "id": "1157b984-3e1f-4a05-bfae-4f3adfc765b8",
  "students": [],
  "instructors": [],
  "name": "Python",
  "description": "Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.",
  "created_at": "2023-03-09T00:10:57.148024Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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
  "description": "Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991."
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
  "id": "1157b984-3e1f-4a05-bfae-4f3adfc765b8",
  "students": [],
  "instructors": [],
  "name": "Python",
  "description": "Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.",
  "created_at": "2023-03-09T00:10:57.148024Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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

<h3>👉 /school_manager/course/student/< course_id >/< student_email > - Add student to course</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
POST /school_manager/course/student/< course_id >/< student_email >
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
  "id": "1157b984-3e1f-4a05-bfae-4f3adfc765b8",
  "students": [
    {
      "id": "9edd0ee1-566d-4bc8-8f43-cfd90e8b5f5c",
      "address": null,
      "first_name": "Alexandro",
      "last_name": "Paiva Vasconcelos",
      "email": "alex_paiva@gmail.com",
      "date_of_birth": "13/05/1994",
      "cpf": "07588897452",
      "phone": "43996521452",
      "gender": "masculino",
      "date_joined": "2023-03-04T17:12:13.446827Z",
      "school": "cd94916b-571b-4a6e-afa0-efe080861422"
    }
  ],
  "instructors": [],
  "name": "Python",
  "description": "Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.",
  "created_at": "2023-03-09T00:10:57.148024Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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

<h3>👉 /school_manager/course/student/< course_id >/< student_email > - Remove student from a course.</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
POST /school_manager/course/student/< course_id >/< student_email >
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
  "id": "1157b984-3e1f-4a05-bfae-4f3adfc765b8",
  "students": [],
  "instructors": [],
  "name": "Python",
  "description": "Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.",
  "created_at": "2023-03-09T00:10:57.148024Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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

<h3>👉 /school_manager/course/instructor/< course_id >/< user_email > - Add instructor to course</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
POST /school_manager/course/instructor/< course_id >/< user_email >
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
  "id": "5ed0f760-562b-4f7a-96c1-8958e724b42d",
  "students": [],
  "instructors": [
    {
      "id": "6a177046-1973-474f-ab31-c95faa1edc5d",
      "first_name": "Renata",
      "last_name": "Andretti Santana",
      "email": "renata_andretti@gmail.com",
      "username": "Renata Andretti",
      "role": "instrutor(a) de ensino",
      "date_joined": "2023-03-08T17:06:08.476909Z",
      "school": "cd94916b-571b-4a6e-afa0-efe080861422"
    }
  ],
  "name": "JavaScript",
  "description": "JavaScript é uma linguagem de programação interpretada estruturada, de script em alto nível com tipagem dinâmica fraca e multiparadigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web.",
  "created_at": "2023-03-04T18:18:51.534763Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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

<h3>Response returned for course or user not found</h3>

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

<h3>👉 /school_manager/course/instructor/< course_id >/< user_email > - Remove instructor from a course.</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
POST /school_manager/course/instructor/< course_id >/< user_email >
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
  "id": "5ed0f760-562b-4f7a-96c1-8958e724b42d",
  "students": [],
  "instructors": [],
  "name": "JavaScript",
  "description": "JavaScript é uma linguagem de programação interpretada estruturada, de script em alto nível com tipagem dinâmica fraca e multiparadigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web.",
  "created_at": "2023-03-04T18:18:51.534763Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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

<h3>Response returned for course or user not found</h3>

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
  "id": "cf44dcc2-5646-4a68-b6b3-6ab182716e9c",
  "address": null,
  "first_name": "Bernardo",
  "last_name": "Alves",
  "email": "bernardo@gmail.com",
  "date_of_birth": "23/07/2001",
  "cpf": "07568827777",
  "phone": "43996935456",
  "gender": "lgbt",
  "date_joined": "2023-03-10T00:31:03.002566Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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
    "id": "9edd0ee1-566d-4bc8-8f43-cfd90e8b5f5c",
    "address": null,
    "first_name": "Alexandro",
    "last_name": "Paiva Vasconcelos",
    "email": "alex_paiva@gmail.com",
    "date_of_birth": "13/05/1994",
    "cpf": "07588897452",
    "phone": "43996521452",
    "gender": "masculino",
    "date_joined": "2023-03-04T17:12:13.446827Z",
    "school": "cd94916b-571b-4a6e-afa0-efe080861422"
  },
  {
    "id": "07887447-8576-41e5-8039-413dcf5ff149",
    "address": null,
    "first_name": "Angélica",
    "last_name": "Arruda De Melo",
    "email": "angelica_melo@gmail.com",
    "date_of_birth": "18/07/1996",
    "cpf": "07568895254",
    "phone": "43998521463",
    "gender": "feminino",
    "date_joined": "2023-03-04T18:15:13.860093Z",
    "school": "cd94916b-571b-4a6e-afa0-efe080861422"
  },
  {
    "id": "cf44dcc2-5646-4a68-b6b3-6ab182716e9c",
    "address": null,
    "first_name": "Bernardo",
    "last_name": "Alves",
    "email": "bernardo@gmail.com",
    "date_of_birth": "23/07/2001",
    "cpf": "07568827777",
    "phone": "43996935456",
    "gender": "lgbt",
    "date_joined": "2023-03-10T00:31:03.002566Z",
    "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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
  "id": "9edd0ee1-566d-4bc8-8f43-cfd90e8b5f5c",
  "address": null,
  "first_name": "Alexandro",
  "last_name": "Paiva Vasconcelos",
  "email": "alex_paiva@gmail.com",
  "date_of_birth": "13/05/1994",
  "cpf": "07588897452",
  "phone": "43996521452",
  "gender": "masculino",
  "date_joined": "2023-03-04T17:12:13.446827Z",
  "school": "cd94916b-571b-4a6e-afa0-efe080861422"
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

Licensed under [MIT](https://github.com/renandcr/school_manager_api/blob/development/LICENSE.md).
