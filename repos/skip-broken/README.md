# skip-broken

---

NOTE!!! If you are an Ansible developer reading this from S3, do not update
the files there! Update them here: https://github.com/relrod/ansible-ci-contrived-yum-repos/
and then copy the repo over from the artifact that gets built in GitHub Actions.

---

This builds three packages, `broken-a`, `broken-b`, `broken-c`.

It builds three versions of `broken-a`, 1.2.3, 1.2.3.4, 1.2.4, 2.0.0.

`broken-a-1.2.3.4` and `broken-a-2.0.0` depend on a nonexistent package, the other versions do not.

`broken-b` depends on `broken-a-1.2.3`.

`broken-c` depends on `broken-a-1.2.4`.

`broken-d` depends on `broken-a` (no version constraint).

Cue fun.
