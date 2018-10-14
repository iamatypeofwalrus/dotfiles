# dotfiles
Setup a new Mac

## Prerequisites
* Download Xcode from the App Store
* Install developer tools `xcode-select --install`

## bootstrap
```
./bootstrap
```

## Manual Setup
### System Preferences
* Map Caps Lock to Control
### VS Code
* [Install VS Code](https://code.visualstudio.com)
* [Install Dracula theme for VS Code](https://github.com/dracula/visual-studio-code)
### Terminal
* [Install Dracula theme for Terminal](https://github.com/dracula/terminal-app)
* set font to `Menlo Regular for Powerline` @ 14pt

### Python
#### Install the latest versions of Python 2 and 3
```
pyenv install --list
pyenv install YOUR_PYTHON_2
pyenv install YOUR_PYTHON_3
pyenv rehash
pyenv global YOUR_PYTHON_3
```

### post bootstrap
Prefer installing the AWS CLI after pyenv is bootstrapped into your zshrc rather than against the system python which is old a.f.

```
./post-bootstrap
```
