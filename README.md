# Docker Compose for Django, Celery, Redis, and Postgres

#### Build docker

```
sudo docker-compose build
```

#### Start docker

```
sudo docker-compose up
```

### Stop docker-compose

```
sudo docker-compose down
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

