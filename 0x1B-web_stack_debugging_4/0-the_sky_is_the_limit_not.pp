# Modifies Nginx settings to handle more traffic effectively.

# Adjust the file limit for Nginx service
exec { 'nginx_ulimit_update':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/bin:/usr/bin'
} ->

# Reload the Nginx service to apply changes
exec { 'reload_nginx_service':
  command => 'service nginx reload',
  path    => '/sbin:/usr/sbin'
}
