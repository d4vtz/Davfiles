#  Configuración de usuario AstroNvim

Esta es mi Configuración personal de AstroNvim.

## Instalación

- Instalar AstroNvim:

```sh
git clone https://github.com/AstroNvim/AstroNvim.git ~/.config/nvim
```

- Instalar estas configuraciones de usuario:

```sh
git clone git@github.com:d4vtz/Davfiles.git ~/.Davfiles
cd ~/.Davfiles
stow nvim
```

- Inicializar AstroNvim

```sh
nvim --headless -c 'autocmd User PackerComplete quitall' -c 'PackerSync'

