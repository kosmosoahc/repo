#!/usr/bin/env python3

from lilaclib import *
import fileinput
import re

depends = [
        'archlinuxcn-keyring'
        ]

build_prefix = 'archlinuxcn-x86_64'

post_build = aur_post_build

def _get_new_version():
  web = s.get('http://octave.sourceforge.net/signal/index.html')
  return re.search(r'\d\.\d\.\d', web.text).group()

def pre_build():
  aur_pre_build()
  ver = _get_new_version()
  with fileinput.input(files=('PKGBUILD'), inplace=1) as f:
    for l in f:
      l = l.rstrip('\n')
      if l.startswith('pkgver='):
        l = 'pkgver=' + ver
      if l.startswith('md5sums='):
        continue
      print(l)

  run_cmd('sh  -c  makepkg -g >> PKGBUILD'.split('  '))


if __name__ == '__main__':
  single_main()
