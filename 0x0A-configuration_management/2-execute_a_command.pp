# Task 2 - sing Puppet, create a manifest that kills a process named killmenow.
exec { 'killmenow':
	command => 'pkill killmenow',
	provider => shell,
}
