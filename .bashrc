#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

SCRIPTS="${HOME}/bin"

PS1='[\u@\h \W]\$ '

# aliases
alias ls='ls --color=auto'
alias config='/usr/bin/git --git-dir=/home/alser/dotfiles/ --work-tree=/home/alser'


# Get npm packages from .npm-packages
NPM_PACKAGES="${HOME}/.npm-packages"
export PATH="$PATH:$NPM_PACKAGES/bin:$SCRIPTS"
# Preserve MANPATH if you already defined it somewhere in your config.
# Otherwise, fall back to `manpath` so we can inherit from `/etc/manpath`.
export MANPATH="${MANPATH-$(manpath)}:$NPM_PACKAGES/share/man"
