export XDG_CONFIG_HOME=$HOME/.config
export ZDOTDIR=$XDG_CONFIG_HOME/zsh
export OPENAI_API_KEY=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

typeset -U path PATH
path=(~/.local/bin $path)
export PATH
