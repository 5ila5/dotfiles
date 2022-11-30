alias brightness0="brightness DP-0" 
brightness() {
	var=$2

	if (($(echo "$2>1" |bc -l) )); then	
	
		if (($(echo "$2<10" |bc -l) )); then	
				
			var=$(bc  <<< "scale=2;$var*10")
		fi
		var=$(bc  <<< "scale=2;$var/100")
	
	fi
	
	xrandr --output $1 --brightness $var
}
md() {
	mkdir -pv $1 && cd $1
}
alias brightness1='brightness DVI-D-0'
alias testqtile='export DISPLAY=:0 && Xephyr -br -ac -noreset -screen 800x600 :1 & export DISPLAY=:1&& qtile start -c ~/.config/qtile/WIP/config.py &'
alias cls='clear'
function palias(){
	echo "alias $1='$2'" >> ~/.bash_aliases && source ~/.bash_aliases;
}

function sw() {
	kanshi
	setxkbmap de &
	clipmanager &
	sxhkd &
	udiskie --tray &
	numlockx &
	nitrogen --restore &
	qtile start -b wayland

}
alias cp="cp -iv"
alias mv="mv -iv"
alias rm="rm -v"
alias mkdir="mkdir -pv"

alias vim = 'nvim'
alias lö=ls
alias 'l=ls -lhag'
alias 'c=clear'
alias 's=sudo'
alias sr='sudo $(history -p !!)'
alias 'srouch=source'
alias 'sourch=source'
alias 'pu=paru -Syu'
alias 'py=paru -Sy'
alias 'sp=paru'
alias p='paru'
alias 'vf=cd'
alias 'svim=sudo vim'
alias pbcopy='xsel --clipboard --input'
alias 'pbpaste="xsel --clipboard --output"'
alias 'cod=code'
alias 'onenote=p3-onenote'
alias 'smake=sudo make'
alias 'mbirght=brightness0'
alias 'mbright=brightness0'
alias 'mbright7=mbright .7'
alias fixbackground='nitrogen --restore'
alias 'sps=sp -S'
alias foldersize='du -ah --max-depth 1'
alias thissize='du -ah --max-depth 0'
alias sourcea='source ~/.bash_aliases'
alias valia='nvim ~/.bash_aliases && source ~/.bash_aliases'
alias testecho='echo test'
alias disksizes='df -h'
alias spyu='sp -Syu'
alias 'sx=startx'
alias cd..='cd ..'
alias updateAll='paru -Syu'
alias spr='paru -Rcns'
alias spsyu='paru -Syu'
alias writer='libreoffice --writer'
alias calc='libreoffice --calc'
alias yay='paru'
alias y='yay'
alias ys='yay -S'
alias yss='yay -Ss'
alias yr='yay -Rcns'
alias sudo='doas'
alias pingtest='ping heise.de'
alias findContent='grep -rnw '.' -e'
alias sv='s vim'
alias spss='sudo pacman -Ss'
alias checkqtile='qtile check -c ~/.config/qtile/configWIP.py'
alias qtilelogs='cat ~/.local/share/qtile/qtile.log'
alias spfind='sudo pacman -Ql '
alias search="grep -rnw . -e"
alias folderSize='du -sh'
alias sw='qtile start -b wayland'
alias sq='qtile start -b wayland'
alias testqtilewayland='qtile start -b wayland -c ~/.config/qtile/configWIP.py'
alias blendet='python ~/.config/HomeassistantAPI_ctl/rollo.py'
alias spq='sudo pacman -Q'
alias spqs='sudo pacman -Qs'
alias code='code --disable-gpu'
alias sshServer='ssh root@eis.lan.home'
alias pacmanLog='cat /var/log/pacman.log'
alias ls='exa'
alias v='vim'
#alias rg='grep'
alias find='fd'
alias config='/usr/bin/git --git-dir=/home/silas/.cfg/ --work-tree=/home/silas'
alias ..='cd ..'
alias ...='cd ../..'
alias padMapScrenn0='xsetwacom set 14 MapToOutput HEAD-0'
alias padMapScrenn1='xsetwacom set 14 MapToOutput HEAD-1'
alias padMapScrenn2='xsetwacom set 14 MapToOutput HEAD-2'
alias teams='teams-insiders --no-sandbox'
alias eis='ssh root@eis.lan.home'
alias testInternet='watch --interval .5 "ping -w 1 -c 1 heise.de | grep \"64 Bytes\" && ping -w 1 -c 1 192.168.168.254 | grep \"64 Bytes\" && ping -w 1 -c 1 192.168.169.254 | grep \"64 Bytes\" && ping eis.lan.home -c 1 -w 1 | grep \"64 Bytes\" "'
alias getIp='curl -s http://checkip.dyndns.org/ | sed "s/[a-zA-Z<>/ :]//g"'
alias startWG='doas systemctl start wg-quick@wg0 && sleep 1 && echo "your new IP addres is:" && getIp'
alias stopWG='doas systemctl stop wg-quick@wg0 && sleep 1 && echo "your new IP addres is:" && getIp'

alias run='compgen -c | dmenu -i | bash'
alias shutdownUpdate='paru -Syu && shutdown now'
alias sshTu='ssh -Y sk76lufi@clientssh5.rbg.informatik.tu-darmstadt.de'

alias sl='doas exa -lhag'
alias x='/home/silas/.local/script/util/unarchive.sh'
alias treesize='ncdu --exclude /proc'
alias g='git'
alias gc='git commit'
alias gcm='git commit -m'
alias gp='git push'
alias gpu='git pull'
alias gpum='git pull --no-rebase --no-ff'
alias gpufop='git pull public master --no-rebase --no-ff'
alias ga='git add'
alias gr='git remote'
alias n=nvim
