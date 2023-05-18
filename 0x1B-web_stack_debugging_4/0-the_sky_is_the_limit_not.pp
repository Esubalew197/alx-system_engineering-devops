# comments out ulimit line in /etc/default/nginx

exec { 'fix nginx ulimit':
  command => '/bin/sed -i "s/ULIMIT/# ULIMIT/" /etc/default/nginx; /usr/sbin/service nginx restart'
}
