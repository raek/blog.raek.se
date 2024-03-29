My go-to method for deploying command line tools I've written is to build Python
packages and installing them. This works well for putting the tools on the PATH,
but one thing I've been missing is to also include "OS integration files" (such
as `man` pages, `.desktop` app launchers, and systemd unit files). Recently I
learned a way to do it.

## Files in a Python Package

A python package can be seen as containing three different types of files:

* _Python code files:_ pure `.py` files, or compiled extensions
* _Resource files:_ data files used internally by the package
* _OS integration files:_ data files used to hook the package into the OS
  environment (eg. the previously mentioned `man`, `.desktop`, and unit files)

Documentation and tool support for resource files seems to be widely available.
This article is about the third type (which I call "OS integration files" as I
don't know any better or standardized term). These kind of files are mostly
portable within the sphere of Unix-like systems. There they get installed in a
location like `/usr/local` for system installs and `~/.local` for user installs.
This is useful since tools like the man page reader, the desktop environment,
and systemd look for files there.

I struggled to find documentation and examples for how to include such files in
Python packages, but eventually I found how to do it in thee Python build
systems: _Flit_, _Setuptools_ and _Hatch_. A limitation of the approach is that
it only works with "user" and "system" installs with `pip` and not with virtual
environments. This article is a summary of what I learned.

## An example application: `striking-clock`

A small toy project will serve as the example: `striking-clock`. The full source
for the package is available [in a GitHub repo][project] with examples for all
of the build systems. It has [a 25-line script (`striking-clock`)][script] which
prints "BONG!" a number of times (the current hour) and then exits.

[project]: <https://github.com/raek/striking-clock/>
[script]: <https://raw.githubusercontent.com/raek/striking-clock/master/setuptools_pyproject.toml/striking_clock.py>

The program is supposed to be executed every hour. That is taken care of by the
two accompanying systemd user unit files. There is one [service][service], which
just runs the script, and one [timer][timer], which activates the service once
every new hour.

The goal is to install these files in the `share/systemd/user` directory below
the "local" directory (`/usr/local` or `~/.local`).

[service]: <https://raw.githubusercontent.com/raek/striking-clock/master/setuptools_pyproject.toml/striking-clock.service>
[timer]: <https://raw.githubusercontent.com/raek/striking-clock/master/setuptools_pyproject.toml/striking-clock.timer>

The `striking-clock` source code has the following files:

* `LICENSE`
* `pyproject.toml`
* `README.md`
* `striking_clock.py`
* `striking-clock.service`
* `striking-clock.timer`

The `pyproject.toml` file looks nearly identical for all three build systems
thanks to [PEP 621][pep621]. Here are the lines common to all the build systems:

[pep621]: <https://peps.python.org/pep-0621/>

    [project]
    name = "striking_clock"
    version = "1.0.0"
    description = "A service that goes BONG! BONG! BONG! every hour."
    readme = "README.md"
    authors = [{name = "Rasmus Bondesson", email = "raek@raek.se"}]
    license = {file = "LICENSE"}
    classifiers = ["License :: OSI Approved :: MIT License"]
    requires-python = ">=3.5, <4"
    dependencies = [
        "appdirs",
    ]

    [project.urls]
    Home = "https://github.com/raek/striking-clock/"

    [project.scripts]
    striking-clock = "striking_clock:main"

Now for the build system dependent parts.

## Declaring OS Integration Files

### Example Using Flit

In Flit, you include OS integration files by specifing a single "external data"
directory. The destination path in the "local" directory simplay mirrors the
path inside the "external data" directory. Here is how the project file tree
look accomodating this if we name the "external data" directory `data`:

    striking-clock
    ├── data
    │   └── share
    │       └── systemd
    │           └── user
    │               ├── striking-clock.service
    │               └── striking-clock.timer
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    └── striking_clock.py

The `pyproject.toml` then gets some additions, notably a tool-specific
[`external-data`][flit-doc] section:

[flit-doc]: <https://flit.pypa.io/en/stable/pyproject_toml.html#external-data-section>

    [build-system]
    requires = ["flit_core >=3.7,<4"]
    build-backend = "flit_core.buildapi"

    [tool.flit.external-data]
    directory = "data"

Fairly easy! The deeply nested directories may be a bit annoying, but at least
they follow a simple rule. Also note the `requires` version: support for
`external-data` was added in `flit-core` 3.7.0 (released February 23, 2022).

### Example Using Setuptools

Setuptools' approach is to list all included OS integration files (called
"non-package data files" or simply "data_files") in a tool-specific
[`data-files`][setuptools-doc] sections:

[setuptools-doc]: <https://setuptools.pypa.io/en/latest/userguide/datafiles.html#non-package-data-files>

    [build-system]
    requires = ["setuptools"]
    build-backend = "setuptools.build_meta"

    [tool.setuptools.data-files]
    "share/systemd/user" = [
        "striking-clock.service",
        "striking-clock.timer",
    ]

In contrast to Flit, Setuptools allows the source files to be placed anywhere in
the source tree. In this example they are in the root for simplicity. The
destination path is defined in the `pyproject.toml` file. The data files section
contains dictionaries where the keys are destination directories and the values
are lists of files to be installed in destination directory.

If you use a `setup.cfg` file, then the added section instead looks like this:

    [options.data_files]
    share/systemd/user =
        striking-clock.service
        striking-clock.timer

And if you sue a `setup.py` file, then the argument to `setup()` looks like
this:

    setuptools.setup(
        ...
        data_files=[
            ("share/systemd/user", [
                "striking-clock.service",
                "striking-clock.timer",
            ]),
        ]
    )

I should probably note that `data-files` has been deprecated in Setuptools.
Examples in the documentation were removed in October 31, 2021. The
documentation for the [`data-files`][data-files-keyword] keyword only says:

[data-files-keyword]: <https://setuptools.pypa.io/en/latest/references/keywords.html#keyword-data-files>

> `data_files` is deprecated. It does not work with wheels, so it should be avoided.

This is a bit odd, since at least the example in this article does in fact work
with weels. [The documentation for OS integration
files][data-files-recommendation] – "Non-Package Data Files" in Setuptools
parlance – urges the reader to consider using reasource files instead (which
doesn't work if OS integration is what's really needed.)

[data-files-recommendation]: <https://setuptools.pypa.io/en/latest/userguide/datafiles.html#non-package-data-files>

In April 24, 2022 [a discussion][data-files-fr] for adding a replacement for
`data-files` was started, citing the features of Flit and Hatch as inspiration.
I find it a bit ironic that the Flit `shared-data` feature [was
inspired][flit-shared-data-fr] by `data-files` from Setuptools.

[data-files-fr]: <https://github.com/pypa/setuptools/issues/3191>
[flit-shared-data-fr]: <https://github.com/pypa/flit/issues/358>

### Example Using Hatch

In Hatch, including OS integration files (called "shared data" here) is
something done by wheel builder plugin. To configure it, we add a tool-specific
[`build.targets.wheel.shared-data`][hatch-doc] section to `pyproject.toml`:

[hatch-doc]: <https://hatch.pypa.io/latest/plugins/builder/wheel/#options>

    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [tool.hatch.build.targets.wheel.shared-data]
    "striking-clock.service" = "share/systemd/user/striking-clock.service"
    "striking-clock.timer" = "share/systemd/user/striking-clock.timer"

Like in Setuptools, the source files can be stored anywhere in the source tree.
In this example too, I put them in the root for simplicity. The section contains
a flat listing of pairs of source files and destination paths. Note that the
roles of the left and right hand sides are reversed compared to Setuptools.

Hatch has supported "shared data" since its public release in April 28, 2022.

## Build and Test

This section is mostly a demo of the settings descibed above to prove that they
work. Each package can be built, and installed in the same way:

    pip install build
    git clone https://github.com/raek/striking-clock.git
    cd striking-clock/<one-of-the-example-directories>/
    python -m build
    pip install --user dist/striking_clock-1.0.0-py3-none-any.whl

Replace "python" and "pip" with the names suitable for your environment, for
example `python3` and `python3 -m pip`. Note that the package should either be
installed in user-mode (`pip install --user`) or in system-mode (`sudo pip
install`) and not in a virtual environment. The OS will not look for the OS
integration files in the virtual environment location, so installing them there
won't have any effect.

To try one of the other examples, uninstall the old one first and then repeat
the steps above fot the new one. You can use `pip show --files striking-clock`
to display which files got installed and where they ended up.

You should now be able to interact with the systemd units. They are user units,
so the `--user` flag needs to be passed to all `systemctl` commands. Let's try
the service:

    # Reload unit files if that have changed
    systemctl --user daemon-reload

    # Check that systemd recognized the unit
    systemctl --user status striking-clock.service

    # Trigger the service once manually for testing
    systemctl --user start striking-clock.service

    # Display output from the service
    journalctl -e --user-unit striking-clock.service

We can also test the timer:

    # Manually start the timer (only for this boot)
    systemctl --user start striking-clock.timer

    # Check the status (time to next trigger, etc)
    systemctl --user status striking-clock.timer

    # Stop the timer again before we forget about it
    systemctl --user stop striking-clock.timer

As usual with timer units, invoke the `enable`/`disable` commands to control
automatic start on boot. (The service unit should not be enabled/disabled, as it
is activated by the timer.)

## Closing Remarks

There it is! I hope this is useful to someone else. Please get in touch if it
was, or if you have any questions, or if you know any missing pieces of the
puzzle I should know (for example regarding the Setuptools deprecation thing).
On HTTP you can use the comment form below and on Gemini see the contact
information on my main capsule page.
