# script kills a process with a specific name
exec { 'pkill killmenow':
    command =>  'pkill -f killmenow',
    path    =>  '/usr/bin/',
}
