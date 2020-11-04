#!/usr/bin/env python3

from github import Github
import os
wanted_release = os.environ['type']
repository = os.environ['repository']
token = os.environ['token']

G = Github(token)
repo = G.get_repo(repository)
releases = repo.get_releases()
for release in releases:
    if wanted_release == 'stable':
        if release.prerelease == 0 and release.draft == 0:
            print('::set-output name=release::{}'.format(release.tag_name))
            break
    elif wanted_release == 'prerelease':
        if release.prerelease == 1:
            print('::set-output name=release::{}'.format(release.tag_name))
            break
    elif wanted_release == 'latest':
        print('::set-output name=release::{}'.format(release.tag_name))
        break
    else:
        print('Cant get release')
