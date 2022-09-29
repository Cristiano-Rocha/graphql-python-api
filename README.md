# graphql-python-api

This a simple Web Api using GraphQL.

## Tecnologies used

* **[Pyhon3](https://www.python.org/downloads/)** Python is a programminglanguage that lets you work quickllu and integrate more effectively
* **[Flask](flask.pocoo.org/)** Flask is a microframework written in Python
* **[Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/e)** Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application
* **[Ariadne](https://ariadnegraphql.org/)** taps into the leading approach in the GraphQL community and opens up hundreds of developer tools, examples, and learning resources.
* **[Postgres](https://www.postgresql.org/)** is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.


## 🌱 How to start this project

Build the image:

```code
docker build -t graphql-python-api:latest -f graphql-python-api/Dockerfile graphql-python-api

```

Run the container with the following command:

```code
docker run -p 5000:5000 graphql-python-api:latest

```

### Queries

#### GET

```code
query GetPost {
  getPost(id: "3"){
    post {
      id
      title
      description
    }
    success
    errors
  }
}

```

#### POST
```code
mutation newPost {
  createPost(
    title: "Welcome to my Blog",
    description:"This is a description") {
    post {
      id
      title
      description
    }
    success
    errors
  }
}

```

#### DELETE
```code
mutation DeletePost {
  deletePost(id: 1){
    success
    errors
  }
}
```

#### PUT
```code
mutation UpdatePost {
  updatePost(id: 2,title:"This is another new night", description:"another detail of a new night"){
    success
    errors
  }
}

```
