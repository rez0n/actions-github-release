#!/usr/bin/env python3

from github import Github
import os

# Settings
wanted_release = os.environ['type']
repository = os.environ['repository']
token = os.getenv('token', None)

# Init class
G = Github(token)
repo = G.get_repo(repository)
releases = repo.get_releases()

# Output formatting function
def output(release):
    print('::set-output name=release::{}'.format(release.tag_name))
    print('::set-output name=release_id::{}'.format(release.id))
    assets = release.get_assets()
    print('::set-output name=browser_download_url::{}'.format(assets[0].browser_download_url))

# Releases parsing
for release in releases:
    if wanted_release == 'stable':
        if release.prerelease == 0 and release.draft == 0:
            output(release)
            break
    elif wanted_release == 'prerelease':
        if release.prerelease == 1:
            output(release)
            break
    elif wanted_release == 'latest':
        output(release)
        break
    elif wanted_release == 'nodraft':
        if release.draft == 0:
            output(release)
            break
    else:
        print('Cant get release')
