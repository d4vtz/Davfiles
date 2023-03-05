return function()
	-- Set key binding
	-- Set autocommands
	-- vim.api.nvim_create_augroup("packer_conf", { clear = true })
	-- vim.api.nvim_create_autocmd("BufWritePost", {
	--   desc = "Sync packer after modifying plugins.lua",
	--   group = "packer_conf",
	--   pattern = "plugins.lua",
	--   command = "source <afile> | PackerSync",
	-- })

	-- Set up custom filetypes
	-- vim.filetype.add {
	--   extension = {
	--     foo = "fooscript",
	--   },
	--   filename = {
	--     ["Foofile"] = "fooscript",
	--   },
	--   pattern = {
	--     ["~/%.config/foo/.*"] = "fooscript",
	--   },
	-- }
	vim.cmd [[
inoremap <C-f> <Esc>: silent exec '.!inkscape-figures create "'.getline('.').'" "'.b:vimtex.root.'/figures/"'<CR><CR>:w<CR>
nnoremap <C-f> : silent exec '!inkscape-figures edit "'.b:vimtex.root.'/figures/" > /dev/null 2>&1 &'<CR><CR>:redraw!<CR>
]]
end
