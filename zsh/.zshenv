export XDG_CONFIG_HOME=$HOME/.config
export ZDOTDIR=$XDG_CONFIG_HOME/zsh

typeset -U path PATH
path=(~/.local/bin $path)
export PATH
