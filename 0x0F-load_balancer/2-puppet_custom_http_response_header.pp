# Create a custom HTTP header response
exec {'Set_custom_header':
    command  => 'sudo apt-get update;
    sudo apt-get -y install nginx;
    sed -i "20 i add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default;
    sudo service nginx restart',
    provider => 'shell',
}