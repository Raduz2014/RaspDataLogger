% rebase('base.tpl', title='System information')
<div class="rightcolumn">
  <div class="card">
    <h2>System information</h2>
    <br/>
    %if defined('subpage'):
       <div class="sysinfo-card">
          <table>
            <tr>
              <td class="tblRecordLabel">Device name:</td>
              <td class="tblRecordValue">{{device_name}}</td>

              <td class="tblRecordLabel">Memory usage:</td>
              <td class="tblRecordValue">{{mem_usage}}</td>
            </tr>
            <tr>
              <td class="tblRecordLabel">Serial number:</td>
              <td class="tblRecordValue">{{sn}}</td>

              <td class="tblRecordLabel">Internet connection:</td>
              <td class="tblRecordValue">{{internet_conn}}</td>
            </tr>
            <tr>
              <td class="tblRecordLabel">Uptime:</td>
              <td class="tblRecordValue">{{uptime}}</td>

              <td class="tblRecordLabel">Remote access:</td>
              <td class="tblRecordValue">{{remote_access}}</td>
            </tr>
            <tr>
              <td class="tblRecordLabel">Disk usage:</td>
              <td class="tblRecordValue">{{disk_usage}}</td>

              <td class="tblRecordLabel">Current date:</td>
              <td class="tblRecordValue">{{current_date}}</td>
            </tr>
          </table>
      </div>    
    %end
  </div>
</div>