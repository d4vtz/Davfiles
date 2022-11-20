-- set vim options here (vim.<first_key>.<second_key> =  value)
return {
	opt = {
		relativenumber = true, -- sets vim.opt.relativenumber
		conceallevel = 2, -- enable conceal
		linebreak = true, -- linebreak soft wrap at words
		list = true, -- show whitespace characters
		listchars = {
			tab = "│→",
			extends = "⟩",
			precedes = "⟨",
			trail = "·",
			nbsp = "␣",
			eol = "↲",
		},
		shortmess = vim.opt.shortmess + { I = true },
		showbreak = "↪ ",
		wrap = true, -- soft wrap lines
		spellfile = "~/.config/astronvim/lua/user/spell/es.utf-8.add",
		thesaurus = "~/.config/astronvim/lua/user/spell/mthesaur.txt",
	},
	g = {
		mapleader = " ", -- sets vim.g.mapleader
	},
}
