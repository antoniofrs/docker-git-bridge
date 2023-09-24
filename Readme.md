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
Docker-git bridge is an application that allows you to build an image and run
the related container starting from a git repository.

Since git access keys and an exposed docker daemon are required,
I strongly advise against using this application in production or on the cloud.


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
    container_name: my-container
    environment:
      - DGB_GIT_TOKEN=github_pat_123412341234....abcdabcs
      - DGB_GIT_PATH=github.com/antoniofrs/<repo-here>
      - DGB_GIT_BRANCH=main
      - DGB_DOCKER_FILE_NAME=Dockerfile
      - DGB_DOCKER_HOST=123.123.123.123:2375
      - DGB_EXPOSED_PORTS=5000:5000
```

## Not supported yet:
- Docker tls
- Docker networks