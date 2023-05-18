# comments out ulimit line in /etc/security/limits.conf

exec { 'fix holberton ulimit':
  command => '/bin/sed -i "s/holberton/# holberton/g" /etc/security/limits.conf;'
}
