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
    showbreak = "↪ ",
    wrap = true, -- soft wrap lines
    spellfile = "~/.config/astronvim/lua/user/spell/es.utf-8.add",
    thesaurus = "~/.config/astronvim/lua/user/spell/mthesaur.txt",
    swapfile = false,
  },
  g = {
    mapleader = " ", -- sets vim.g.mapleader
  },
}
