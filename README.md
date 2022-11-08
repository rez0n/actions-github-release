# GitHub Actions: Get Github release

This Action able to get latest release version (tag) of the monorepo package.

## Configuration

### Inputs

| Name       | Description                                                  | Example                       |
| ---------- | ------------------------------------------------------------ | ----------------------------- | ------ | -------- | -------- |
| repository | The Github owner/repository                                  | `nodejs/node`                 |
| type       | The release type (prerelease                                 | stable                        | latest | nodraft) | `stable` |
| token      | Github auth token (default variable for each action session) | `${{ secrets.GITHUB_TOKEN }}` |
| package    | monorepo package name                                        |

#### Possible values for `type` input

- _stable_ - Get the stable `latest` release
- _prerelease_ - Get the latest `prerelease`
- _latest_ - Get the _really_ latest release with no matter is it stable or prerelease
- _nodraft_ - Get the _really_ latest release excluding drafts

### Outputs

Action outputs 3 variables

- `release` - release tag
- `release_id` - release Github ID
- `browser_download_url` - URL to download first file in release assets

## Usage example

```
on:
  push:
    branches: [ main ]

jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:

    - name: Get latest release of NodeJS
      uses: rez0n/actions-github-release@main
      id: node_release
      env:
        token: ${{ secrets.GITHUB_TOKEN }}
        repository: "nodejs/node"
        type: "stable"
        package: "@organization/user-service"

    - name: Build image
      uses: docker/build-push-action@v1
        with:
          ...
          dockerfile: Dockerfile
          tags: latest, ${{ steps.node_release.outputs.release }}
```
