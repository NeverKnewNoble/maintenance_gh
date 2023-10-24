<h2>Maintenance Rescheduling</h2>
<h3>Report {{ doc.name }} has been rescheduled according to the details below.</h3>
<h4>Scheduling Details:</h4>

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