<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type">
    <script type="text/javascript" src="{{ get_url('static', path='js/jquery.min.js') }}" charset="utf-8"></script>
    <script type="text/javascript" src="{{ get_url('static', path='js/jquery.cookie.js') }}" charset="utf-8"></script>
    <script type="text/javascript" src="{{ get_url('static', path='js/jsencrypt.min.js') }}" charset="utf-8"></script>
    <script type="text/javascript" src="{{ get_url('static', path='js/configjsencrypt.js') }}" charset="utf-8"></script>

<div id="hbox">
  <div class="box">
      <h2>Login</h2>
      <p>Please insert your credentials:</p>
      <form id="loginform"  method="post" name="login" onSubmit="return changeFormInputs();">
        <div>
            <label for="username">Username</label>
          <input type="text" name="username" id="username" />
        </div>
        <div>
          <label for="password">Password</label>
          <input type="password" name="password" id="password"/>
        </div>
        <div>
          <button type="submit" id="btnSubmitLoginData" > OK </button>
        </div>
      </form>
      <br />
  </div>
</div>
<style>
    div {
        margin:auto;
        width:20em;
        text-align:center;
        padding: 10px;
    }

    label {
        display:inline-block;
        float:left;
    }

    input {
        background-color:#f8f8f8;
        margin:auto;
        border:1px solid #777;
    }
</style>
<script type="text/javascript">
    function changeFormInputs(){
        //var oldPVal =  document.querySelector("input[name='password']").value
        //document.querySelector("input[name='password']").value = ''
        //var aa = window.btoa(encSvc.encrypt(oldPVal))
        //console.log('aa',aa)
        //document.querySelector("input[name='password']").value = aa
        document.getElementById('loginform').action = 'login'
    }

    $(document).ready(function(){
        /*$('#btnSubmitLoginData')
        .click(function(){
            var usrname = $("input[name='username']").val(),
                parola = $("input[name='password']").val();

            var submitLogin = {
                username: usrname,
                password: encSvc.encrypt(parola)
            };

            $.post('/login',
            submitLogin,
            function(data, status, jqXHR) {// success callback
                console.log('status: ' + status + ', data: ' + data);
            })

        })*/
    });
</script>