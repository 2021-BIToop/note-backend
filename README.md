# note-backend

> BITOOP class homework

One designed note software backend

#### Install
```
pip install fastapi
pip install uvicorn
pip install sqlalchemy
```

### Setup
```
uvicorn main:app --reload
```

### Docker

This project has been dockerized. To build a docker image from source, execute the following command at the root directory of this project:

```shell
$ docker build .
```

The docker image built can be started by the following command:

```shell
$ docker run -d -p 80:3000 <image-id>
```

If you want to bind the HTTP server to a different local address, start the image by the following command:

```shell
$ docker run -d -p <local-address>:80:3000 <image-id>
```

where `<local-address>` is the local address of the host machine that the HTTP server will be bound to.
