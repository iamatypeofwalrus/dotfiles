export EDITOR="subl --wait --new-window"
export GREP_OPTIONS='--color=auto'
export CLICOLOR=true # ls colors output on Mac OS

export PATH=/usr/local/sbin:$PATH
export PATH=/usr/local/bin:$PATH
export PATH="/Applications/Sublime Text.app/Contents/SharedSupport/bin":$PATH # subl
export PATH="/opt/homebrew/bin":$PATH

export PATH="/Users/jfeeney/opt/anaconda3/bin:$PATH"
export PATH=~/.local/bin:$PATH # python user install
export PATH="/opt/homebrew/opt/libpq/bin:$PATH" # postgresql client

alias cs="gh codespace ssh -- -t 'zsh -l'"
