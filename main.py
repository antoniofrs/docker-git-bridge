import signal
import sys
import os
import logging
from package.DockerManger import DockerManager
from package.GitManager import clone_repo
from package.Validator import convert_mapped_ports, validate_config
from package.model.GitConfig import GitConfig

# Configure logger
logging.basicConfig (
    format="[%(asctime)s] %(module)s:%(lineno)d %(levelname)s\t%(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
    level=logging.INFO
)

# Get Config

config = {
    "git_password": os.getenv('DGB_GIT_PASSWORD', None),
    "git_username": os.getenv('DGB_GIT_USERNAME', None),
    "repo_url": os.getenv("DGB_GIT_REPO_URL"),
    "branch": os.getenv("DGB_GIT_BRANCH", "main"),
    "docker_host": os.getenv("DGB_DOCKER_HOST", "unix://var/run/docker.sock"),
    "docker_file_name": os.getenv("DGB_DOCKER_FILE_NAME", "Dockerfile"),
    "docker_image_tag": os.getenv("DGB_DOCKER_IMAGE_TAG", "dgb-image:latest"),
    "docker_exposed_ports": convert_mapped_ports(os.getenv("DGB_EXPOSED_PORTS"))
}

validate_config(config)

# Clone or pull repository
gitConfig = GitConfig(
    url= config["repo_url"],
    username= config["git_username"],
    password= config["git_password"],
    branch= config["branch"]
)

clone_repo(gitConfig)

# Start docker container
docker_manager = DockerManager(
    docker_host=config["docker_host"],
    docker_image_tag=config["docker_image_tag"],
    docker_file_name=config["docker_file_name"],
    mapped_ports= config["docker_exposed_ports"]
)

docker_manager.build_image()
docker_manager.run_container()

signal.signal(signal.SIGTERM, lambda _ : docker_manager.__del__())