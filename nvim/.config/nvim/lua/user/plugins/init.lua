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
	["simrat39/rust-tools.nvim"] = {
		after = { "nvim-lspconfig", "mason-lspconfig.nvim" }, -- make sure to load after mason-lspconfig
		config = function()
			require("rust-tools").setup({
				server = astronvim.lsp.server_settings("rust_analyzer"), -- get the server settings and built in capabilities/on_attach
			})
		end,
	},
	["nyngwang/NeoRoot.lua"] = {
		config = function()
			require("neo-root").setup({
				CUR_MODE = 2, -- 1 for file/buffer mode, 2 for proj-mode
			})
		end,
	},
	["hrsh7th/cmp-nvim-lsp-signature-help"] = {
		after = "nvim-cmp",
		config = function()
			astronvim.add_user_cmp_source("cmp_nvim_lsp_signature_help")
		end,
	},
	["j-hui/fidget.nvim"] = {
		config = function()
			require("fidget").setup({})
		end,
	},
	require("user.plugins.fugitive"),
}
