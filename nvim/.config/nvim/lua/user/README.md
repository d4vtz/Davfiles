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
```
## Plugins
 Los plugins que necesito para mi flujo de trabajo son:

 - [Nord](https://github.com/shaunsingh/nord.nvim):
Tema de Neovim basado en la paleta de colores Nord.

- [Vimtex](https://github.com/lervag/vimtex):
VimTeX es un complemento moderno de sintaxis y tipo de archivo Vim y Neovim para archivos LaTeX.

- [Trouble](https://github.com/folke/trouble.nvim)
Una bonita lista para mostrar diagnósticos, referencias, resultados de telescopios, soluciones rápidas y listas de ubicaciones para ayudarlo a resolver todos los problemas que está causando su código.

-[Mkdir](https://github.com/jghauser/mkdir.nvim)
Un complemento para neovim que crea automáticamente los directorios que faltan al guardar un archivo.

- [Hop](https://github.com/phaazon/hop.nvim)
Hop es un complemento similar a EasyMotion que le permite saltar a cualquier parte de un documento con la menor cantidad de pulsaciones de teclas posible.

- [Glow](https://github.com/ellisonleao/glow.nvim)
Obtenga una vista previa del código markdown directamente en Neovim.

- [Project](https://github.com/ahmedkhalf/project.nvim)
un complemento de neovim todo en uno escrito en lua que proporciona una gestión de proyectos superior.

- [Telescope Bibtex](https://github.com/nvim-telescope/telescope-bibtex.nvim)
Busque y pegue entradas de *.bibtex con telescopio.

- [Code Runner](https://github.com/CRAG666/code_runner.nvim)
Ejecutor de código

