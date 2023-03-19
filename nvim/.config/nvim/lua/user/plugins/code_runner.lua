return {
	"CRAG666/code_runner.nvim",
	opts = {
		-- choose default mode (valid term, tab, float, toggle, buf)
		mode = "float",
		-- Focus on runner window(only works on toggle, term and tab mode)
		focus = true,
		-- startinsert (see ':h inserting-ex')
		startinsert = false,
		term = {
			--  Position to open the terminal, this option is ignored if mode is tab
			position = "bot",
			-- window size, this option is ignored if tab is true
			size = 8,
		},
		float = {
			-- Key that close the code_runner floating window
			close_key = "<ESC>",
			-- Window border (see ':h nvim_open_win')
			border = "rounded",
			-- Num from `0 - 1` for measurements
			height = 0.35,
			width = 0.95,
			x = 0.5,
			y = 0.9,
			-- Highlight group for floating window/border (see ':h winhl')
			border_hl = "FloatBorder",
			float_hl = "Normal",
			-- Transparency (see ':h winblend')
			blend = 35,
		},
		filetype = {
			java = "cd $dir && javac $fileName && java $fileNameWithoutExt",
			python = "python3 -u",
			typescript = "deno run",
			rust = "cd $dir && rustc $fileName && $dir/$fileNameWithoutExt",
		},
		project = {},
	}
}
