-- Configure plugins
return {
  ["shaunsingh/nord.nvim"] = require("user.plugins.nord"),
  ["lervag/vimtex"] = require("user.plugins.vimtex"),
  ["barreiroleo/ltex-extra.nvim"] = {},
  ["folke/trouble.nvim"] = require("user.plugins.trouble"),
  ["jghauser/mkdir.nvim"] = {},
  ["nvim-telescope/telescope-bibtex.nvim"] = require("user.plugins.telescope_bibtex"),
  ["phaazon/hop.nvim"] = require("user.plugins.hop"),
  ["ahmedkhalf/project.nvim"] = require("user.plugins.project"),
  ["goolord/alpha-nvim"] = require("user.plugins.alpha"),
  ["CRAG666/code_runner.nvim"] = require("user.plugins.code_runner"),
  ["ellisonleao/glow.nvim"] = require("user.plugins.glow"),
  ["simrat39/rust-tools.nvim"] = require("user.plugins.rust_tools"),
  ["hrsh7th/cmp-nvim-lsp-signature-help"] = require("user.plugins.cmp_nvim_lsp_signature_help"),
  ["j-hui/fidget.nvim"] = require("user.plugins.fidget"),
  ["tpope/vim-fugitive"] = require("user.plugins.fugitive"),
  ["danymat/neogen"] = require("user.plugins.neogen"),
}
