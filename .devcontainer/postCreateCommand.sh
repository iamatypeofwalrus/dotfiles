#!/usr/bin/env sh

# add the goreleaser binary to apt-get
echo 'deb [trusted=yes] https://repo.goreleaser.com/apt/ /' | sudo tee /etc/apt/sources.list.d/goreleaser.list

sudo apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && sudo apt-get -y install --no-install-recommends \
        jq \
        goreleaser \
        hugo \
        awscli \
        protobuf-compiler
