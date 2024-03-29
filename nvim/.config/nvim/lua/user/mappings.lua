-- My mappings
return {
	n = {
		["<leader>bb"] = { "<cmd>tabnew<cr>", desc = "New tab" },
		["<leader>bc"] = { "<cmd>BufferLinePickClose<cr>", desc = "Pick to close" },
		["<leader>bj"] = { "<cmd>BufferLinePick<cr>", desc = "Pick to jump" },
		["<leader>bt"] = { "<cmd>BufferLineSortByTabs<cr>", desc = "Sort by tabs" },
		-- quick save
		["<C-s>"] = { ":w!<cr>", desc = "Save File" }, -- change description but the same command
		["<F12>"] = { "<cmd>TroubleToggle document_diagnostics<cr>", desc = "Open Trouble" },
		["<F11>"] = { "<cmd>TroubleRefresh<cr>", desc = "Trouble Refresh" },
		-- Compilacion de LaTex
		["<F9>"] = { "<cmd>VimtexCompile<cr>", desc = "Compile latex" },
		["<F8>"] = { "<cmd>VimtexView<cr>", desc = "View compile pdf" },
		["<C-b>"] = { "<cmd>Telescope bibtex<cr>", desc = "Telescope bibtex" },
		["<C-w>"] = { "<cmd>HopWord<cr>", desc = "Lanzar HopWord" },
		["<C-c>"] = { "<cmd>HopChar2<cr>" },
		["<leader>r"] = { ":RunCode<CR>", desc = "Run Code" },
		-- Desactive arrows
		["<Left>"] = { "<Nop>" },
		["<Right>"] = { "<Nop>" },
		["<Up>"] = { "<Nop>" },
		["<Down>"] = { "<Nop>" },
		["j"] = { "gj" },
		["k"] = { "gk" },
	},
	t = {
		-- setting a mapping to false will disable it
		-- ["<esc>"] = false,
		["<esc>"] = { "<C-\\><C-n>", desc = "Terminal normal mode" },
	},
}
