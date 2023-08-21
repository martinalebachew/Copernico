# Copernico 🤔
Copernico is my NeoVim configuration based on NvChad and tailored to my specific needs and preferences. It's compatible with MacOS, Linux & Windows and includes
the following adjustments:

* No example configuration prompt.
* Safe installation commands with backups.
* Catppuccin as the default theme.
* GitHub Copilot NeoVim plugin pre-installed.
* Syntax highlighting for many of my favorite languages.
* Updated post-installation readme buffer.


## macOS Configuration Guide

### Install prerequisites
```
brew install iterm2 neovim
```
You'll have to use iTerm2 since the macOS terminal has insufficient color support.

### Set up aliases
```
alias nv=nvim
echo 'alias nv=nvim' >> ~/.zshrc
```

### Set up iTerm2
Manual configuration:
* Install [JetBrainsMono Nerd Font](https://www.nerdfonts.com/font-downloads) and set it as the default terminal font.
* Choose JetbrainsMono Nerd Font and **not** ~~JetbrainsMono Nerd Font Mono~~ to avoid small icons.
* Change default font size to 20pt.
* Using the menu bar, lick iTerm2 > Make iTerm2 Default Term.

### Install NvConfig
```
rm -rf ~/.config/nvim.backup
mv ~/.config/nvim ~/.config/nvim.backup &> /dev/null
rm -rf ~/.local/share/nvim
git clone https://github.com/martinalebachew/Copernico ~/.config/nvim --depth 1 && nv
```

### Configure Copilot
GitHub Copilot plugin for NeoVim comes preinstalled with Copernico. It is recommended to invoke `:Copilot setup` to finalize installation.
