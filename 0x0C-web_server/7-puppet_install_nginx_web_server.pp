# install and configure Nginx server using Puppet
# 301 redirect when querying /redirect_me

#install nginx
package { 'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt'
}

#nginx running
service { 'nginx':
  ensure => running,
  enable => true
}

#configuration
exec {'redirect':
  provider => shell,
  command  => 'sudo sed -i "/server_name _;/ a\\\trewrite ^/redirect_me https://juancarabalidev.com permanent;" /etc/nginx/sites-available/default',
}

#index file
exec { 'index':
  provider => shell,
  command  => 'echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html'
}
