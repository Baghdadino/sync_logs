# sync_logs
* custom module for user's CRUD activities on models in Odoo 14

# Steps
* I created a conda environment with python=3.7 where I installed Odoo 14's requirement.
* I created a docker container to run a postgres instance using the following command:
  # docker run -p 5432:5432 -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -d --name odoo_v14 postgres:10.0
* I used Audit Trail module for odoo 14 and made some customizations here is the link:
  # https://apps.odoo.com/apps/modules/14.0/smile_audit/
* I cloned the Audit menuitem and named it "SyncLogs" with 2 submenus: Rules and Logs.
* Rule menuitem where you add the tarcking rule for the Model(Student, Parent)
* Logs menuitem with slight changes from the original where an "action" field is added.
  # docker db backup file
  https://drive.google.com/file/d/10wCadoovchkOd0f5O7GBFl9jwRrWyz3a/view?usp=sharing


