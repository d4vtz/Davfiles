return {
	-- keys = { "<F9>", "<F10>" },
	config = function()
		-- vim.g.vimtex_compiler_engine = "lualatex"
		vim.g.vimtex_view_method = "zathura"
		-- vim.g.vimtex_quickfix_enabled = 1
		-- vim.g.vimtex_quickfix_mode = 2
		-- vim.g.vimtex_quickfix_open_on_warning = 1
		vim.g.vimtex_compiler_latexmk = {
			build_dir = "Build",
			callback = 1,
			continuous = 1,
			executable = "latexmk",
			hooks = {},
			options = {
				"-verbose",
				"-file-line-error",
				"-synctex=1",
				"-interaction=nonstopmode",
			},
		}
	end,
}
