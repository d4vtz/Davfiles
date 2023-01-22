return {
	completion = {
		completeopt = "menu,menuone,noinsert",
		keyword_length = 2,
	},
	source_priority = {
		luasnip = 1000,
		nvim_lua = 800,
		nvim_lsp = 700,
		path = 500,
		buffer = 250,
	},
}
