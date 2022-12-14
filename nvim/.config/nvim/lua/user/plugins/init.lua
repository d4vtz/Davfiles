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
  ["simrat39/rust-tools.nvim"] = {},
}
