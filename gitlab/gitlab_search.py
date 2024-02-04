#!/usr/bin/env python3
'''
References:
- https://stackoverflow.com/questions/35087844/search-for-code-or-text-in-gitlab
- https://github.com/python-gitlab/python-gitlab
'''

# Import Standard Libraries
import argparse
import logging
import os
import sys

# Import External Libraries
import gitlab

DESCRIPTION='''\
description:
  This script is used to search GitLab for text.
'''

EPILOG='''\
epilog:
  detailed output for each argument here...
'''

def verify_gitlab_url():
    '''
    verify_gitlab_url is used to make sure we have a GitLab URL set.
    '''
    GITLAB_URL = ''
    if len(args.gitlab_url) > 0:
        GITLAB_URL = args.gitlab_url
    else:
        try:
            GITLAB_URL = os.environ["GITLAB_URL"]
        except Exception as e:
            logging.error("No GitLab URL defined, exiting.")
            print(e)
            parser.print_usage()
            sys.exit(1)
    return GITLAB_URL

def verify_gitlab_private_token():
    '''
    verify_gitlab_private_token is used to make sure we have a GitLab URL set.
    '''
    GITLAB_PRIVATE_TOKEN = ''
    if len(args.gitlab_private_token) > 0:
        GITLAB_PRIVATE_TOKEN = args.gitlab_private_token
    else:
        try:
            GITLAB_PRIVATE_TOKEN = os.environ["GITLAB_PRIVATE_TOKEN"]
        except Exception as e:
            logging.error("No GitLab Private Token defined, exiting.")
            print()
            parser.print_usage()
            sys.exit(1)
    return GITLAB_PRIVATE_TOKEN

def gitlab_search(gitlab_server, token, file_filter, text, group=None, project_filter=None, ssl_verify=bool):
    return_value = []
    gl = gitlab.Gitlab(url=gitlab_server, private_token=token, ssl_verify=ssl_verify)
    if (project_filter == '') and (group == ''):
        logging.debug('search all groups, this may take a while')
        projects = gl.projects.list(all=True)
    else:
        projects = []
        try:
            group_object = gl.groups.get(group)
            group_projects = group_object.projects.list(search=project_filter)
            for group_project in group_projects:
                projects.append(gl.projects.get(group_project.id))
        except Exception as e:
            logging.error(str(e))
            logging.error(f"Error getting group: {group}")
            sys.exit(0)
    for project in projects:
        logging.debug(f"working on project {project.attributes['name']}")
        files = []
        try:
            files = project.repository_tree(recursive=True, all=True)
        except Exception as e:
            print(str(e), "Error getting tree in project:", project.name)
        for file in files:
            # logging.debug(f"##### {file}")
            logging.debug(f"working on file {file['name']}")
            if file_filter == file['name'] or file_filter == "" and file['type'] == 'blob':

                file_content = project.files.raw(file_path=file['path'], ref='main')
                if text in str(file_content):
                    return_value.append({
                        "project": project.name,
                        "file": file['path']
                    })

    return return_value


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=DESCRIPTION,
    epilog=EPILOG
)
default = parser.add_argument_group("default arguments")
default.add_argument("--gitlab-file-filter", default="")
default.add_argument("--gitlab-group", default="examples")
default.add_argument("--gitlab-project", default="")
default.add_argument("--gitlab-search-text", default="pipeline")
default.add_argument("--gitlab-verify-ssl", action='store_false')
default.add_argument("--log-level", default="INFO")
required = parser.add_argument_group("required arguments")
required.add_argument("--gitlab-private-token", default="", required=False)
required.add_argument("--gitlab-url", default="http://localhost", required=False)
args = parser.parse_args()

# set log level of logging module
numeric_level = getattr(logging, args.log_level.upper(), None)
logging.basicConfig(level=numeric_level, format='%(asctime)s - %(levelname)s - %(message)s')


# Start
GL_URL = verify_gitlab_url()
GL_TOKEN = verify_gitlab_private_token()
RESULTS = gitlab_search(GL_URL, GL_TOKEN, args.gitlab_file_filter, args.gitlab_search_text, args.gitlab_group, args.gitlab_project, bool(args.gitlab_verify_ssl))

print('## Search Summary ##')
print(f"  GitLab URL: {GL_URL}")
print(f"  GitLab Group: {args.gitlab_group}")
print(f"  GitLab Project: {args.gitlab_project}")
print(f"  GitLab Search Text: {args.gitlab_search_text}")
print(f"  GitLab File Filter: {args.gitlab_file_filter}")
print(f"  GitLab Verify SSL: {args.gitlab_verify_ssl}")

if len(RESULTS) > 0:
    print('## Search Results (found in files) ##')
    for i in RESULTS:
        print(i)
else:
    print('## Search Results (nothing found)')
