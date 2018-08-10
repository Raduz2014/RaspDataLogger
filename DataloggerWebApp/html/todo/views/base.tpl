<!DOCTYPE html>
<html>
<head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type">
    <title>{{title or 'No title'}}</title>

    <link rel="stylesheet" type="text/css" href="{{ get_url('static', path='css/main.css') }}" charset="utf-8"/>
    <script type="text/javascript" src="{{ get_url('static', path='js/jquery.min.js') }}" charset="utf-8"></script>
    <script type="text/javascript" src="{{ get_url('static', path='js/jquery.cookie.js') }}" charset="utf-8"></script>
</head>
<body>

<div class="header">
  <h1>My Website</h1>
  <p>Resize the browser window to see the effect.</p>
</div>
%setdefault('username', 'No user')

<div class="topnav">
  <a href="/" \\ 
  %if page_state == "home": 
  class="active" \\
  %end
  >Home</a>
  
  <a href="/config"
  <a href="/" \\ 
  %if page_state == "config": 
  class="active" \\
  %end  
  >Configuration</a>
  
  <a href="/schedule_tasks" \\
  %if page_state == "schedtasks": 
  class="active" \\
  %end  
  >Schedule Tasks</a>

  <a href="/modbus_network" \\
  %if page_state == "modbus": 
  class="active" \\
  %end  
  >Modbus configuration</a>

  <a href="/meter_profiles" \\
  %if page_state == "meterprofiles": 
  class="active" \\
  %end    
  >Read Profiles</a>

  <a href="/meter_drivers" \\
  %if page_state == "meterdrivers": 
  class="active" \\
  %end    
  >Meter drivers</a>

  <a href="/logout" style="float:right">Logout</a>
  <a href="/userinfo" style="float:right">{{username}}</a>
</div>

<div class="row">
  <div class="leftcolumn">\\
    %if page_state == "home": 
      <div class="card sidemenu">     
        <h3>System</h3>
        <a href="/sys_info" \\
          %if subpage == "sys_info": 
          class="active" \\
          %end 
        >Information</a>
        <a href="/wire" \\
            %if subpage == "wire": 
            class="active" \\
            %end         
        >Wire network</a>
        <a href="/wireless" \\
            %if subpage == "wireless": 
            class="active" \\
            %end 
        >Wireless network</a>
        <a href="/mobile" \\
            %if subpage == "mobile": 
              class="active" \\
            %end 
        >Mobile network</a>
      </div>\\
    %else:
      <div class="card sidemenu">
        <h3>Other</h3>
      </div>\\
    %end
  </div>
    {{!base}}
</div>

<div class="footer">
  <h2>Footer</h2>
</div>

</body>
</html>
