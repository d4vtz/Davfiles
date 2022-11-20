return {
	settings = {
		texlab = {
			build = {
				executable = "latexmk",
				onSave = false,
				forwardSearchAfter = true,
				args = { "-pdf", "-interaction=nonstopmode", "-synctex=1", "-outdir", "%f" },
			},
			auxDirectory = "Build",
			forwardSearch = {
				executable = "zathura",
				args = { "--synctex-forward", "%l:1:%f", "%p" },
			},
			diagnostics = {
				ignoredPatterns = { "Underfull" },
			},
		},
	},
}
