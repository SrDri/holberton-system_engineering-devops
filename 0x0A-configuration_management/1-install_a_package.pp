# Task 1 - Using Puppet, create a manifest that kills a process named killmenow.
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
