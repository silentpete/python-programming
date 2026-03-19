import os
import sys
import gitlab
import datetime

token = os.environ.get('GITLAB_ACCESS_TOKEN', None)
if token is None:
    print("Please set GITLAB_ACCESS_TOKEN")
    sys.exit(1)

gl = gitlab.Gitlab('https://gitlab01.parrylabs.net/', private_token=token, user_agent='token_checker/0.1')

todayplus30 = (datetime.datetime.today() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')

commands = []

print("PAT")
print("user,token_id,token_name,expires_at")
for t in gl.personal_access_tokens.list(all=True, as_list=False):
    if t.revoked or not t.active:
        continue

    if t.expires_at is not None and t.expires_at <= todayplus30:
        user = gl.users.get(t.user_id)
        if user.state != "active":
            continue
        print(f'"{user.name}","{t.id}","{t.name}","{t.expires_at}"')
        commands.append(f"PersonalAccessToken.where(id: {t.id}).update_all(expires_at: 1.year.from_now)")

print()
print()
print("GROUP TOKENS")
print("group,group_id,token_id,token_name,expires_at")
for group in gl.groups.list(all=True, as_list=False):
    for t in group.access_tokens.list(all=True, as_list=False):
        if t.revoked or not t.active:
            continue

        if t.expires_at is not None and t.expires_at <= todayplus30:
            print(f'"{group.name}","{group.id}","{t.id}","{t.name}","{t.expires_at}"')
            # Group tokens still appear as PATs
            commands.append(f"PersonalAccessToken.where(id: {t.id}).update_all(expires_at: 1.year.from_now)")

print()
print()
print("PROJECT TOKENS")
print("project,project_id,token_id,token_name,expires_at")
for project in gl.projects.list(all=True, as_list=False):
    for t in project.access_tokens.list(all=True, as_list=False):
        if t.revoked or not t.active:
            continue

        if t.expires_at is not None and t.expires_at <= todayplus30:
            print(f'"{project.name}","{project.id}","{t.id}","{t.name}","{t.expires_at}"')
            # Project tokens are also PATs, woo
            commands.append(f"PersonalAccessToken.where(id: {t.id}).update_all(expires_at: 1.year.from_now)")

# Deploy tokens don't currently appear to have enforce expiry dates, so skip those.
# print()
# print()
# print("DEPLOY TOKENS")
# print("deploy_token_id,deploy_token_name,deploy_token_username,expires_at")
# for t in gl.deploytokens.list(all=True, as_list=False):
#     if t.revoked or t.expired:
#         continue

#     if t.expires_at is not None:
#         if t.expires_at <= todayplus30:
#             print(f'"{t.id}","{t.name}","{t.username}","{t.expires_at}"')

print()
print()
print("COMMANDS")
print("These are the commands to extend the expiration date of the tokens.")
print("On the Gitlab server run `gitlab-rails console` and paste these commands in.")
print()
for c in commands:
    print(c)
