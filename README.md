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

### Useful Links
https://docs.bitnami.com/general/apps/edx/
https://openedx.atlassian.net/wiki/spaces/OpenOPS/pages/19662636/How-to+articles
https://blog.lawrencemcdaniel.com/?s=open+edx
https://docs.bitnami.com/general/apps/edx/configuration/install-theme/
