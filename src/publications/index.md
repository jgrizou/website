---
style: Default
navbar:
  publications: true
---

<div class="btn-group btn-group-lg" role="group" aria-label="...">
  <button type="button" class="btn btn-default" id="buttonselected">Selected</button>
  <button type="button" class="btn btn-default" id="buttonpertype">Per Type</button>
  <button type="button" class="btn btn-default" id="buttonperyear">Per Year</button>
</div>

<button type="button" class="btn btn-default btn-lg pull-right" id="buttonfullbib">
  <span class="glyphicon glyphicon-list-alt" aria-hidden="true"></span> Full bib file
</button>

<button type="button" class="btn btn-default btn-lg pull-right" id="buttonscholar">
  <span class="glyphicon glyphicon-user" aria-hidden="true"></span> Google Scholar
</button>

<div id="importselected"></div>
<div id="importpertype"></div>
<div id="importperyear"></div>

<script>
$( document ).ready( function () {
    $( "#importselected" ).load( "{{ "selected.html" | relative_path | web_path}}" );
    $( "#importpertype" ).load( "{{ "pertype.html" | relative_path | web_path}}" );
    $( "#importperyear" ).load( "{{ "peryear.html" | relative_path | web_path}}" );

    $("#buttonselected").click(function(){
        $("#importselected").show();
        $("#importpertype").hide();
        $("#importperyear").hide();
    });
    $("#buttonpertype").click(function(){
      $("#importselected").hide();
      $("#importpertype").show();
      $("#importperyear").hide();
    }).trigger( "click" );
    $("#buttonperyear").click(function(){
      $("#importselected").hide();
      $("#importpertype").hide();
      $("#importperyear").show();
    });

    $("#buttonscholar").click(function(){
        window.open("http://scholar.google.fr/citations?user=Fej-hGQAAAAJ&hl=en");
    });

    $("#buttonfullbib").click(function(){
        window.open("jgrizou.bib");
    });
});
</script>
