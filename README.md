trizen
======

trizen is a lightweight wrapper for AUR, written in Perl.

Main features include:
* Installation of packages from the AUR
* Search support for AUR packages
* Reading AUR comments for packages
* Upgrade support for AUR packages
* Recursive resolver of AUR dependencies
* Built-in interaction with 'pacman'
* Edit support for text files
* Input/output UTF-8 support

# INSTALLATION

* Tagged version:
```bash
git clone https://aur.archlinux.org/trizen.git
cd trizen
makepkg -si
```

* `-git` version:

```bash
git clone https://aur.archlinux.org/trizen-git.git
cd trizen-git
makepkg -si
```

# Screenshots

#### Search results

![trizen -Ss youtube](https://user-images.githubusercontent.com/614513/32417050-f5e5a310-c25b-11e7-8598-056431ce9a1d.png)

#### Package info

![trizen -Si sidef](https://user-images.githubusercontent.com/614513/32417040-d137a68a-c25b-11e7-89f3-362b084b8873.png)

#### Options

![trizen -h](https://user-images.githubusercontent.com/614513/32417044-dc3d6d6c-c25b-11e7-9ef4-ce9e3aa90a34.png)

# Usage

```
usage: trizen [option] [pkgname] [pkgname] [...]

Main options:
    -S              : installs package
    -Ss             : searches for package
    -Si             : outputs info for package
    -Sm             : outputs the packages maintained by [...]
    -Sp             : outputs PKGBUILD only
    -Sl             : builds and installs package from `pwd`
    -Syu            : upgrades installed packages
    -Sc             : clears the cache directory
    -C              : outputs AUR comments for a package
    -G              : clones a package in the current directory
    -Gd             : clones a package with all needed AUR dependencies
    -R              : removes packages (see pacman -Rh)
    -Q              : for installed packages (see pacman -Qh)
    -U              : installs local packages from '--clone-dir' or `pwd`

Other options:
    --quiet         : be quiet
    --really-quiet  : be really quiet
    --nocolors      : no text colors
    --aur           : only AUR actions (with -S, -Si, -Su, -Ss, -Sc)
    --asdeps        : installs packages as dependencies
    --asexplicit    : installs packages as explicitly installed
    --movepkg       : move built packages into pacman's cache directory
    --needed        : do not reinstall up-to-date packages
    --noedit        : do not prompt to edit files
    --nopull        : do not `git pull` new changes
    --nobuild       : do not build packages (implies --noedit)
    --noinstall     : do not install packages after building
    --noinfo        : do not display package info after cloning
    --devel         : update devel packages during -Su
    --show-ood      : show out-of-date flagged packages during -Su
    --noconfirm     : do not ask for any confirmation
    --force         : pass the --force option to pacman
    --skipinteg     : pass the --skipinteg option to makepkg
    --stats         : show some info about the installed packages
    --clone-dir=s   : directory where to clone and build packages
    --movepkg-dir=s : move built packages in this directory (with --movepkg)

Meta options:
    --debug         : activate the debug/verbose mode
    --help          : print this message and exit
    --version       : print version and exit
    --update-config : update the configuration file

:: Each config-key is a valid option when preceded with '--'

```

A configuration file is automatically generated at: `~/.config/trizen/trizen.conf`
