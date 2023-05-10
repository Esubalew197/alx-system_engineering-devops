# puppet manifest ensuring file /var/www/html/index.html exists
exec { 'correct typo':
  command  => '/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}

