return {
  { -- statusline
    hl = { fg = "fg", bg = "bg" },
    astronvim.status.component.mode(),
    astronvim.status.component.git_branch(),
    astronvim.status.component.file_info(
      (astronvim.is_available("bufferline.nvim") or vim.g.heirline_bufferline)
      and { filetype = {}, filename = false, file_modified = false }
      or nil
    ),
    astronvim.status.component.git_diff(),
    astronvim.status.component.diagnostics(),
    astronvim.status.component.fill(),
    astronvim.status.component.cmd_info(),
    astronvim.status.component.fill(),
    astronvim.status.component.lsp({ lsp_progress = false }),
    astronvim.status.component.treesitter(),
    astronvim.status.component.nav(),
    astronvim.status.component.mode({ surround = { separator = "right" } }),
  },
  { -- winbar
    static = {
      disabled = {
        buftype = { "terminal", "prompt", "nofile", "help", "quickfix" },
        filetype = { "NvimTree", "neo%-tree", "dashboard", "Outline", "aerial" },
      },
    },
    init = function(self)
      self.bufnr = vim.api.nvim_get_current_buf()
    end,
    fallthrough = false,
    { -- disable winbar for some buffer and file types
      condition = function(self)
        return vim.opt.diff:get() or astronvim.status.condition.buffer_matches(self.disabled or {})
      end,
      init = function()
        vim.opt_local.winbar = nil
      end,
    },
    -- inactive buffer winbar
    astronvim.status.component.file_info({
      condition = function()
        return not astronvim.status.condition.is_active()
      end,
      unique_path = {},
      file_icon = { hl = astronvim.status.hl.file_icon("winbar") },
      file_modified = false,
      file_read_only = false,
      hl = astronvim.status.hl.get_attributes("winbarnc", true),
      surround = false,
      update = "BufEnter",
    }),
    -- active buffer winbar
    astronvim.status.component.breadcrumbs({ hl = astronvim.status.hl.get_attributes("winbar", true) }),
  },
  { -- bufferline
    { -- file tree padding
      condition = function(self)
        self.winid = vim.api.nvim_tabpage_list_wins(0)[1]
        return astronvim.status.condition.buffer_matches(
          { filetype = { "neo%-tree", "NvimTree" } },
          vim.api.nvim_win_get_buf(self.winid)
        )
      end,
      provider = function(self)
        return string.rep(" ", vim.api.nvim_win_get_width(self.winid))
      end,
      hl = { bg = "tabline_bg" },
    },
    -- component for each buffer tab
    astronvim.status.heirline.make_buflist(astronvim.status.component.tabline_file_info()),
    -- fill the rest of the tabline with background color
    astronvim.status.component.fill({ hl = { bg = "tabline_bg" } }),
    -- tab list
    {
      -- only show tabs if there are more than one
      condition = function()
        return #vim.api.nvim_list_tabpages() >= 2
      end,
      -- create components for each tab page
      astronvim.status.heirline.make_tablist({ -- component for each tab
        provider = astronvim.status.provider.tabnr(),
        hl = function(self)
          return astronvim.status.hl.get_attributes(astronvim.status.heirline.tab_type(self, "tab"), true)
        end,
      }),
      -- close button for current tab
      {
        provider = astronvim.status.provider.close_button({
          kind = "TabClose",
          padding = { left = 1, right = 1 },
        }),
        hl = astronvim.status.hl.get_attributes("tab_close", true),
        on_click = { callback = astronvim.close_tab, name = "heirline_tabline_close_tab_callback" },
      },
    },
  },
}
