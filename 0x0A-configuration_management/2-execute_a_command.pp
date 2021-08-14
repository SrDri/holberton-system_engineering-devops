# Task 2 - create a manifest that kills a process named killmenow

exec {'kill process killmenow':
	command  => 'pkill killmenow',
	path => '/usr/bin'
}
