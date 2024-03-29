The APT package manager used in the Debian and Ubuntu Linux distros
keeps track of installed packages, but also which files they
installed. Here are four package management commands I have ended up
using regularly.

## What package does this file belong to?

If you know the path to a file (for example a configuration file) you
can find name of the package it belongs to by running `dpkg`:

    $ dpkg -S /etc/smartd.conf
    smartmontools: /etc/smartd.conf

In this example the `smartmontools` package provides the
`/etc/smartd.conf` file.

You might want to know which package provides a tool you have been
using. A common scenario is when you have a tool available on your
computer, you want to run it on another computer, and you don't recall
how you installed the tool. Simply pass the command name through the
`which` command to get the full path and use `dpkg` again to find the
owning package:

    $ dpkg -S `which sendmail`
    msmtp-mta: /usr/sbin/sendmail

In this example the `msmtp-mta` package provides the `sendmail`
command. In general, the package name might not be obvious, especially
if multiple packages can provide the same file.

## Which package version do I have?

Checking which version of a package you gave installed is useful for
knowing which features are supported by that version. The version is
easily checked check using `apt-cache` when you have the package name:

    $ apt-cache policy msmtp-mta
    msmtp-mta:
      Installed: 1.8.6-1
      Candidate: 1.8.6-1
      Version table:
     *** 1.8.6-1 500
            500 http://se.archive.ubuntu.com/...
            100 /var/lib/dpkg/status

In this example the version of the installed `msmtp-mta` package is
`1.8.6-1`.

## What files did the package install?

Sometimes you know that a package did install something, but not
exacly where. This could be an example file, documentation, a utility
command, an init script, a library, etc. Given a package name the
`dpkg` command can list the files that the package installed:

    $ dpkg -L endlessh
    /.
    /etc
    /etc/init.d
    /etc/init.d/endlessh
    /lib
    /lib/systemd
    /lib/systemd/system
    /lib/systemd/system/endlessh.service
    /usr
    /usr/bin
    /usr/bin/endlessh
    /usr/share
    /usr/share/doc
    /usr/share/doc/endlessh
    /usr/share/doc/endlessh/README.Debian
    /usr/share/doc/endlessh/changelog.Debian.gz
    /usr/share/doc/endlessh/copyright
    /usr/share/man
    /usr/share/man/man1
    /usr/share/man/man1/endlessh.1.gz

From this output we can see that the `endlessh` package provides an
init script, a `systemd` service unit file, a binary, a readme file, a
changelog, a license file, and a manpage.

## How do I keep track of manually installed files?

Sometimes you need to install something that is not available as a
package. Luckily, there's a tool called `checkinstall` that acts as a
glue between a command that install files and the APT package
manager. You typically invoke it like this:

    $ cd some-package
    $ ./configure
    $ make
    $ sudo checkinstall make install

Here the `checkinstall` command wraps the `make install` command one
would usually run. The file system is scanned for new files created by
the installation command. The created files are then added to a new
APT package. When you run `checkinstall` you get to fill in the
details of the package (name, version, maintainer, etc).

The source directory can be deleted at this point. Once the files are
installed and owned properly by a package it is now easy to uninstall
previously installed files - simply uninstall the package!
