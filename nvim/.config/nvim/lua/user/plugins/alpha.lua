return {
	"goolord/alpha-nvim",
	lazy = true,
	enable = true,
	opts = function()
		local dashboard = require "alpha.themes.dashboard"

		dashboard.section.header.val = {
			"                                                     ",
			"  ███╗   ██╗███████╗ ██████╗ ██╗   ██╗██╗███╗   ███╗ ",
			"  ████╗  ██║██╔════╝██╔═══██╗██║   ██║██║████╗ ████║ ",
			"  ██╔██╗ ██║█████╗  ██║   ██║██║   ██║██║██╔████╔██║ ",
			"  ██║╚██╗██║██╔══╝  ██║   ██║╚██╗ ██╔╝██║██║╚██╔╝██║ ",
			"  ██║ ╚████║███████╗╚██████╔╝ ╚████╔╝ ██║██║ ╚═╝ ██║ ",
			"  ╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝     ╚═╝ ",
			"                                                     ",
		}
		dashboard.section.header.opts.hl = "DashboardHeader"

		local button = require("astronvim.utils").alpha_button
		dashboard.section.buttons.val = {
			button("LDR n", "  New File  "),
			button("LDR f f", "  Find File  "),
			button("LDR f o", "  Recents  "),
			button("LDR f w", "  Find Word  "),
			button("LDR f '", "  Bookmarks  "),
			button("LDR S l", "  Last Session  "),
		}

		dashboard.section.footer.val =
		{ "     Keep it simple, stupid!     ", "AstroNvim loaded " .. require("lazy").stats().count .. " plugins " }
		dashboard.section.footer.opts.hl = "DashboardFooter"

		dashboard.config.layout[1].val = vim.fn.max { 2, vim.fn.floor(vim.fn.winheight(0) * 0.2) }
		dashboard.config.layout[3].val = 5
		dashboard.config.opts.noautocmd = true
		return dashboard
	end
}
