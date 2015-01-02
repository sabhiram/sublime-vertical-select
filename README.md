#sublime-vertical-select
[![Build Status](https://travis-ci.org/sabhiram/sublime-vertical-select.svg?branch=master)](https://travis-ci.org/sabhiram/sublime-vertical-select)

SublimeText plugin to select the same position of the previous / next line

![](https://raw.githubusercontent.com/sabhiram/public-images/master/sublime-vertical-select/sublime-vertical-select.gif)

## Usage:

To select the same position in the previous line press:

|    OS   | Key Combination  |
| ------- | ---------------  |
| Linux   | alt + shift + up |
| Mac     | alt + shift + up |
| Windows | alt + shift + up |

To select the same position in the next line press:

|    OS   | Key Combination    |
| ------- | ---------------    |
| Linux   | alt + shift + down |
| Mac     | alt + shift + down |
| Windows | alt + shift + down |

## Installation

The easiest way to install `Vertical Select` is to install it from Package Control

### Package Control Install

If you have [Package Control](https://sublime.wbond.net/installation) installed, then simply naviagte to `Package Control: Install Package` and select the `Vertical Select` plugin and you are done!

### Manual Install 

From SublimeText `Packages` folder:
```sh
git clone git@github.com:sabhiram/sublime-vertical-select.git sublime-vertical-select
```

## Settings & Default Key Mapping

Currently there are no settings exposed. To override the keybinding for these keys, bind the `vertical_select_up` and `vertical_select_down` commands in your User keymap file

## Developers

Appreciate the help! Here is stuff you should probably know:

### Install for both Sublime Text 2 and 3:

Some folks prefer to clone the git repo right into their SublimeText `Packages` folder. While this is probably ok for most users, I prefer to create a symbolic link to the package so that I can point to the plugin from both flavors of SublimeText (for testing and the like...)

```
cd ~/dev
git clone git@github.com:sabhiram/sublime-vertical-select.git sublime-vertical-select
ln -s sublime-vertical-select ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/sublime-vertical-select
ln -s sublime-vertical-select ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/sublime-vertical-select 
```

### Running Tests & CI 

This project, and any pull requests will automatically be run against [Travis CI](https://travis-ci.org/sabhiram/sublime-vertical-select). For local development, the tests assume that the following are installed and configured:

Hopefully you have [Sublime Text](http://www.sublimetext.com/3) installed

Next make sure you have [Package Control](https://sublime.wbond.net/installation) installed as well (and you really should, it's awesome!)

Via the SublimeText Package Control, install the `UnitTesting` package. You can do this by hitting `ctrl + shift + p`, then select `Package Control: Install Package`. Once the menu loads, choose the `UnitTesting` package.

To run the tests: `ctrl + shift + p` then select `UnitTesting: Run any project test suite` and type in the name of this package (in my case, and typically `sublime-vertical-select` but is basically the name of the folder which you chose to clone the repo into).

### Sublime Text API Reference

[Sublime Text 2 API](https://www.sublimetext.com/docs/2/api_reference.html)

[Sublime Text 3 API](https://www.sublimetext.com/docs/3/api_reference.html)
