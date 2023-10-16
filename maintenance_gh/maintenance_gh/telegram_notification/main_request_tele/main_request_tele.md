<h3>Issue Report For Maintenance Team<h3>

<p>Request {{ doc.name }} has been submitted to the maintenance team<p>

{% for sector in doc.sector %}
Sector: {{ sector.sector }}
{% endfor %}

{% for sector in doc.sector %}
Description: {{ sector.issue_description }}
{% endfor %}