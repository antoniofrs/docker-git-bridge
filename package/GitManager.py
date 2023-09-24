import logging
import os
import git

def clone_repo(access_token , repo_path, branch):
    app_dir = 'app'

    try:
        repo_url = get_repo_url(repo_path,access_token)
        if os.path.exists(app_dir):
            logging.info("Pulling from remote branch")
            repo = git.Repo(app_dir)
            repo.remotes.origin.pull()
        else:
            logging.info("Repo not found, cloning from remote branch")
            repo = git.Repo.clone_from(repo_url, app_dir)
        
        logging.info(f"Checking out branch {branch}")
        if repo.active_branch.name != branch:
            repo.git.checkout(branch)

    except git.GitCommandError as e:
        print(f'Cannot clone or pull remote repository: {e}')

    except Exception as ex:
        print(f'Unexpected exception: {ex}')


def get_repo_url(repo_path,access_token):
    
    if access_token != None:
        access_token += "@"

    return f'https://{access_token}{repo_path}'