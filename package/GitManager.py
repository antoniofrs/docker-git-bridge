import logging
import os
import re
import git

from package.Validator import not_empty
from package.model.GitConfig import GitConfig


def clone_repo(git_config: GitConfig):
    app_dir = 'app'

    try:
        repo_url = get_repo_url(
            git_config.url,
            git_config.username,
            git_config.password
        )

        if os.path.exists(app_dir):
            logging.info("Pulling from remote branch")
            repo = git.Repo(app_dir)
            repo.remotes.origin.pull()
        else:
            logging.info("Repo not found, cloning from remote branch")
            repo = git.Repo.clone_from(repo_url, app_dir)
        
        logging.info(f"Checking out branch {git_config.branch}")
        if repo.active_branch.name != git_config.branch:
            logging.info(f"Checking out to {git_config.branch} branch")
            repo.git.checkout(git_config.branch)

    except git.GitCommandError as e:
        logging.error(f'Cannot clone or pull remote repository: {e}')

    except Exception as ex:
        logging.error(f'Unexpected exception: {ex}')


def get_repo_url(repo_url, username, password):

    # Does the URL contain username and password?
    if re.search(r':\/\/[^@]+@', repo_url):
        return repo_url

    credentials = ""
    if not_empty(username):
        credentials += username
    if not_empty(password):
        if credentials:
            credentials += ":" + password
        else:
            logging.error("Missing username for specified password")
            exit(0)

    if credentials:
        repo_url = re.sub(r'https://', f'https://{credentials}@', repo_url)

    return repo_url