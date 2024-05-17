# odoo_llm_auto_responder

LLM auto responder is a module for the enterprise-resource-planning (ERP) software [odoo](https://www.odoo.com).

This module allows you to **generate LLM supported automatic answers** for odoo helpdesk tickets. 
Therefore,it uses and is depending on the [Helpdesk Management](https://github.com/OCA/helpdesk/tree/16.0) module. 

![odoo_llm_auto_responder](https://github.com/Abilium-GmbH/odoo_llm_auto_responder/assets/160774626/eaf18624-fc7a-4606-8807-c723bb2f4b91)


**What sets this addon apart from other widespread chatbots is that the LLM runs locally on your system and
uses your previous answers as new context for the answer generation.**

It was developed by 6 Computer Science students at the university of Bern in cooperation with [Abilium](https://www.abilium.com/).

## Getting started

We developed the module for the community edition (version 16.0) of odoo.
It should work just fine with the Enterprise Edition but wasn't tested by us.

### 1. Docker installation
- Install Docker on your system


### 2. Repository cloning
- Clone this repository


### 3. Testbed setup
- Navigate to the "odoo_llm_auto_responder/testbed directory"
- Run the script named "prepare-and-run-testbed.sh"


### 4. Initial configuration
- On the first execution, ensure that the line "docker-compose -f docker-compose.yml build" is not commented
out and is executed
- After the initial setup, comment out this line
- access http://localhost:8069 and log in using admin:admin
- Now the Odoo application is started;
1. Browse to the "Apps" module
2. Search for "Odoo LLM Auto Responder" and click on "install"
3. The module "Helpdesk Management" will be automatically installed as well
4. **Note**: Probably the filter “Apps” has to be removed in the search window first before the module can be found.
Or it can be searched directly for the module.


### 5. Adding first context to LLM (Depends on chosen LLM)
The flask server can be accessed over the external port 5001 or the internal port 5000 (if you work inside of docker).
To store context into the context database you need to access the URL http://localhost:5001/store
and pass a json-file that is structured as following: {“context”: "insert your context here"}.
This task can be accomplished via the terminal on the own device or through code.
Here’s an example command to store context through the terminal:

curl -X POST -H "Content-Type: application/json" -d "{"context":"Insert context."}" \http://localhost:5000/store




## Documentation
For further instructions on how to install and use this module please refer out to [user manual](./Manual.pdf).
