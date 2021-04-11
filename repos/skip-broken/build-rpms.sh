#!/usr/bin/env bash

set -e

for spec in SPECS/*.spec; do
  rpmbuild -ba "$spec" --define "_topdir $(pwd)"
done

# And build 'a' again with a different version
rpmbuild -ba SPECS/broken-a.spec --define "_topdir $(pwd)" --define "_pkgversion 1.2.4"

# and again for a conditional requires
rpmbuild -ba SPECS/broken-a.spec --define "_topdir $(pwd)" --define "_pkgversion 2.0.0"

# and again for a conditional requires that we can downgrade to (so can't be max version)
rpmbuild -ba SPECS/broken-a.spec --define "_topdir $(pwd)" --define "_pkgversion 1.2.3.4"

pushd RPMS
  createrepo .
popd
