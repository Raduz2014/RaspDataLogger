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
      <form action="login" method="post" name="login">
        <div>
            <label for="username">Username</label>
          <input type="text" name="username" id="username" />
        </div>
        <div>
          <label for="password">Password</label>
          <input type="password" name="password" id="password"/>
        </div>
        <div>
          <button type="submit" > OK </button>
          <button type="button" class="close"> Cancel </button>
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