<h2>Maintenance Request</h2>
<h3>Request {{ doc.name }} Has Been Submitted</h2>

<p>Dear Maintenance Manager,<br>
<p>I am writting to notify and to request for the necessary repairs for the following property:<br>

<h4>Request Details:<h4>
<ul>
<li>
{% for sector in doc.sector_list %}
Sector: {{ sector.sector_1 }}
{% endfor %}
</li>
<li>
{% for sector in doc.sector_list %}
Description: {{ sector.issue_description }}
{% endfor %}
</li>
</ul>
