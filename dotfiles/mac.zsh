export EDITOR="subl --wait --new-window"
export GREP_OPTIONS='--color=auto'
export CLICOLOR=true # ls colors output on Mac OS

export PATH=/usr/local/sbin:$PATH
export PATH=/usr/local/bin:$PATH
export PATH=$PATH:$GOPATH/bin
export PATH="/Applications/Sublime Text.app/Contents/SharedSupport/bin":$PATH # subl

# Do i need much of this shit if I will just dev on codespaces?
export PATH=~/.nodenv/shims:$PATH            # nodenv
export PATH=/usr/local/var/rbenv/shims:$PATH # rbenv
export PATH=~/.pyenv/shims:$PATH             # pyenv
export PATH=~/.local/bin:$PATH               # python user install
export PATH=$PATH:$HOME/.cargo/bin

export GOPATH=$HOME/code/go

alias ssh-gh-cs="gh codespace ssh -- -t 'zsh -l'"

# load runtimes
lr() {
    eval "$(rbenv init -)" 
    eval "$(nodenv init -)"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    export PATH=$(python -m site --user-base)/bin:$PATH
}
