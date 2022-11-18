source ~/.zplug/init.zsh
zplug "zsh-users/zsh-syntax-highlighting", defer:2
zplug "zsh-users/zsh-completions", defer:2
autoload -U compinit && compinit
# Then, source plugins and add commands to $PATH
zplug load
