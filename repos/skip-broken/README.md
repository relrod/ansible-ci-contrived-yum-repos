# skip-broken

This builds three packages, `broken-a`, `broken-b`, `broken-c`.

It builds two versions of `broken-a`, 1.2.3, and 1.2.4.

`broken-b` depends on `broken-a-1.2.3`.

`broken-c` depends on `broken-a-1.2.4`.

Cue fun.
