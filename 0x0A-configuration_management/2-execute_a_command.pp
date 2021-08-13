# Task 2 - sing Puppet, create a manifest that kills a process named killmenow.

exec { 'killmenow':
	command => 'pkill -f killmenow',
	provider => 'shell',
	path    => '/usr/bin'
}
