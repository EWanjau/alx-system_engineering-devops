# using puppet to install a package and specify the version
package { 'flask':
    ensure   =>  '2.1.0',
    provider => 'pip3',
}
