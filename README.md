This is an example project of Python/Flask with Gunicorn and an Nginx running in Docker.   
It is not fully 100% good yet, this is a first draft.

Dowload with git and then  
```
docker-compose -f docker-compose.yml up --build
```

In browser: http://localhost:8080/myapp/

Visual Code can then be used to connect to the container and develop/test code inside the container.
Gunicorn is setup to reload when new codes is stored.
  
  
Examles was take from below links:  
[For explanation please visit my blog on blog.entirely.digital](https://blog.entirely.digital/docker-gunicorn-and-flask)

To add SSL, please check Nginx and Let’s Encrypt 
[Nginx and Let’s Encrypt](https://medium.com/@pentacent/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71)  

