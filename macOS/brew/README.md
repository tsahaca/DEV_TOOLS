# Home Brew CheatSheet

## brew commands

| **Use Case** | **Command** |
|--------------|-------------|
| To check if a package was installed by brew | brew info \<package name\> |
| To list all packages installed by brew | brew deps --tree --installed | 
| To update a package | brew upgrade \<package name\> |
| To link the newly upgraded package | brew link --overwrite \<package name\> |

## Commands

| **Command**  | **Use Case** |
|--------------|--------------|
| brew install git	| Install a package |
| brew uninstall git	| Remove/Uninstall a package |
| brew upgrade git	| Upgrade a package |
| brew unlink git	| Unlink |
| brew link git	| Link |
| brew switch git 2.5.0	| Change versions |
| brew list --versions git	| See what versions you have |

## More package commands

| **Command**  | **Use Case** |
|--------------|--------------|
|brew info git	| List versions, caveats, etc |
|brew cleanup git	| Remove old versions |
|brew edit git	| Edit this formula |
|brew cat git	| Print this formula |
|brew home git	| Open homepage |
|brew search git	| Search for formulas |


## Global commands

| **Command**  | **Use Case** |
|--------------|--------------|
| brew update	| Update brew and cask |
| brew upgrade	| Upgrade all packages |
| brew list	| List installed |
| brew outdated	| What’s due for upgrades? |
| brew doctor	| Diagnose brew issues |

## Brew Cask commands

| **Command**  | **Use Case** |
|--------------|--------------|
| brew install --cask firefox	| Install the Firefox browser |
| brew list --cask	| List installed applications |

### Cask commands are used for interacting with graphical applications.

### [Homebrew - Basics Commands and Cheatsheet](https://dev.to/andremare/homebrew---basics--cheatsheet-3a3n)
