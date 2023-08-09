# Docker Compose for Django, Celery, Redis, and Postgres
* CRUD operations on a Task with Postgres as Db
* Using Celery-tasks to update task priority asynchronously with different delays

  eg: Task with priority High, its status will move from 0-1 in x seconds, then 1-2 in y seconds 
#### Build docker

```
docker-compose build
```

#### Start docker

```
docker-compose up
```

### Stop docker-compose

```
 docker-compose down
```

#### Task CRUD API on 

```
http://0.0.0.0:80/tasks/
```

#### Sample Request 

```
{
    "title": "test task",
    "description": "Testing",
    "owner_email": "h1@a1.com",
    "creator_email": "h2@w2.com",
    "priority": 1

}
```

