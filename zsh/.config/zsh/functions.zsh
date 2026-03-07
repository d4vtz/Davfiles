function mkcd(){
  mkdir -p $1 && cd $1
}

function zupdate(){
  source "${ZDOTDIR:-$HOME}/alias.zsh"
  source "${ZDOTDIR:-$HOME}/functions.zsh"
  source "${ZDOTDIR:-$HOME}/.zshrc"
}
