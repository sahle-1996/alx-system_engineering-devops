# Puppet manifest to configure nginx for specific requirements

# Install nginx package
package { 'nginx':
  ensure => 'present',
}

# Create index.html with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  mode    => '0644',
}

# Configure nginx for redirection and Hello World! response
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    location /redirect_me {
        return 301 https://blog.ehoneahobed.com/;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}
",
  notify  => Exec['nginx-reload'],
}

# Ensure nginx service is running and restart on configuration change
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  hasrestart => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Exec resource to reload nginx configuration
exec { 'nginx-reload':
  command     => 'sudo service nginx reload',
  refreshonly => true,
}
