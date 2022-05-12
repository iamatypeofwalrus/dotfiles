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
* TK time tracker app

### Dracula Themes
[Install Dracula theme for the following applications](https://draculatheme.com/)

* [Terminal](https://draculatheme.com/terminal)
* [VS Code](https://draculatheme.com/visual-studio-code)
* [Chrome](https://draculatheme.com/chrome)
* [Slack](https://draculatheme.com/slack)

### Mac OS Preferences
#### System Preferences
* Map Caps Lock to Control
* Map cmd+shift+\ to show notification center

#### Magnet Shortcuts
* Left Third  - ctrl + alt + cmd + left
* Right Third - ctrl + alt + cmd + right
* Left Two Thirds - ctrl + alt + cmd + up
* Right Two Thirds - ctrl + alt + cmd + down

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

## Appendix
### Github Codespace: use zsh when connecting over ssh
```
gh codespace ssh -- -t 'zsh -l'
```

### Lazy Loading Program Runtimes
https://frederic-hemberger.de/notes/shell/speed-up-initial-zsh-startup-with-lazy-loading/

````zsh
ruby() {
  unfunction $0
  eval "$(rbenv init -)"
  $0 "$@"
}

```
