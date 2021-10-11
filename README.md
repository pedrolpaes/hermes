# Projeto de API para Portal Codivas

Usamos Django REST framework

https://www.django-rest-framework.org/

Para testar os endpoints/chamadas de API escolha:

- `Postman`
- `Insomnia`
- VS extension `Thunder Client` 





#### Depois clonado o respositorio, no terminal:

1.  Entrar na pasta principal`$ cd hermes`
2.  Criar ambiente virtual`$ python -m venv .venv`
3.  Ativar ambiente virtual `$ source .venv/bin/activate`
4. Instalar os pacotes que estão usados `$ pip install -r requirements.txt`
5.  Criar sua branch de teste/issues `$ git checkout -b <nomeDaMinhaBranch>`

#### Iniciar Django and REST framework:

1. `$ python manage.py runserver`
2. 

---

#### Endpoint para o cadastro do usuário

POST /usuario/cadastro/ 		

**Body** parameters

| Name      | Data Type | Required | Default Value | Description      |
| --------- | --------- | -------- | ------------- | ---------------- |
| email     | text      | true     | ----          | email do usuário |
| password  | text      | true     | ----          | senha            |
| user_name | text      | true     | ----          | nome do usuário  |

Exemplo do **Request**:

{
    "email": "hello@example.com",
    "password": "VerySafePassword0909",
	“user_name”: “Eumesma”

}

Exemplo do **Response**:

Status: 201 Created
{
 	"email": "hello@example.com",
	“user_name”: “Eumesma”
}



---

#### Endpoint para liberação dos tokens de autentificação “access” e “refresh” (JWT)

<a href=https://jwt.io/>Mais sobre JWT</a>  <a href=https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html>Mais sobre Django RESTframework simplejwt</a>

POST  /api/token/

**Body** parameters

| Name     | Data Type | Required | Default Value | Description      |
| -------- | --------- | -------- | ------------- | :--------------- |
| email    | text      | true     | ----          | email do usuário |
| password | text      | true     | ----          | senha            |

Exemplo do **Request**:

{
    "email": "hello@example.com",
    "password": "VerySafePassword0909",
}

Exemplo do **Response**:

Status: 200 OK

{

​	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMTQ5NTM0OSwianRpIjoiMjQ3Zjk4ZTNjY2QzNGNhNDgxOGQyM2Y1ZDI0ZWYyZjkiLCJ1c2VyX2lkIjo0fQ.ZvtehE6HSKbnQ4IF9W4q9Ix68eFVlaS11ken5TYeWLg",

​	“access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMxNDA5MjQ5LCJqdGkiOiJjNmM2OWMzOGY0MTM0ZTI3YjdmNWFmODNkYjg2ZWQyMyIsInVzZXJfaWQiOjR9.t_rypTfu7xmxpLuuBUu-YqliZNJGdH1yVnp6fDePkWs"

}



---

#### Endpoint para atualizar o “refresh” token

POST /api/token/refresh/

**Body** parameters

| Name    | Data Type | Required | Default Value | Description   |
| ------- | --------- | -------- | ------------- | :------------ |
| refresh | text      | true     | ----          | refresh token |

Exemplo do **Request**:

{
	"refresh": 																																																															"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMTQ5NTM0OSwianRpIjoiMjQ3Zjk4ZTNjY2QzNGNhNDgxOGQyM2Y1ZDI0ZWYyZjkiLCJ1c2VyX2lkIjo0fQ.ZvtehE6HSKbnQ4IF9W4q9Ix68eFVlaS11ken5TYeWLg",
}



Exemplo do **Response**:

Status: 200 OK

{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMxNDEzMjU0LCJqdGkiOiI0ODY3ZmMxY2RmYWY0YmI2OTQyMzdjNTZiN2Y4ZjZiMyIsInVzZXJfaWQiOjR9.CKxReV_-GgDx3ndJ3AmvBeZG_0lHBXIfT3ckHD_xn10",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMTQ5OTM1NCwianRpIjoiYWFmY2YxNDI4NGY4NDFiYWE3OGM3MzcxODBjNTcwNjQiLCJ1c2VyX2lkIjo0fQ.y0FW8o94OSzDpmtOS_vQerhW2MFfCye5nU7lpSCwdzA"
}



---

#### Endpoint para obter a lista de usuários

GET usuario/

**Body** parameters

None

Exemplo do **Response**:

{...},

{
    "id": 4,
    "password": "pbkdf2_sha256$260000$NXarxzcniaSww6D02Ot2Uo$0JKaYRjGhlqM1ttlSV9R0aMkm1Kuuk6Kdoj4aluPhg4=",
    "is_superuser": false,
    "email": "lolo@lolo.com",
    "user_name": "Lolo",
    "nome": "",
    "sobrenome": null,
    "bio": "",
    "genero": null,
    "cpf": null,
    "data_nascimento": null,
    "cep": null,
    "cidade": null,
    "estado": null,
    "is_staff": false,
    "is_active": true,
    "date_joined": "2021-09-11T23:08:29.824123Z",
    "last_login": "2021-09-11T23:08:29.619171Z",
    "groups": [],
    "user_permissions": []
  },

{...}

