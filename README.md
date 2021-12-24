# dotfiles
Setup a new Mac

## Pre Bootstrap: Install XCode Tools
* Download Xcode from the App Store
* Install developer tools `xcode-select --install`

## Bootstrap
```
./bootstrap-mac-personal

# If at work you must be off VPN else Github will throttle you
./script/fetch-my-tools
```

## Post bootstrap
### Install Sublime Text
* https://www.sublimetext.com/download

### Install  VS Code
* [Install VS Code](https://code.visualstudio.com)

### Mac App Store
* [Things](https://apps.apple.com/us/app/things-3/id904280696?mt=12)
* [Fantastical](https://apps.apple.com/us/app/fantastical-calendar-tasks/id975937182?mt=12)
* [Magnet](https://apps.apple.com/us/app/magnet/id441258766?mt=12)
* [iA Writer](https://apps.apple.com/us/app/ia-writer/id775737590?mt=12)
* [Kaleidoscope](https://apps.apple.com/us/app/kaleidoscope/id587512244?mt=12)

### Others
* [Alfred](https://www.alfredapp.com)

## Dracula
[Install Dracula theme for the following applications](https://draculatheme.com/)

- [ ] [Terminal](https://draculatheme.com/terminal)
- [ ] [VS Code](https://draculatheme.com/visual-studio-code)
- [ ] [Chrome](https://draculatheme.com/chrome)
- [ ] [Slack](https://draculatheme.com/slack)

### OS Settings
#### System Preferences
* Map Caps Lock to Control
* Map cmd+shift+\ to show notification center


### App Specific
#### Terminal
* set font to `Menlo Regular for Powerline` @ 14pt

## Appendix
### Lazy Loading Program Runtimes
https://frederic-hemberger.de/notes/shell/speed-up-initial-zsh-startup-with-lazy-loading/

````zsh
ruby() {
  unfunction $0
  eval "$(rbenv init -)"
  $0 "$@"
}

```
