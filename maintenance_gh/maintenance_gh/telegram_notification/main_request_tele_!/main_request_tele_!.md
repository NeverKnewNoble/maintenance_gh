<h3>Maintenance Request</h3>
<h2>Request {{ doc.name }} Has Been Submitted To The Maintenance Team</h2>

<p>Dear Maintenance Manager,<br>
<p>I am writting to notify you of and to request for the necessary repairs for the following property:<br>

<h4>Scheduling Details:<h4>

{% for sector in doc.sector %}
Sector: {{ sector.sector }}
{% endfor %}

{% for sector in doc.sector %}
Description: {{ sector.issue_description }}
{% endfor %}