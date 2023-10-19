<h4>Maintenance Scheduling</h4>
<h3>Report {{ doc.name }} has been submitted to the maintenance team</h3>

<h2>Scheduling Details:</h2>

<ul>
<li>
{% for track in doc.track %}
Sector: {{ track.sector_name }}
{% endfor %}
</li>

<li>
{% for track in doc.track %}
Description: {{ track.description_scheduling }}
{% endfor %}
</li>

<li>
{% for track in doc.track %}
Instructions: {{ track.instructions_}}
{% endfor %}
</li>
</ul>