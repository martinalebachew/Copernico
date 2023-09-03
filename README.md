# Copernico 🤔
Copernico is my NeoVim configuration based on NvChad and tailored to my specific needs and preferences. It's compatible with MacOS, Linux & Windows and includes
the following adjustments:

* No example configuration prompt.
* Safe installation commands with backups.
* Catppuccin as the default theme.
* GitHub Copilot NeoVim plugin pre-installed.
* Syntax highlighting for many of my favorite languages.
* Updated post-installation readme buffer.
* Tmux, TPM and VTN (Vim Tmux Navigator) included.


## macOS Configuration Guide

### Install prerequisites
```
brew install iterm2 neovim tmux
```
* Please install the [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) manually.
* You'll have to use iTerm2 since the macOS terminal has insufficient color support.

## Install TPM and VTN (Tmux-side)
```
rm -rf ~/.tmux.conf.backup ~/.tmux/plugins/tpm
mv ~/.tmux.conf ~/.tmux.conf.backup &> /dev/null
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
echo "set -g @plugin 'tmux-plugins/tpm'" >> ~/.tmux.conf
echo "set -g @plugin 'tmux-plugins/tmux-sensible'" >> ~/.tmux.conf
echo "set -g @plugin 'christoomey/vim-tmux-navigator'" >> ~/.tmux.conf
echo "run '~/.tmux/plugins/tpm/tpm'" >> ~/.tmux.conf
```

### Set up aliases
```
alias nv=nvim
echo 'alias nv=nvim' >> ~/.zshrc
```

### Set up iTerm2
Manual configuration:
* Install the [JetBrainsMono Font](https://www.jetbrains.com/lp/mono) and set it as the default terminal font.
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
