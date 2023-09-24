import logging
import os
from threading import Thread
import docker

class DockerManager:

    def __init__(self, docker_host, docker_image_tag, docker_file_name, mapped_ports) -> None:
        self.docker_image_tag = docker_image_tag
        self.docker_file_name = docker_file_name
        self.mapped_ports = mapped_ports
        self.client = docker.DockerClient(base_url=docker_host, tls=False)


    def build_image(self):
        logging.info("Building image")
        self.client.images.build(
            path="app/",
            tag=self.docker_image_tag,
            dockerfile=self.docker_file_name,
            buildargs=None,
            rm=True
        )

    def run_container(self):
        logging.info("Running container")
        self.container = self.client.containers.run(
            image=self.docker_image_tag,
            ports = self.mapped_ports,
            environment=[f"{key}={value}" for key, value in os.environ.items()],
            remove=True,
            detach=True
        )

        Thread(
            target=log_container,
            args=[self.container]
        ).start()
        
    def __del__(self):
        logging.info("Stopping container")
        if self.container != None:
            self.container.stop()
            self.container.remove()


def log_container(container):
    for log in container.logs(stream=True, follow=True):
        logging.info(log.decode('utf-8').strip())



