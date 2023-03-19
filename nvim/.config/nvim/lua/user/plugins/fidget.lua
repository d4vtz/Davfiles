return {
	"j-hui/fidget.nvim",
	event = "VeryLazy",
	opts = {
		sources = {
			["null-ls"] = {
				ignore = true
			}
		}
	},
	config = function()
		require("fidget").setup {}
	end,
}
