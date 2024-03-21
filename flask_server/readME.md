Short explication of the flask_server package: <br>
<code>Dockerfile</code>, <code>requirements.txt</code> are for the flaskserver setup over docker. To run the docker server use <code>docker-compose.yml</code> in the odoo_llm_auto_responder package (do not move the file into another package without testing if it still works)<br>
<code>app.py</code> programs the functionality of the docker flaskserver <br>
<code>flaskServer.py</code>is a local flaskserver to test <br>
<code>__init__</code> and <code>llm_integration</code> have no functionality yet <br>
<code>test</code> is to test out the LLM. <br>
<code>serverRequests</code> is a python file to call up the server and communicate with it <br>

