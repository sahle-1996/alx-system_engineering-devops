# Adjust Nginx configuration to increase request handling capacity.

exec { 'update_nginx_file_limit_and_restart':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && service nginx restart',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin']
}
