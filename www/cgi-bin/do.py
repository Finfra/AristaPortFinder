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
  <!-- Accordion -->

  <h2 class="demoHeaders"><img src="/img/eos-screenshot.jpg" alt="" height="42" width=
  "142" style="margin-right: 100px" /> Leaf Switch Port Finder</h2>

  <div id="accordion">
    <div>
      <h3><a href="#">Compute Leaf Switch List</a></h3>

      <div>
        <div id=do>do</div>
        <table id="example" class="display" cellspacing="0" width="1184">
          <thead>
            <tr>
              <th>Name</th>

              <th>Position</th>

              <th>Office</th>

              <th>Age</th>

              <th>Start date</th>

              <th>Salary</th>
            </tr>
          </thead>

          <tfoot>
            <tr>
              <th>Name</th>

              <th>Position</th>

              <th>Office</th>

              <th>Age</th>

              <th>Start date</th>

              <th>Salary</th>
            </tr>
          </tfoot>

          <tbody>
            <tr>
              <td>Tiger Nixon</td>

              <td>System Architect</td>

              <td>Edinburgh</td>

              <td>61</td>

              <td>2011/04/25</td>

              <td>$320,800</td>
            </tr>

            <tr>
              <td>Garrett Winters</td>

              <td>Accountant</td>

              <td>Tokyo</td>

              <td>63</td>

              <td>2011/07/25</td>

              <td>$170,750</td>
            </tr>

            <tr>
              <td>Ashton Cox</td>

              <td>Junior Technical Author</td>

              <td>San Francisco</td>

              <td>66</td>

              <td>2009/01/12</td>

              <td>$86,000</td>
            </tr>

            <tr>
              <td>Cedric Kelly</td>

              <td>Senior Javascript Developer</td>

              <td>Edinburgh</td>

              <td>22</td>

              <td>2012/03/29</td>

              <td>$433,060</td>
            </tr>

            <tr>
              <td>Airi Satou</td>

              <td>Accountant</td>

              <td>Tokyo</td>

              <td>33</td>

              <td>2008/11/28</td>

              <td>$162,700</td>
            </tr>

            <tr>
              <td>Brielle Williamson</td>

              <td>Integration Specialist</td>

              <td>New York</td>

              <td>61</td>

              <td>2012/12/02</td>

              <td>$372,000</td>
            </tr>

            <tr>
              <td>Herrod Chandler</td>

              <td>Sales Assistant</td>

              <td>San Francisco</td>

              <td>59</td>

              <td>2012/08/06</td>

              <td>$137,500</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div>
      <h3><a href="#">Compute Leaf Switch Port View</a></h3>

      <div>
        <div>
          <div align="center">
            <table background="/img/7050TX.png" id="switch" class="port">
              <tr>
                <td id="p1" class="port">1 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p3" class="port">3 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p5" class="port">5 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p7" class="port">7 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p9" class="port">9 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p11" class="port">11 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p13" class="port">13 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p15" class="port">15 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p17" class="port">17 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p19" class="port">19 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p21" class="port">21 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p23" class="port">23 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p25" class="port">25 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p27" class="port">27 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p29" class="port">29 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p31" class="port">31 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p33" class="port">33 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p35" class="port">35 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p37" class="port">37 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p39" class="port">39 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p41" class="port">41 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p43" class="port">43 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p45" class="port">45 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p47" class="port">47 <img src="/img/green.png" height="20" width=
                "20" /></td>
              </tr>

              <tr>
                <td id="p2" class="port">2 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p4" class="port">4 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p6" class="port">6 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p8" class="port">8 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p10" class="port">10 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p12" class="port">12 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p14" class="port">14 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p16" class="port">16 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p18" class="port">18 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p20" class="port">20 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p22" class="port">22 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p24" class="port">24 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p26" class="port">26 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p28" class="port">28 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p30" class="port">30 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p32" class="port">32 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p34" class="port">34 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p36" class="port">36 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p38" class="port">38 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p40" class="port">40 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p42" class="port">42 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p44" class="port">44 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p46" class="port">46 <img src="/img/green.png" height="20" width=
                "20" /></td>

                <td id="p48" class="port">48 <img src="/img/green.png" height="20" width=
                "20" /></td>
              </tr>
            </table>
          </div>

          <div align="center">
            <table>
              <tr>
                <td class="key1"><img src="/img/green.png" height="40" width="40" /></td>

                <td class="val1">Connected</td>

                <td class="key1"><img src="/img/yellow.png" height="40" width="40" /></td>

                <td class="val1">Not Connected</td>

                <td class="key1"><img src="/img/red.png" height="40" width="40" /></td>

                <td class="val1">Disabled</td>

                <td class="key1"><img src="/img/black.jpg" height="40" width="40" /></td>

                <td class="val1">-</td>
              </tr>
            </table>
          </div>
        </div>
      </div>

      <div>
        <h3><a href="#">Compute Leaf Switch Port Status</a></h3>

        <div>
          <table width="100%">
            <tr>
              <td colspan="3">{portname----------------------------------------}</td>
            </tr>

            <tr>
              <td>{key}</td>

              <td>{values}</td>

              <td rowspan="3">VLAN <input type="text" name="VLAN" value="1" />
              <input type="submit" value="Apply" /><br />
              <br />
              ---------<br />
              ---------<br />
              ---------<br /></td>
            </tr>

            <tr>
              <td>{key}</td>

              <td>{values}</td>
            </tr>

            <tr>
              <td>{key}</td>

              <td>{values}</td>
            </tr>
          </table>
          <input type="submit" value="go! Edge Leaf Switch Status" /><br />
        </div>
      </div>

      <div>
        <h3><a href="#">Edge Leaf Switch Status</a></h3>

        <div>
          <table>
            <tr>
              <td>
                <table>
                  
                  <tr>
                    <td colsapan="2">Edge Leaf Switch #1</td>
                  </tr>

                  <tr>
                    <td>{key}</td>

                    <td>{values}</td>
                  </tr>

                  <tr>
                    <td>{key}</td>

                    <td>{values}</td>
                  </tr>
                </table>
              </td>

              <td>
                
            <table>
            <tr>
              <td colsapan="2">Edge Leaf Switch #2</td>
            </tr>

            <tr>
              <td>{key}</td>

              <td>{values}</td>
            </tr>

            <tr>
              <td>{key}</td>

              <td>{values}</td>
            </tr>
          </table>



              </td>

          
        </div>
      </div>
    </div>
  </div>
</body>
</html>

"""