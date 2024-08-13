#!/usr/bin/env puppet
"""
Puppet configuration to fix file permissions on WordPress settings.
"""

# Ensure the correct permissions on wp-settings.php
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}
