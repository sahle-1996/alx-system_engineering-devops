# Ensure puppet-lint version 2.1.0 is installed

exec { 'install-puppet-lint':
  command => 'apt-get install -y puppet-lint=2.1.0',
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
}
