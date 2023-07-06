node 'ubuntu' {
  class{'nginx':}
  nginx::vhost {'techysoft.tech':
    port => '80',
    docroot => '/var/www/html'
  }
}
