#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "Content-Type: text/html;charset=utf-8"
print ""
print
print """
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="utf-8" />

  <title>Leaf Switch Port Finder</title>
  <link type="text/css" href="/css/smoothness/jquery-ui-1.8.18.custom.css" rel="stylesheet" />
  <link type="text/css" href="/css/jquery-ui.css rel=" />
  <script type="text/javascript" src="/js/jquery-2.1.3.js"></script>
  <script type="text/javascript" src="/js/jquery-ui-1.11/jquery-ui.min.js"></script>
  <script type="text/javascript">
//<![CDATA[
      $(document).ready(function() {
        $("#accordion").accordion({ 
          header: "h3", 
          create: function (event, ui) {$("span#result").html ($("span#result").html () + "<b>Created</b><br>");},
          beforeActivate : function (event, ui){$("span#result").html ($("span#result").html () + ", <b>beforeActivate</b><br>");},
          activate: function (event, ui) {$("span#result").html ($("span#result").html () + "<b>activate</b><br>");} 
        });
        $("#do").click(function(event){
          //alert('hi');
           $( "#accordion" ).accordion({ active: 1 });
        });
      } );
  //]]>
  </script>
  <style type="text/css">
/*<![CDATA[*/
  .demoHeaders {font-size: 250%;  }
  /*]]>*/
  </style>
</head>

<body>
<h1>Just Test, "chmod +x *.py" script is need in linux or unix.</h1>
</body>
</html>

"""