return {
  "sindrets/winshift.nvim",
  opts = {
    highlight_moving_win = true, -- Highlight the window being moved
    focused_hl_group = "Visual", -- The highlight group used for the moving window
    moving_win_options = {
      wrap = false,
      cursorline = false,
      cursorcolumn = false,
      colorcolumn = "",
    },
    keymaps = {
      disable_defaults = false, -- Disable the default keymaps
      win_move_mode = {
        ["h"] = "left",
        ["j"] = "down",
        ["k"] = "up",
        ["l"] = "right",
        ["H"] = "far_left",
        ["J"] = "far_down",
        ["K"] = "far_up",
        ["L"] = "far_right",
        ["<left>"] = "left",
        ["<down>"] = "down",
        ["<up>"] = "up",
        ["<right>"] = "right",
        ["<S-left>"] = "far_left",
        ["<S-down>"] = "far_down",
        ["<S-up>"] = "far_up",
        ["<S-right>"] = "far_right",
      },
    },
  },
}
