import os
import time
from helper import Config, ConfigParser, Dir

from github_lib import *

if __name__ == '__main__':
    start_time = time.time()
    conf = Config('conf.ini')

    github = Github(conf.token, conf.url)

    #github.create_repo('blog')

    # github.commit_file('ccocom/blog', 'with-module1.py')

    github.delete_file('ccocom/blog', 'with-module1.py')

    github.commit_file('ccocom/blog', 'with-module1.py')
    
    github.commit_file('ccocom/blog', 'with-module1.py')

    # github.delete_repo('ccocom/blog')

    # github.get_repos() 

