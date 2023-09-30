# Docker-Git bridge

```
                           ___....___
 ^^                __..-:'':__:..:__:'':-..__
                 _.-:__:.-:'':  :  :  :'':-.:__:-._
               .':.-:  :  :  :  :  :  :  :  :  :._:'.
            _ :.':  :  :  :  :  :  :  :  :  :  :  :'.: _
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
    DOCKER [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]   GIT
  :::::::::[ ]:__:__:__:__:__:__:__:__:__:__:__:__:__:[ ]:::::::::::
  !!!!!!!!![ ]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![ ]!!!!!!!!!!!
  ^^^^^^^^^[ ]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[ ]^^^^^^^^^^^
           [ ]                                        [ ]
           [ ]                                        [ ]
           [ ]                                        [ ]
   ~~^_~^~/   \~^-~^~ _~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/   \~^ ~~_ ^
```
DOKER IMAGE: https://hub.docker.com/r/antoniofrs/docker-git-bridge

Docker-git bridge is an application that allows you to build an image and run
the related container starting from a git repository.

Since a git access key and an exposed docker daemon are required,
I strongly advise against using this application in production or on a cloud environment.


### Environment variable

- DGB_GIT_TOKEN
- DGB_GIT_PATH  (eg: github.com/<username>/<repo>)
- DGB_GIT_BRANCH (default: main)

- DGB_DOCKER_FILE_NAME (default: Dockerfile)
- DGB_DOCKER_HOST (default: unix://var/run/docker.sock, e.g: tcp://123.123.123.123:2375 )
- DGB_EXPOSED_PORTS (e.g: 5000:5000,8080:80)
- DGB_DOCKER_IMAGE_TAG (default: dgb-image:latest)

### Docker file example:

```yml
  my-container:
    image: antoniofrs/docker-git-bridge
    container_name: my-container
    environment:
      - DGB_GIT_TOKEN=github_pat_123412341234....abcdabcs
      - DGB_GIT_PATH=github.com/antoniofrs/<repo-here>
      - DGB_GIT_BRANCH=main
      - DGB_DOCKER_FILE_NAME=Dockerfile
      - DGB_DOCKER_HOST=tcp://123.123.123.123:2375
      - DGB_EXPOSED_PORTS=5000:5000,4040:4040,8080:80
      - OTHER_ENV_VAR=other_env_value
```

You can specify the list of environment variables needed by your container inside the `environment` section.

## Not supported yet:
- Docker tls
- Docker networks
