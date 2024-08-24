# Adjust file limits for the user 'holberton' to prevent access issues.

# Modify the hard file limit for holberton.
exec { 'adjust_hard_limit_holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => ['/bin/', '/usr/bin/']
}

# Modify the soft file limit for holberton.
exec { 'adjust_soft_limit_holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => ['/bin/', '/usr/bin/']
}
