# fix Apache 500 error
exec { 'fix typo':
  command => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/ /var/www/html/wp-settings.php',
  path    => '/bin',
}
