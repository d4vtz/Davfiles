source ~/.zplug/init.zsh
autoload -Uz compinit && compinit
zplug "zsh-users/zsh-syntax-highlighting", defer:2
zplug "zsh-users/zsh-completions", defer:2
zplug "zsh-users/zsh-autosuggestions", defer:2

# Complete and autosuggestions menu
unsetopt menu_complete
setopt auto_menu
zstyle ':completion:*:default' menu select=2
bindkey '^ ' autosuggest-execute

# Then, source plugins and add commands to $PATH
zplug load
