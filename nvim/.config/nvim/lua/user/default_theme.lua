-- Default theme configuration
return {
	-- set the highlight style for diagnostic messages
	highlights = function(hl)
		-- New approach instead of diagnostic_style
		hl.DiagnosticError.italic = true
		hl.DiagnosticHint.italic = true
		hl.DiagnosticInfo.italic = true
		hl.DiagnosticWarn.italic = true

		return hl
	end,
	-- enable or disable highlighting for extra plugins
	plugins = {
		aerial = true,
		beacon = false,
		bufferline = true,
		dashboard = true,
		highlighturl = true,
		hop = false,
		indent_blankline = true,
		lightspeed = false,
		["neo-tree"] = true,
		notify = true,
		["nvim-tree"] = false,
		["nvim-web-devicons"] = true,
		rainbow = true,
		symbols_outline = false,
		telescope = true,
		vimwiki = false,
		["which-key"] = true,
	},
}
