# using puppet to create a new file, set its permisions, user and specify the path
file { 'school':
  path => '/tmp/school',
  mode => '0744',
  owner => 'www-data',
  group => 'www-data',
  content => 'I love Puppet',
}
