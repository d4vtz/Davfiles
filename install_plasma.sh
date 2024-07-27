#! /bin/env bash
common=(chrome lsd zathura nvim zsh paru tmux)


linked()
{
  stow $1
  if [ $? -eq 0 ]
  then
    echo El paquete $1 ha sido instalado
  else
    echo Ha fallado la instalacion del paquete $1
  fi
}

common_install()
{
for pack in ${common[@]}
do
  linked $pack
done
}


plasma_install()
{
  linked plasma
}

common_install
plasma_install
