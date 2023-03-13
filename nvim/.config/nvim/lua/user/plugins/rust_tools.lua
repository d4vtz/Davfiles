return {
	"simrat39/rust-tools.nvim",
	after = { "nvim-lspconfig", "mason-lspconfig.nvim" },                     -- make sure to load after mason-lspconfig
	opt = {
		server = require("astronvim.utils.lsp").server_settings("rust_analyzer"), -- get the server settings and built in capabilities/on_attach
	}
}
