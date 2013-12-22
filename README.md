trizen
======

trizen is a lightweight wrapper for AUR written in Perl.

Main features:

* Install packages from AUR
* Search for packages in AUR
* Read package comments from AUR
* Full AUR dependencies support
* Update the packages from AUR
* Can interact with 'pacman'
* Edit support for TXT files

It has a syntax similar with pacman:

    -S              : installs package
    -Ss             : searches for package
    -Si             : outputs info for package
    -Sm             : outputs the packages maintained by [...]
    -Sp             : outputs PKGBUILD only
    -Su             : upgrades installed packages
    -Sc             : clears the cache directory
    -C              : outputs AUR comments only
    -G              : download and extract AUR tarball only
    -R              : remove packages (see pacman -Rh)
    -Q              : for installed packages (see pacman -Qh)
    -U              : installs local packages from /tmp or CWD

But it has other options too:

    --quiet         : be quiet
    --really_quiet  : be really quiet
    --force         : set --force argument for makepkg and pacman
    --nocolors      : no text colors
    --aur           : only AUR packages (for: -S, -Si, -Su, -Ss)
    --asdep         : installs package as dependency
    --noinstall     : build package only, don't install it
    --movepkg       : move the built package to the pacman cache directory
    --needed        : don't reinstall up to date packages
    --noedit        : do not prompt to edit files
    --devel         : update devel packages during -Su
    --show_ood      : show out-of-date flagged packages during -Su
    --noconfirm     : do not prompt for any confirmation
    --skipinteg     : when using makepkg, skip the checksum
    --stats         : show some info about the installed packages
    --update_config : update configuration file before exit
    --movepkg_dir=s : move built packages in this directory (with --movepkg)

And a configuration file which can be found in:
~/.config/trizen/trizen.conf
