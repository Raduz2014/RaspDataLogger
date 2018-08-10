% rebase('base.tpl', title='Blank page')
<div class="rightcolumn">
  <div class="card">
    <h2>No content</h2>
    <span>Page: {{page_state}}</span>
    <br/>
    %if defined('subpage'):
      <span>SubPage: {{subpage}}</span>
    %end
  </div>
</div>