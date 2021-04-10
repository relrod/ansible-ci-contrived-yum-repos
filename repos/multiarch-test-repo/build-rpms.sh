#!/usr/bin/env bash

for spec in SPECS/*.spec; do
  rpmbuild -ba "$spec" --define "_topdir $(pwd)" --target i686,x86_64 --define "_pkgversion 1.0"
  rpmbuild -ba "$spec" --define "_topdir $(pwd)" --target i686,x86_64 --define "_pkgversion 2.0"
done

pushd RPMS
  createrepo .
popd
