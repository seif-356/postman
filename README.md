#swagger

openapi: 3.0.0
info:
  title: Lab 3
  version: 1.0.0
servers:
  - url: http://127.0.0.1:3000
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
paths:
  /todos:
    get:
      tags:
        - default
      summary: http://127.0.0.1:3000/todos
      security:
        - bearerAuth: []
      responses:
        '200':
          description: Successful response
          content:
            application/json: {}
    post:
      tags:
        - default
      summary: New Request
      requestBody:
        content:
          application/json:
            schema:
              type: object
              example:
                title: task2
                completed: false
      security:
        - bearerAuth: []
      responses:
        '200':
          description: Successful response
          content:
            application/json: {}
    delete:
      tags:
        - default
      summary: New Request
      security:
        - bearerAuth: []
      responses:
        '200':
          description: Successful response
          content:
            application/json: {}
  /todos/2:
    put:
      tags:
        - default
      summary: New Request
      requestBody:
        content:
          application/json:
            schema:
              type: object
              example:
                title: Cloudys task
                completed: true
      security:
        - bearerAuth: []
      responses:
        '200':
          description: Successful response
          content:
            application/json: {}
