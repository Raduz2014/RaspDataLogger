% rebase('base.tpl', title='Lan configuration')
<div class="rightcolumn">
  <div class="card">
    <h2>Lan interfaces</h2>
    <br/>
    %if defined('subpage'):
       <div class="lan-card">\\
          %for lan in lans:
            <div>LAN Interface name: <b>{{lan[0]}}</b></div>
            % for adrcomp in lan[1]['mac']:
                <div>MAC Address:<span>{{adrcomp['addr']}}</span></div>
            % end
            % for adrcomp in lan[1]['ip']:
              <div>IP Address:<span>{{adrcomp['addr']}}</span></div>
              <div>Netmask:<span>{{adrcomp['netmask']}}</span></div>
              <div>Broadcast:<span>{{adrcomp['broadcast']}}</span></div>\\
            % end
          %end
      </div>    
    %end
  </div>
</div>