# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.config/zsh/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Upload plugin manager zap
[ -f "$HOME/.local/share/zap/zap.zsh" ] && source "$HOME/.local/share/zap/zap.zsh"

plug "zsh-users/zsh-completions"
plug "zsh-users/zsh-autosuggestions"
plug "zsh-users/zsh-syntax-highlighting"
plug "romkatv/powerlevel10k"

# Complete and autosuggestions menu
autoload -Uz compinit && compinit
unsetopt menu_complete
setopt auto_menu
zstyle ':completion:*:default' menu select=2
bindkey '^ ' autosuggest-execute

# Command Hystory
setopt sharehistory
setopt histignorealldups
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=$ZDOTDIR/zsh_history

# To customize prompt, run `p10k configure` or edit ~/.config/zsh/.p10k.zsh.
[[ ! -f ~/.config/zsh/.p10k.zsh ]] || source ~/.config/zsh/.p10k.zsh
