# using puppet to create a new file, set its permisions, user and specify the path
file { 'school':
  content => 'I love Puppet',
  path => '/tmp/school',
  owner => 'www-data',
  group => 'www-data',
  mode => '0744',
}
