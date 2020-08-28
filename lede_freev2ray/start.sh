pip3 install requests bs4 -i https://mirrors.aliyun.com/pypi/simple/
#echo `dirname $0`
file_path="$PWD"
chmod 755 $file_path/*
#建立软连接 建立网页
ln -s $file_path /www/v2ray
#添加 内容进入crontab文件 并重启crontab服务
cat >> /var/spool/cron/crontabs/root <<EOF
0 */12 * * 1-6 /www/v2ray/playUsual.sh >>/tmp/v2ray.log  2>&1
0 12 * * 0  /www/v2ray/playUsual.sh >>/tmp/v2ray.log  2>&1
0 0 * * 0  /www/v2ray/playSunday.sh >>/tmp/v2ray.log  2>&1
EOF
systemctl restart crond