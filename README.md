# dotfiles
Setup a new computer

## Personal Mac
### Pre Bootstrap: Install XCode Tools
* Download Xcode from the App Store
* Install developer tools `xcode-select --install`

## Work Mac

## Linux

## Bootstrap
```
./bootstrap

# If at work you must be off VPN else Github will throttle you
./script/install-personal-binaries
```

## Mac Apps
### Install Sublime Text
* https://www.sublimetext.com/download

### Install VS Code
* [Install VS Code](https://code.visualstudio.com)

### Mac App Store
* [Things](https://apps.apple.com/us/app/things-3/id904280696?mt=12)
* [Fantastical](https://apps.apple.com/us/app/fantastical-calendar-tasks/id975937182?mt=12)
* [Magnet](https://apps.apple.com/us/app/magnet/id441258766?mt=12)
* [iA Writer](https://apps.apple.com/us/app/ia-writer/id775737590?mt=12)
* [Kaleidoscope](https://apps.apple.com/us/app/kaleidoscope/id587512244?mt=12)

### Others
* [Alfred](https://www.alfredapp.com)
* [Timer app](https://github.com/michaelvillar/timer-app)
* [1Password](https://1password.com)
* [1Password for Safari]()
* [Docker](https://www.docker.com)
* [Airbuddy](https://v2.airbuddy.app/download)

### Dracula Themes
[Install Dracula theme for the following applications](https://draculatheme.com/)

* [Terminal](https://draculatheme.com/terminal)
* [VS Code](https://draculatheme.com/visual-studio-code)
    * this should be handled automatically by VS Code Settings Sync

### Python on Mac
* [Install from Conda](https://www.anaconda.com/products/distribution)
* re-bootstrap to remove CONDA cruft from zshrc

### Mac OS Preferences
#### Modifier Keys
* Caps Lock to Control

#### System Preferences
* Map cmd+shift+\ to show notification center

#### Magnet Shortcuts
* Left - ctrl + cmd + left
* Right - ctrl - cmd + right

* Left Third  - ctrl + alt + cmd + left
* Right Third - ctrl + alt + cmd + right
* Left Two Thirds - ctrl + alt + cmd + up
* Right Two Thirds - ctrl + alt + cmd + down

* maximize - ctrl + alt + cmd + m

#### Things shortcuts
* New todo - ctrl + cmd + space
* helper todo - ctrl + alt + cmd + space

#### Mac OS Hot Corners
* Upper left - Mission control
* lower left - desktop
* Upper Right - application windows
* lower left - quick note

#### Terminal
* set font to `Menlo Regular for Powerline` @ 14pt

#### Mail.app
* "Show most recent messages at the top"

## Appendix
### Github Codespace: use zsh when connecting over ssh
```
gh codespace ssh -- -t 'zsh -l'
```
