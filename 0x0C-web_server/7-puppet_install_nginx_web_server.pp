# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Configure Nginx site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80;
      server_name _;

      location /redirect_me {
        return 301 http://\$host/new_location;
      }

      location / {
        return 200 'Hello World!';
      }
    }
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
