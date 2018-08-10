<!DOCTYPE html>
<html>
<head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type">
    <title>{{title or 'No title'}}</title>

    <link rel="stylesheet" type="text/css" href="{{ get_url('static', path='css/main.css') }}" charset="utf-8"/>
    <script type="text/javascript" src="{{ get_url('static', path='js/jquery.min.js') }}" charset="utf-8"></script>
    <script type="text/javascript" src="{{ get_url('static', path='js/jquery.cookie.js') }}" charset="utf-8"></script>
    <script type="text/javascript" src="{{ get_url('static', path='js/kendo.all.min.js') }}" charset="utf-8"></script>
</head>
<body>

<div class="header">
  <h1>My Website</h1>
  <p>Resize the browser window to see the effect.</p>
</div>

<div class="topnav">
  <a href="/">Home</a>
  <a href="/config">Configuration</a>
  <a href="/schedule_tasks">Schedule Tasks</a>
  <a href="/modbus_network">Modbus network</a>
  <a href="/read_profiles">Read Profiles</a>
  <a href="/define_drivers">Device drivers</a>
  <a href="/logout" style="float:right">Logout</a>
</div>

<div class="row">
    {{!base}}
</div>

<div class="footer">
  <h2>Footer</h2>
</div>

</body>
</html>
