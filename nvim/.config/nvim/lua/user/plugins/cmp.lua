local compare = require("cmp.config.compare")

return {
	completion = {
		completeopt = "menu,menuone,noinsert",
		keyword_length = 2,
	},
	source_priority = {
		luasnip = 1000,
		cmp_nvim_lsp_signature_help = 900,
		nvim_lua = 800,
		nvim_lsp = 700,
		path = 500,
		buffer = 250,
	},
	formatting = {
		format = function(entry, vim_item)
			return require("lspkind").cmp_format(astronvim.lspkind)(entry, vim_item)
		end,
		sorting = {
			priority_weight = 2,
			comparators = {
				compare.kind,
				compare.sort_text,
			},
		},
	},
}
