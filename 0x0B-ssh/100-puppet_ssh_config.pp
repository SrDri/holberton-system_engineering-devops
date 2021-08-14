# ssh config
exec { 'ssh-config':
path    => '/bin'
command => 'echo "PasswordAuthentication no" >> /ect/ssh/ssh_config; echo "IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config'
}
