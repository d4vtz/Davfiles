return {
	after = "nvim-cmp",
	config = function()
		astronvim.add_user_cmp_source("cmp_nvim_lsp_signature_help")
	end,
}
