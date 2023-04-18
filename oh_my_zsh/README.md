# How to install & configure OhMyZsh

PreRequisites zsh and iTerm2 (other terminal) must be installed

1. Install OhMyZsh
```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
2. Install zsh-autosuggestions
```
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
```
3. Install zsh-syntax-highlighting
```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```
4. Add zsh-autosuggestions & zsh-syntax-highlighting to plugins() section
```
vi ~/.zshrc
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
```
5. Install Powerlevel10k themes
```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```
6. Add Powerlevel10k theme to .zshrc
```
vi ~/.zshrc
ZSH_THEME="powerlevel10k/powerlevel10k"
```
7. Activate the changes in .zshrc
```
source ~/.zshrc
```
8. Follow the prompts to configure powerlevel10k

### Installing Zsh in Windows Git Bash

[Click Here](https://dominikrys.com/posts/zsh-in-git-bash-on-windows/)
