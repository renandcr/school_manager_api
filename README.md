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
  - [Employee](#employee)
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
| PATCH | /school_manager/school/< int:school_id > | Update school. |
| DELETE | /school_manager/school/< int:school_id > | Delete school. |

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

<h3>👉 /school_manager/school/< int:school_id > - Update school</h3>

[back to Endpoints](#1---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/school/< int:school_id >
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

<h3>Response returned for invalid ID</h3>

Status code

```
400 Bad Request
```

```json
{
  "error": ["“4c808757-a504-4168-93b2-847dbbd39ca” is not a valid UUID."]
}
```

<br>

<br>

<h3>Response returned for no results found</h3>

Status code

```
404 Not Found
```

```json
{
  "error": ["No results for 4c808757-a504-4168-93b2-847dbbd39ca4"]
}
```

<br>

<h3>👉 /school_manager/school/< int:school_id > - Delete school</h3>

[back to Endpoints](#1---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/school/< int:school_id >
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

<h3>Response returned for no results found</h3>

Status code

```
404 Not Found
```

```json
{
  "error": ["No results for 4c808757-a504-4168-93b2-847dbbd39ca4"]
}
```

<br>

<h3>Response returned for invalid ID</h3>

Status code

```
400 Bad Request
```

```json
{
  "error": ["“4c808757-a504-4168-93b2-847dbbd39ca” is not a valid UUID."]
}
```

<br>

### Student

#### 2 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/student/< int:school_id > | Create student. |
| GET | /school_manager/student/< int:school_id > | Get students. |
| GET | /school_manager/student/< int:school_id >/< int:student_id > | Get student profile. |
| PATCH | /school_manager/student/< int:school_id >/< int:student_id > | Update student. |
| DELETE | /school_manager/student/< int:school_id >/< int:student_id > | Delete student. |

<br>

<h3>👉 /school_manager/student/< int:school_id > - Create student</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
POST /school_manager/student/< int:school_id >
Host: localhost:8000
Content-type: application/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "name": "Tobias",
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
  "id": 1,
  "name": "Tobias",
  "last_name": "Almeida Ramos",
  "email": "tobias@gmail.com",
  "date_of_birth": "13/06/1990",
  "cpf": "07568875950",
  "phone": "43996935598",
  "gender": "masculino",
  "created_at": "2023-02-05T23:41:52.908114Z",
  "school_id": "1"
}
```

<br>

<h3>👉 /school_manager/student/< int:school_id > - Get students</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
GET /school_manager/student/< int:school_id >
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
    "id": 1,
    "name": "Tobias",
    "last_name": "Almeida Ramos",
    "email": "tobias@gmail.com",
    "date_of_birth": "13/06/1990",
    "cpf": "07568875950",
    "phone": "43996935598",
    "gender": "masculino",
    "created_at": "2023-02-05T23:41:52.908114Z",
    "school_id": "1"
  },
  {
    "id": 2,
    "name": "Marcos",
    "last_name": "Rocha",
    "email": "marcos@gmail.com",
    "date_of_birth": "20/08/2000",
    "cpf": "07568858970",
    "phone": "43996935040",
    "gender": "masculino",
    "created_at": "2023-02-05T23:41:52.908114Z",
    "school_id": "1"
  }
]
```

<br>

<h3>👉 /school_manager/student/< int:school_id >/< int:student_id > - Get student profile</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
GET /school_manager/student/< int:school_id >/< int:student_id >
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
  "name": "Tobias",
  "last_name": "Almeida Ramos",
  "email": "tobias@gmail.com",
  "date_of_birth": "13/06/1990",
  "cpf": "07568875950",
  "phone": "43996935598",
  "gender": "masculino",
  "created_at": "2023-02-05T23:41:52.908114Z",
  "school_id": "1"
}
```

<br>

<h3>👉 /school_manager/student/< int:school_id >/< int:student_id > - Update student</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/student/< int:school_id >/< int:student_id >
Host: localhost:8000
Content-type: aplication/json
Authorization: Bearer token
```

<h3>Request body</h3>

```json
{
  "email": "tobias_almeida@gmail.com",
  "phone": "43996935577"
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
  "name": "Tobias",
  "last_name": "Almeida Ramos",
  "email": "tobias_almeida@gmail.com",
  "date_of_birth": "13/06/1990",
  "cpf": "07568875950",
  "phone": "43996935577",
  "gender": "masculino",
  "created_at": "2023-02-05T23:41:52.908114Z",
  "school_id": "1"
}
```

<br>

<h3>👉 /school_manager/student/< int:school_id >/< int:student_id > - Delete student</h3>

[back to Endpoints](#2---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/student/< int:school_id >/< int:student_id >
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

### Course

#### 3 - Endpoints

[back to index](#index)

| Method | Route                                                      | Description    |
| ------ | ---------------------------------------------------------- | -------------- |
| POST   | /school_manager/course/< int:school_id >                   | Create course. |
| GET    | /school_manager/course/< int:school_id >                   | Get courses.   |
| GET    | /school_manager/course/< int:school_id >/< int:course_id > | Get a course.  |
| PATCH  | /school_manager/course/< int:school_id >/< int:course_id > | Update course. |
| DELETE | /school_manager/course/< int:school_id >/< int:course_id > | Delete course. |

<br>

<h3>👉 /school_manager/course/< int:school_id > - Create course </h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
POST /school_manager/course/< int:school_id >
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

<h3>👉 /school_manager/course/< int:school_id > - Get courses</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
GET /school_manager/course/< int:school_id >
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

<h3>👉 /school_manager/course/< int:school_id >/< int:course_id > - Get a course</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
GET /school_manager/course/< int:school_id >/< int:course_id >
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

<h3>👉 /school_manager/course/< int:school_id >/< int:course_id > - Update course

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/course/< int:school_id >/< int:course_id >
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

<h3>👉 /school_manager/course/< int:school_id >/< int:course_id > - Delete course</h3>

[back to Endpoints](#3---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/course/< int:school_id >/< int:course_id >
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

<br>

### Employee

#### 4 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/employee/< int:school_id > | Create employee. |
| GET | /school_manager/employee/< int:school_id > | Get employees. |
| PATCH | /school_manager/employee/< int:school_id >/< int:employee_id > | Update employee. |
| DELETE | /school_manager/employee/< int:school_id >/< int:employee_id > | Delete employee. |

<br>

<h3>👉 /school_manager/employee/< int:school_id > - Create employee </h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
POST /school_manager/employee/< int:school_id >
Host: localhost:8000
Content-type: application/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "username": "Claudia Amaral",
  "email": "claudia@gmail.com",
  "password": "856477"
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
  "username": "Claudia Amaral",
  "email": "claudia@gmail.com",
  "created_at": "2023-02-05T23:41:52.908114Z",
  "school_id": "1"
}
```

<br>

<h3>👉 /school_manager/employee/< int:school_id > - Get employees</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
GET /school_manager/employee/< int:school_id >
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
    "username": "Claudia Amaral",
    "email": "claudia@gmail.com",
    "created_at": "2023-02-05T23:41:52.908114Z",
    "school_id": "1"
  },
  {
    "id": 2,
    "username": "Pedro Cavalcante",
    "email": "pedro@gmail.com",
    "created_at": "2023-02-05T23:41:52.908114Z",
    "school_id": "1"
  }
]
```

<br>

<h3>👉 /school_manager/employee/< int:school_id >/< int:employee_id > - Update employee</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/employee/< int:school_id >/< int:employee_id >
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
  "id": 1,
  "username": "Claudia Amaral",
  "email": "claudia_amaral@gmail.com",
  "created_at": "2023-02-05T23:41:52.908114Z",
  "school_id": "1"
}
```

<br>

<h3>👉 /school_manager/employee/< int:school_id >/< int:student_id > - Delete employee</h3>

[back to Endpoints](#4---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/employee/< int:school_id >/< int:employee_id >
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

### Address

#### 5 - Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /school_manager/address/< int:school_id >/< int:student_id > | Create address. |
| GET | /school_manager/address/< int:school_id >/< int:student_id > | Get a address. |
| PATCH | /school_manager/address/< int:school_id >/< int:student_id > | Update address. |
| DELETE | /school_manager/address/< int:school_id >/< int:student_id > | Delete address. |

<br>

<h3>👉 /school_manager/address/< int:school_id >/< int:student_id > - Create address</h3>

[back to Endpoints](#5---endpoints)

<h3>Request information</h3>

```
POST /school_manager/address/< int:school_id >/< int:student_id >
Host: localhost:8000
Content-type: application/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "zip-code": "85444777",
  "state": "PR",
  "city": "Curitiba",
  "street": "Benedito Mascarenhas",
  "district": "Água azul",
  "number": "1584"
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
  "zip-code": "85444777",
  "state": "PR",
  "city": "Curitiba",
  "street": "Benedito Mascarenhas",
  "district": "Água azul",
  "number": "1584",
  "created_at": "2023-02-05T23:41:52.908114Z",
  "student_id": "1"
}
```

<br>

<h3>👉 /school_manager/address/< int:school_id >/< int:student_id > - Get a address</h3>

[back to Endpoints](#5---endpoints)

<h3>Request information</h3>

```
GET /school_manager/address/< int:school_id >/< int:student_id >
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
  "id": 1,
  "zip-code": "85444777",
  "state": "PR",
  "city": "Curitiba",
  "street": "Benedito Mascarenhas",
  "district": "Água azul",
  "number": "1584",
  "created_at": "2023-02-05T23:41:52.908114Z",
  "student_id": "1"
}
```

<br>

<h3>👉 /school_manager/address/< int:school_id >/< int:student_id > - Update address</h3>

[back to Endpoints](#5---endpoints)

<h3>Request information</h3>

```
PATCH /school_manager/address/< int:school_id >/< int:student_id >
Host: localhost:8000
Content-type: aplication/json
Authorization: Bearer Token
```

<h3>Request body</h3>

```json
{
  "number": "3050"
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
  "id": 1,
  "zip-code": "85444777",
  "state": "PR",
  "city": "Curitiba",
  "street": "Benedito Mascarenhas",
  "district": "Água azul",
  "number": "3050",
  "created_at": "2023-02-05T23:41:52.908114Z",
  "student_id": "1"
}
```

<br>

<h3>👉 /school_manager/address/< int:school_id >/< int:student_id > - Delete address</h3>

[back to Endpoints](#5---endpoints)

<h3>Request information</h3>

```
DELETE /school_manager/address/< int:school_id >/< int:student_id >
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
