# Odoo Basics

## Architecture Overview
* Odoo follows a multitier architecture, meaning that the presentation, the business logic and the data storage are separated.
* The **presentation** tier is a combination of **HTML5, JavaScript and CSS**
* The **logic** tier is exclusively written in **Python**,
* The **data** tier only supports **PostgreSQL** as an **RDBMS**


## Odoo modules
* Both server and client extensions are packaged as modules which are optionally loaded in a database.
* A module is a collection of functions and data that target a single purpose.
* Odoo modules can either add brand new business logic to an Odoo system or alter and extend existing business logic.
* Everything in Odoo starts and ends with modules.
* Modules may also be referred to as **addons** and the directories where the Odoo server finds them form the **addons_path**

### Composition of a module
* **Business objects**
  * A business object (e.g. an invoice) is declared as a Python class or Models
* **Object views**
  * Define UI display
* **Data files**
  * XML or CSV files declaring the model data
* **Web controllers**
  * Handle requests from web browsers
* **Static web data**
  * Images, CSS or JavaScript files used by the web interface or website

### Module structure
* An Odoo module is declared by its manifest.
  ```sh
    module
    ├── models
    │   ├── *.py
    │   └── __init__.py
    ├── data
    │   └── *.xml
    ├── __init__.py
    └── __manifest__.py
  ```
### Odoo Editions
* Odoo is available in two versions
  * Odoo Enterprise (licensed & shared sources)
  * Odoo Community (open-source)
* In addition to services such as support or upgrades, the Enterprise version provides extra functionalities to Odoo.
* From a technical point-of-view, these functionalities are simply new modules installed on top of the modules provided by the Community version.