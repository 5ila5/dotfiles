# dotfiles
my Dotfiles


RESTORE
```bash
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
```
```bash
git clone --bare <git-repo-url> $HOME/.cfg
```
```bash
config checkout
```
if an Error Message pos up use this to back up conflicting files

```bash
mkdir -p .config-backup && config checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | xargs -I{} mv {} .config-backup/{}
```
and rerun ```config checkout```
