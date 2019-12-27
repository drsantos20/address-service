# Address API
Customer and Address API

## Overview

RabbitMQ, celery and Kombu was used to exchange messages between each app/service

Following the diagram below, celery keeps consumer up to listen if has a new message to given a queue.

For the producer part it also was used kombu to send a message to given a queue.

![oder-address-ms](/img/order-address-ms-design.png)

![der](/img/order-address-ms-er.png)

### Getting Started
Following these instructions will make this project running in your local machine development.

**The entire customer app needs from other project to be up as well which is:**
[customer-api](https://github.com/drsantos20/customer-service.git)

### Prerequisites

- Have a google maps api key

```buildoutcfg
- Python
- Docker
- docker-compose
- Postgres
```

### Installing

1- `Customer`
```buildoutcfg
1- git clone https://github.com/drsantos20/customer-service.git
2- cd customer-service
3- python3 -m venv env
4- source env/bin/activate
5- docker-compose up --build
```

2- `Address`
```buildoutcfg
1- git clone https://github.com/drsantos20/address-service.git
2- cd address-service
2.1 Add your google maps API key into /address-service/api/settings.py -> `GOOGLE_API_KEY`
3- python3 -m venv env
4- source env/bin/activate
5- docker-compose up --build
```

### Running tests

Make ensure if rabbitmq and postgres images is running.

to check ``docker ps``

```buildoutcfg
python manage.py test
```

### Available URLS:
```buildoutcfg
POST http://127.0.0.1:8000/api/v1/order/
```

## Author

* **Daniel Santos** - *Trying to keep simple and clean* - [drsantos20](https://github.com/drsantos20)