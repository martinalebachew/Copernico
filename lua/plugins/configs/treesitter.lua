local options = {
  ensure_installed = { "bash", "c", "c_sharp", "comment", "cpp", "css", "dart", "dockerfile", "gitignore", "html", "java", "javascript", "json", "latex", "lua", "make", "markdown", "markdown_inline", "ninja", "proto", "python", "regex", "rust", "sql", "swift", "tsx", "typescript", "vim", "yaml" },
  auto_install = true,

  highlight = {
    enable = true,
    use_languagetree = true,
  },

  indent = { enable = true },
}

return options
