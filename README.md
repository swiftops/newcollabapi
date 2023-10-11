# newcollabapi
Collab service for RedTeam

# Local Devlopement requirement
1. Ubuntu Linux system 
2. VS Code
3. Docker
4. Postman
5. Postgresql Admin Tool for query browser
6. GitHub Login for Accessing Repository

# Postgresql Docker compose file:
=================================
version: '3.1'

services:

  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: HackM3
      PGDATA: /var/lib/postgresql/data/pgdata

    volumes:
      - ./db:/var/lib/postgresql/data

    ports:
      - 1486:1486
      - 5432:5432

# Docker file END

# Apache Webserver Docker compose file:
=======================================
version: '3'
services:
  swiftent_apache:
    image: digite/swiftent-apache:latest
    container_name: swiftent_apache
    hostname: swiftent_apache    
    environment:
## Set Timezone to container ##
## Please refer link for Timezone code need to pass as per you location. For example India= Asia/Kolkata
### LINK: http://manpages.ubuntu.com/manpages/bionic/man3/DateTime::TimeZone::Catalog.3pm.html
      - TZ=Asia/Kolkata

## MOUNT THE PATH FOR PERSISTANT STORAGE, REPLACE THE PATH WITH YOUR MOUNT PATH.
## EXAMPLE:
## <YOUR PATH>:/opt/configuration
## <YOUR PATH>:/var/log/apache2
    volumes:
      - ./conf:/opt/configuration
      - ./log:/var/log/apache2
      - /data/Pythonwork/redteam/newcollabapi/frontend:/var/www/html
    ports:
      - 80:80
      - 443:443

# Docker file END 

# Apache HTTPD configuration file Name: app-http.conf
# Note: Abouve config File name should be added into 'apache2.conf' in your mounted path.
===========================================================================

        <VirtualHost _default_:80>
#                ServerAdmin itis@digite.com
#                ServerName swift.digite.com
                LogFormat "%h %t \"%r\" %>s %p %b \"%{Referer}i\" \"%{User-Agent}i\" %{ms}T" nimblelog
                ErrorLog ${APACHE_LOG_DIR}/app-error.log
                #CustomLog ${APACHE_LOG_DIR}/app-access.log nimblelog
                CustomLog "|/usr/bin/rotatelogs -l ${APACHE_LOG_DIR}/app-access-%d-%m-%Y-%H-%M-%S.log 86400" nimblelog

                <Proxy *>
                  Order deny,allow
                  Allow from all
               </Proxy>                                

 ### Static content configuration ####
DocumentRoot /var/www/html

<Directory /var/www/html>
 Options -Indexes
 AllowOverride All
  Order allow,deny
 Allow from all
</Directory>

ErrorDocument 503 /UnplannedDowntime.html


## Enable gzip compression
SetOutputFilter DEFLATE
SetInputFilter DEFLATE
SetEnvIfNoCase Request_URI \.(?:gif|jpe?g|png)$ no-gzip dont-vary
SetEnvIfNoCase Request_URI \.(?:pdf|exe|zip)$ no-gzip dont-vary
     

        </VirtualHost> 

# Apache Configuration END
