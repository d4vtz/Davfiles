return {
  "onsails/lspkind.nvim",
  opts = function(_, opts)
    opts.mode = "symbol"
    opts.symbol_map = {
      NONE = "",
      Array = " ",
      Boolean = "⊨ ",
      Class = " ",
      Constructor = " ",
      Key = " ",
      Namespace = " ",
      Null = "NULL",
      Number = "#",
      Object = "⦿ ",
      Package = " ",
      Property = " ",
      Reference = " ",
      Snippet = " ",
      String = "𝓐",
      TypeParameter = "",
      Unit = " ",
    }
    opts.menu = {
      buffer = "[Buf]",
      nvim_lsp = "[LSP]",
      nvim_lua = "[Api]",
      path = "[Path]",
      luasnip = "[Snip]",
    }
    return opts
  end,
}
