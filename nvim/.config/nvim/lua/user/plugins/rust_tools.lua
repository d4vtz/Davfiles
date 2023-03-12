return {
	after = { "nvim-lspconfig", "mason-lspconfig.nvim" }, -- make sure to load after mason-lspconfig
	config = function()
		require("rust-tools").setup({
			server = astronvim.lsp.server_settings("rust_analyzer"), -- get the server settings and built in capabilities/on_attach
		})
	end,
}