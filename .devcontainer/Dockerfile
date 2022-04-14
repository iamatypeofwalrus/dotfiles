FROM "mcr.microsoft.com/vscode/devcontainers/universal:linux"

# install tools
RUN echo 'deb [trusted=yes] https://repo.goreleaser.com/apt/ /' | sudo tee /etc/apt/sources.list.d/goreleaser.list

RUN sudo apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && sudo apt-get -y install --no-install-recommends \
        jq \
        goreleaser \
        hugo
