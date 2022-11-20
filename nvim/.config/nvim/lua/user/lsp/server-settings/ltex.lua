return {
	on_attach = function(client, bufnr)
		-- your other on_attach functions.
		require("ltex_extra").setup({
			load_langs = { "es", "en-US" }, -- table <string> : languages for witch dictionaries will be loaded
			init_check = true, -- boolean : whether to load dictionaries on startup
			log_level = "none", -- string : "none", "trace", "debug", "info", "warn", "error", "fatal"
		})
	end,
	settings = {
		ltex = {
			enabled = { "latex", "tex", "bib", "markdown" },
			language = "es",
			additionalRules = { motherTongue = { "en" } },
			latex = {
				environments = { lstlisting = "ignore", verbatim = "ignore", equation = "ignore" },
				commands = { label = "ignore", "\\ref{}" == "ignore" },
			},
		},
	},
}
