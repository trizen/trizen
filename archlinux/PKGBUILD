# Maintainer: Trizen <echo dHJpemVueEBnbWFpbC5jb20K | base64 -d>

pkgname=trizen
pkgver=124.a52fc0c
pkgrel=1
pkgdesc="Trizen's AUR Package Manager: A lightweight wrapper for AUR."
arch=('any')
url="https://github.com/trizen/trizen"
license=('GPLv3');

makedepends=('git')
depends=(
         'perl>=5.10.0'
         'perl-libwww'
         'perl-term-ui'
         'pacman'
         'perl-json'
         'perl-data-dump'
         'perl-lwp-protocol-https'
         )

optdepends=(
            'perl-term-readline-gnu: for better STDIN support'
           )

source=('git://github.com/trizen/trizen.git')
md5sums=('SKIP')

pkgver() {
  cd $pkgname
  echo $(git rev-list --count master).$(git rev-parse --short master)
}

package() {
  cd $pkgname
  install -m 755 -D $pkgname "$pkgdir/usr/bin/$pkgname"
}
