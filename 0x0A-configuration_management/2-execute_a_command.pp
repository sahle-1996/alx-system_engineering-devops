# Terminate the 'killmenow' process

exec { 'terminate_killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/usr/bin', '/bin'],
}
