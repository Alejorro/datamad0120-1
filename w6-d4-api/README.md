## Build docker image with name `miapi`

`docker build -t miapi .`


## Run a docker container from image with name `miapi

`docker run -p 5000:5000 miapi`

`docker run -p 5000:5000 --env MONGODB_URL="mongodb://host.docker.internal/companies" miapi`

## Deploy with docker in HEROKU

heroku login
heroku container:login
heroku container:push web
heroku container:release web

## Sync with mongodb atlas remote database

Before running this command, create a `.private.env` file with content `REMOTE_DB=....`
`$ bash syncdb.sh`

- [https://devcenter.heroku.com/articles/container-registry-and-runtime]