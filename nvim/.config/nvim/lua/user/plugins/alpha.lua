local if_nil = vim.F.if_nil
local leader = "SPC"

local function button(sc, txt, keybind, keybind_opts)
	local sc_ = sc:gsub("%s", ""):gsub(leader, "<leader>")

	local opts = {
		position = "center",
		shortcut = sc,
		cursor = 5,
		width = 50,
		align_shortcut = "right",
		hl_shortcut = "Keyword",
	}
	if keybind then
		keybind_opts = if_nil(keybind_opts, { noremap = true, silent = true, nowait = true })
		opts.keymap = { "n", sc_, keybind, keybind_opts }
	end

	local function on_press()
		local key = vim.api.nvim_replace_termcodes(keybind or sc_ .. "<Ignore>", true, false, true)
		vim.api.nvim_feedkeys(key, "t", false)
	end

	return {
		type = "button",
		val = txt,
		on_press = on_press,
		opts = opts,
	}
end

return {
	layout = {
		{ type = "padding", val = vim.fn.max({ 2, vim.fn.floor(vim.fn.winheight(0) * 0.2) }) },
		{
			type = "text",
			val = astronvim.user_plugin_opts("header", nil, false),
			opts = {
				position = "center",
				hl = "DashboardHeader",
			},
		},
		{ type = "padding", val = 5 },
		{
			type = "group",
			val = {
				button("LDR f f", "  Find File", ":Telescope find_files<cr>"),
				button("LDR f o", "  Recents", ":Telescope oldfiles<cr>"),
				button("LDR f w", "  Find Word", ":Telescope live_grep<cr>"),
				button("LDR f p", "  Projects", ":Telescope projects<cr>"),
				button("LDR f n", "  New File  ", ":ene<cr>"),
				button("LDR S l", "  Last Session", ":Sesion<cr>"),
			},
			opts = {
				spacing = 1,
			},
		},

		{
			type = "text",
			val = {
				" ",
				" ",
				"Keep It Simple, Stupid",
			},
			opts = {
				position = "center",
				hl = "DashboardFooter",
			},
		},
	},
}
