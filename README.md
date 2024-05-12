<!-- README.md

Copyright (c) Matt McCarthy 2024
See LICENSE for details.
-->

# ColorCycle

**Dynamic color-changing wallpaper application**

## Synopsis

**ColorCycle** is a terminal process that sets your desktop wallpaper to a solid color that changes hue based on the minute of the hour&mdash;red for the top of the hour, then smooth transitions to yellow, green, cyan, indigo, violet and back to red in ten-minute increments.

Consider this a project in artistic expression, or if you're feeling ambitious, a productivity tool. Knowing what time of the hour based on what color your wallpaper changes to is faster than looking at the clock, which tends to be pinned to the corner of our screens.

For the lazy, we don't even need to change our focus to approximate how much time we have left in the hour. This saves precious seconds, and keeps our primary focus on work while passively considering the time rather than wasting aggregate minutes actively checking the clock.

## Basic Installation

A **macOS (Sonoma, Silicon/ARM)** binary is provided in the project's `dist` directory. Windows and Linux users face the ultimatum of waiting for support or compiling on their own, modded software&mdash;which will involve finding a way to update desktop wallpaper programmatically. To make this easier, most of the process is outlined below.

## Compiling from Source

So far, this application is only *officially* supported on **macOS**. It is assumed that Linux users will understand the project's structure and be able to set a virtual environment and execute as they see fit. Windows users may need to use WSL.

For the purposes of this tutorial, it is assumed you are using `zsh`, the default **Terminal.app** shell. You may use any shell you like, but to keep it super simple, commands provided will be for `zsh`.

The first step is to clone this repository. That should be easy enough.

### Dependency Overview

At this point, the project only depends on Python and a few of its officially supported modules (listed by chronological order of relevance):

- [Python](https://www.python.org/) (for interpretting the project code)
- [`pip`](https://pip.pypa.io/en/stable/) (for installing the below packages)
- [`virtualenv`](https://virtualenv.pypa.io/en/stable/) (for containing dependencies within a dedicated evnviornment)
- [Pillow](https://pillow.readthedocs.io/) (for generating wallpapers)

It is recommended that you read the installation instructions in the documentation links above before continuing.

### Install Python

Secondly, ensure that Python 3.10 or greater is installed. You may verify the version with the following command:

```zsh
python --version
```

If the version is out of date, you may have previously installed an earlier image. Otherwise, if you get an error message complaining that the command doesn't exist, you might need to add it to your `$PATH`.

### Install Package Installer for Python

Next, install [`pip`](https://pip.pypa.io/en/stable/). There are a few different methods of doing this, but my preferred method is by running the following:

```zsh
python -m pip install -U pip
```

This will allow you to run `pip` via its own command, at its latest version, rather than relying on `python -m`.

### Install and Activate Virtual Environment

Now that `pip` is installed, we need a place to store dependencies.

```zsh
pip install -U virtualenv
```

Once installed, create a virtual environment directory:

```zsh
virtualenv .venv
```

Naming it `.venv` is recommended for a few reasons:

1. The leading period makes it hidden on POSIX systems
2. The 'v' in `.venv` sets it apart from environment *variables*
3. This project has references to it with that name. If you change it here, be prepared to change in `Makefile` in the project root.


### Use C-Make to Install Remaining Dependencies

Now, the `Makefile` at the project root will automate the rest for you.

```zsh
make
```

This will perform the following steps in order:

1. Create a virtual environment (like in the last step) if one does not exist
2. Install remaining dependencies via `pip` (namely, Pillow)
3. Compile the project

## Running the Compiled Binary

When complete, you are ready to run the executable.

```zsh
make run
```

Optionally, you may want to add the `dist` directory to your `$PATH` variable. That way, you can simply run:

```zsh
colorcycle
```

Exit with `ctrl` + `c`.

