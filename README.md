# open-edx
Documentation and other helper tools for changing/ editing open-edx configs + themes

If you have knowledge of Django it should be very easy for you to understand and edit this.

# Getting Started
Before you  start make sure you have your vm instance up and running

### Login
Username: bitnami
Password: bitnami

To view your site:
  - GCP - Google Cloud Platform
    - You can view your VM instance page and go to the external ip address
  - VM
    - When you start your vm instance or connect to it via ssh the machine will show you at what ip address you can view the website.
  
To setup open edx with your configs you need to edit both*(if you are going to be using both cms and lms otherwise just edit which ever one you are going to be using) lms and cms. 
  - Change Directory
    - LMS
      - `cd /opt/bitnami/edx/conf/lms.env.json` -> For setting up environment variables for LMS
    - CMS
      - `cd /opt/bitnami/edx/conf/cms.env.json` -> For setting up environment variables for CMS
  
  *.auth.json files contains db and other connection credentials and might need to change/edit them
  httpd-*.conf files contains rules for the server to allow which files/folders should be accessible
    
# Compiling Your Assets and Restarting your server
  - If you enabled the custom theme for LMS, update LMS assets:
    - `sudo /opt/bitnami/apps/edx/bin/edxapp-update-assets-lms`
  
  - If you enabled the custom theme for CMS, update CMS assets:
    - `sudo /opt/bitnami/apps/edx/bin/edxapp-update-assets-cms`
    
  - Restart the Apache server:
    `sudo /opt/bitnami/ctlscript.sh restart apache`

- Everytime you make any changes to your lms or cms files make sure to recompile them 
  - if you only make changes to lms only update lms

- Always restart your server after re-compiling your assets

# Connecting to your SMTP server
https://docs.bitnami.com/installer/apps/edx/configuration/configure-smtp/
You will need to edit *.env.json & *.auth.json. Both lms and cms environment and cms files are virtually the same. So any changes you make lms you will need to make to cms unless you are not using the cms portion of open-edx.
- In your lms.auth.json & cms.auth.json files you will need to look for:
  - `EMAIL_HOST_PASSWORD` set it equal to your smtp client password
  - `EMAIL_HOST_USER` set it equal to your smtp client email/user  
- In your lms.auth.json & cms.auth.json files you will need to look for:
  - `EMAIL_HOST` set it equal to your smtp server url (example: smtp.google.com)
  - `EMAIL_PORT` set it equal to your smtp server port it should be 587 or 465 unless otherwise
  - `DEFAULT_FROM_EMAIL` set it equal to your outgoing email (example: no-reply@example.com)

- For changes to take place your would need to restart both apache and edx:
  - Restarting Apache -> `sudo /opt/bitnami/ctlscript.sh restart apache`
  - Restarting Edx -> `sudo /opt/bitnami/ctlscript.sh restart edx`
  

## Delete a course
  - cd apps/edx/edx-platform
  - sudo -u bitnami ../bin/python.edxapp ./manage.py lms dump_course_ids --settings aws
  - sudo -u bitnami ../bin/python.edxapp ./manage.py cms --settings=aws delete_course COURSE_ID
  
  
### Links
https://docs.bitnami.com/general/apps/edx/
https://openedx.atlassian.net/wiki/spaces/OpenOPS/pages/19662636/How-to+articles
https://blog.lawrencemcdaniel.com/?s=open+edx
https://docs.bitnami.com/installer/apps/edx/configuration/configure-smtp/
https://docs.bitnami.com/general/apps/edx/configuration/install-theme/
https://openedx.atlassian.net/wiki/spaces/OXA/pages/158194136/How+to+delete+a+course
