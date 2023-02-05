return {
	"danymat/neogen",
	dependencias = "nvim-treesitter/nvim-treesitter",
	cmd = { "Neogen" },
	config = function()
		require("neogen").setup({ snippet_engine = "luasnip" })
	end,
}
