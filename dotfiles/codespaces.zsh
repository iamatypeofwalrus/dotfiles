export EDITOR='code --wait'
export LS_COLORS='di=34:ln=35:so=32:pi=33:ex=31:bd=34;46:cd=34;43:su=30;41:sg=30;46:tw=30;42:ow=30;43' # ls colors on Ubuntu that match Mac OS
export PATH=/usr/local/go/bin:$PATH # prefer the version that's installed here as it's the one the Golang extension will use

alias ls='ls --color=auto' # couldn't figure out how to do it with just the env variables. this was pretty quick
