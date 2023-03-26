return {
	settings = {
		texlab = {
			auxDirectory = "Build",
			outputDirectory = "Build",
			build = {
				executable = "latexmk",
				onSave = false,
				forwardSearchAfter = true,
				args = { "-pdf", "-pvc", "-interaction=nonstopmode", "-synctex=1", "-outdir=./Build", "-aux-directory=./Build",
					"%f" },
			},
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
